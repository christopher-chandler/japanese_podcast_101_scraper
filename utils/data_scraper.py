# Standard
import csv
import glob
import os
import shutil

# Pip
import bs4

# Custom
from utils.progress_bar import update_progress


def data_prep():
    open("page_results/mp3_text/episode_results.csv", mode="w+")
    files = glob.glob("mp3_files/*.mp3")
    for f in files:
        os.remove(f)
    os.remove("page_results/mp3_text/episode_results.csv")


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


def download_audio(session, save_type, save_name, scrapped_audio, tags):

    with session:
        with open(
            "page_results/mp3_text/episode_results.csv", mode="a+", encoding="utf-8"
        ) as save_results:
            csv_writer = csv.writer(save_results)

            c = 0

            for mp3 in scrapped_audio:
                c += 1
                prog = c / len(scrapped_audio)
                update_progress(prog, save_type)
                audio_file = session.get(scrapped_audio.get(mp3))
                res_name = f"{save_type}_{save_name}_{c}"
                save = open(
                    f"page_results/mp3_files/{save_type}_{save_name}_{c}.mp3", mode="wb"
                )
                save.write(audio_file.content)
                sound_name = f"[sound:{res_name}.mp3]"

                csv_writer.writerow((mp3, sound_name, tags))


def move_audio(destination_folder: str):
    source_folder = "page_results/mp3_files"

    audio_file = [mp3 for mp3 in glob.iglob(f"{source_folder}/*.mp3")]

    if audio_file:

        for mp3 in glob.iglob(f"{source_folder}/*.mp3"):
            old_file_destination = mp3.split("/")[-1]
            new_file_destination = f"{destination_folder}/{old_file_destination}"
            shutil.move(mp3, new_file_destination)
    else:
        print("There are no audio files to be moved. Check the mp3_files folder.")
