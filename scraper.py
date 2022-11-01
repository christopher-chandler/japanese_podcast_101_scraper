# Standard
import argparse
import glob


# Pip
import requests
from bs4 import BeautifulSoup as Bs

# Custom
from utils.args import args
from utils.data_scraper import get_text_audio, get_tags, download_audio, get_title, data_prep

data_prep()

session = requests.Session()
session.headers.update(
    {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/63.0.3239.132 Safari/537.36"
    }
)


def run(page):

    soup = Bs(page, "html.parser")

    vocab = soup.findAll(class_="lsn3-lesson-vocabulary__td--recorder")
    dialog = soup.findAll(class_="lsn3-lesson-dialogue__td--recorder")
    tags = soup.findAll(class_="r101-headline__appears-in")

    vocab_res = get_text_audio(vocab)
    dialog_res = get_text_audio(dialog)
    tag_res = get_tags(tags)
    title = soup.findAll(class_="r101-headline__cell-a")
    title_res = get_title(title)

    if bool(tag_res) is False:
        anki_tags = f"{title_res} japanese_podcast_101"
    else:
        tag_res.append("japanese_podcast_101")
        formatted_tags = [tag.replace(" ","_") for tag in tag_res]
        anki_tags = " ".join(formatted_tags)

    download_audio(session, "dialog", title_res, dialog_res,tags=anki_tags)
    download_audio(session, "vocab_examples", title_res, vocab_res, tags=anki_tags)


if __name__ == "__main__":

    if args.website:
        website = open(args.website, mode="r", encoding="utf-8").read()
        run(website)

    if args.automatic:
        in_file = glob.glob("*.html")[0]
        website = open(in_file, mode="r", encoding="utf-8").read()
        run(website)

