# Standard
import csv
import glob
import os
import shutil

#Pip
import bs4

# Custom
from utils.progress_bar import update_progress


def data_prep():
    open("mp3_text/episode_results.csv", mode="w+")
    files = glob.glob("mp3_files/*.mp3")
    for f in files:
        os.remove(f)
    os.remove("mp3_text/episode_results.csv")


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


def download_audio(session, save_type, save_name, audio, tags):

    with session:
        with open(
            "mp3_text/episode_results.csv", mode="a+", encoding="utf-8"
        ) as save_results:
            csv_writer = csv.writer(save_results)
            c = 0
            for entry in audio:
                c += 1
                prog = c / len(audio)
                update_progress(prog, save_type)
                audio_file = session.get(audio.get(entry))
                res_name = f"{save_type}_{save_name}_{c}"
                save = open(f"mp3_files/{save_type}_{save_name}_{c}.mp3", mode="wb")
                save.write(audio_file.content)
                sound_name = f"[sound:{res_name}.mp3]"

                csv_writer.writerow((entry, sound_name, tags))


def move_audio():
    source_folder = "/Users/christopherchandler/Github/Python/Jp101Scrapper/mp3_files" 
    destination_folder = "/Users/christopherchandler/Library/Application Support/Anki2/Main Anki/collection.media"
    
    audio_file = [mp3 for mp3 in glob.iglob(f"{source_folder}/*.mp3")]

    if audio_file:

        for mp3 in glob.iglob(f"{source_folder}/*.mp3"):
            old_file_destination = mp3.split("/")[-1]
            new_file_destionation = f"{destination_folder}/{file}"

            shutil.move(old_file_destination, new_file_destionation)
    else: 
        print("There are no audio files to be moved. Check the mp3_files folder.")
