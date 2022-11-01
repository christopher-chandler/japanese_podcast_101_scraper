import csv
import glob
import os
import bs4
from utils.prog import update_progress

def data_prep():
    open("mp3_text/episode_results.csv", mode="w+")
    files = glob.glob('mp3_files/*.mp3')
    for f in files:
        os.remove(f)

def get_text_audio(section: bs4.element.ResultSet) -> dict:
    results = dict()
    for row in section:

        if row.findAll():
            data_text = row.findAll()[0].get("data-text")
            data_url = row.findAll()[0].get("data-url")
            if data_url in results.values():
                break
            else:
                results[data_text] = data_url
    return results


def get_tags(tags: bs4.element.ResultSet) -> list:
    results = list()
    for row in tags:
        results.append(row.getText().strip())

    return results


def get_title(title):
    for row in title:
        if row.findAll():
            return row.findAll()[0].getText().replace(" ", "_").lower()


def download_audio(session, save_type, save_name, audio,tags):

    with session:
        with open(
            "mp3_text/episode_results.csv", mode="a+", encoding="utf-8"
        ) as save_results:
            csv_writer = csv.writer(save_results)
            c = 0
            for entry in audio:
                c += 1

                update_progress(c/len(audio))
                audio_file = session.get(audio.get(entry))
                res_name = f"{save_type}_{save_name}_{c}"
                save = open(f"mp3_files/{save_type}_{save_name}_{c}.mp3", mode="wb")
                save.write(audio_file.content)
                sound_name = f"[sound:{res_name}.mp3]"

                csv_writer.writerow((entry, sound_name,tags))
