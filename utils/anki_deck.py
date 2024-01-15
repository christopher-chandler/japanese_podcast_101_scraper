# Standard Library
import csv

# Third-party
import genanki

# Custom
# None


def generate_anki_deck() -> None:

    # Read HTML templates
    FRONT = open("html_templates/front.html").read()
    BACK = open("html_templates/back.html").read()

    # Read CSV file
    RESULTS = csv.reader(
        open("page_results/mp3_text/episode_results.csv", mode="r", encoding="utf-8")
    )

    # Create Anki model
    MODEL = genanki.Model(
        1607392319,
        "Default",
        fields=[
            {"name": "Sentence"},
            {"name": "Sentence Audio"},
        ],
        templates=[
            {
                "name": "Card 1",
                "qfmt": FRONT,
                "afmt": BACK,
            }
        ],
    )

    # Create Anki deck
    default_deck = genanki.Deck(2059400110, "Default")

    # Populate Anki deck with notes
    for row in RESULTS:
        sentence, audio, tags = row[0], row[1], row[2]
        anki_tags = ["jp::" + i for i in tags.split()]
        note = genanki.Note(model=MODEL, fields=[sentence, audio], tags=anki_tags)
        default_deck.add_note(note)

    # Create Anki package and save to file
    genanki.Package(default_deck).write_to_file("anki_folder/output.apkg")
