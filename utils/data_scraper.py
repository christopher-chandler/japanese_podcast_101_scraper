# Standard
import csv
import glob
import os
import re
import shutil

# Pip
import bs4

# Custom
from utils.progress_bar import update_progress


def remove_punctuation(input_string: str) -> str:
    # Define a regex pattern to match punctuation
    punctuation_pattern = re.compile(r"[^\w\s]")

    # Use the pattern to replace punctuation with an empty string
    result_string = re.sub(punctuation_pattern, "", input_string)

    return result_string


def data_prep() -> None:
    """
    Perform data preparation tasks.

    This function creates an empty CSV file at "page_results/mp3_text/episode_results.csv",
    removes all MP3 files in the "mp3_files" directory, and finally deletes the CSV file.

    Returns:
        None
    """

    # Mp3 files
    mp3_files = glob.glob("mp3_files/*.mp3")

    for mp3 in mp3_files:
        os.remove(mp3)

    # CSV results
    os.remove("page_results/mp3_text/episode_results.csv")


def get_text_audio(section: bs4.element.ResultSet) -> dict:
    """
    Extracts text and corresponding audio URLs from a BeautifulSoup ResultSet.

    Args:
        section (bs4.element.ResultSet): A ResultSet containing HTML elements.

    Returns:
        dict: A dictionary mapping text to audio URLs.
    """
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
    """
    Extracts and returns a list of tags from a BeautifulSoup ResultSet.

    Args:
        tags (bs4.element.ResultSet): A ResultSet containing HTML elements.

    Returns:
        list: A list of tags.
    """
    results = list()
    for row in tags:
        results.append(row.getText().strip())

    return results


def get_title(title: bs4.element.ResultSet) -> str:
    """
    Extracts and returns the title from a BeautifulSoup ResultSet.

    Args:
        title (bs4.element.ResultSet): A ResultSet containing HTML elements.

    Returns:
        str: The title with spaces replaced by underscores and converted to lowercase.
    """
    for row in title:
        if row.findAll():
            raw_title = row.findAll()[0].getText().replace(" ", "_").lower()
            return raw_title


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
                save_name = remove_punctuation(save_name)

                audio_file_name = f"{save_type}_{save_name}_{c}"

                save = open(
                    f"page_results/mp3_files/{save_type}_{save_name}_{c}.mp3", mode="wb"
                )
                save.write(audio_file.content)
                clean_audio_file_name = remove_punctuation(audio_file_name)

                mp3_file_name = f"[sound:{clean_audio_file_name}.mp3]"

                csv_writer.writerow((mp3, mp3_file_name, tags))


def move_audio(destination_folder: str):
    """
    Move audio files from the source folder to the specified destination folder.

    Args:
        destination_folder (str): The path to the destination folder.

    Returns:
        None
    """
    source_folder = "page_results/mp3_files"

    audio_files = [mp3 for mp3 in glob.iglob(f"{source_folder}/*.mp3")]

    if audio_files:
        for mp3 in audio_files:
            old_file_destination = mp3.split("/")[-1]
            new_file_destination = f"{destination_folder}/{old_file_destination}"
            shutil.move(mp3, new_file_destination)
    else:
        print("There are no audio files to be moved. Check the mp3_files folder.")
