# Standard Library
import csv
from glob import glob

# Third-party
import genanki


# Custom
# None


def generate_anki_deck() -> None:
    # Read HTML templates
    FRONT = open("html_templates/front.html").read()
    BACK = open("html_templates/back.html").read()
    CSS = open("html_templates/custom_css.css").read()

    # MP3 Files
    MP3 = glob("page_results/mp3_files/*.mp3")

    # Read CSV file
    RESULTS = csv.reader(
        open("page_results/mp3_text/episode_results.csv", mode="r", encoding="utf-8")
    )

    # Create Anki model
    MODEL = genanki.Model(
        1607392319,
        "Jp - Japanese Sentence Audio",
        fields=[
            {"name": "Sentence"},
            {"name": "Translation"},
            {"name": "Definitions"},
            {"name": "Target Word"},
            {"name": "Focus Morph"},
            {"name": "Screenshot"},
            {"name": "Sentence Audio"},
            {"name": "Word Audio"},
            {"name": "Notes"},
            {"name": "Explanation"},
            {"name": "Source Title Field"},
            {"name": "Source URL Field"},
        ],
        templates=[
            {
                "name": "Sentence Audio",
                "qfmt": FRONT,
                "afmt": BACK,
            }
        ],
        css=CSS,
    )

    # Create Anki deck
    default_deck = genanki.Deck(2059400110, "Jp101")

    # Populate Anki deck with notes
    for row in RESULTS:
        sentence, sentence_audio, tags = row[0], row[1], row[2]
        anki_tags = [i for i in tags.split()]

        fields = ["" for i in range(12)]
        fields[0] = sentence
        fields[6] = sentence_audio

        note = genanki.Note(model=MODEL, fields=fields, tags=anki_tags)
        default_deck.add_note(note)

    # Create Anki package and save to file
    anki_pkg = genanki.Package(default_deck)
    anki_pkg.media_files = MP3

    anki_pkg.write_to_file("anki_folder/output.apkg")
