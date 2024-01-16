# Standard
import argparse

# Pip
# None

# Custom
# None

jp_podcast_parser = argparse.ArgumentParser()
jp_podcast_parser.add_argument(
    "--website", "--w", type=str, help="Enter the page manually"
)
jp_podcast_parser.add_argument(
    "--automatic",
    "--a",
    action="store_true",
    help="downloads the first page saved in the directory",
)
jp_podcast_parser.add_argument(
    "--clear", "--c", action="store_true", help="clears old files"
)
jp_podcast_parser.add_argument(
    "--file_path", type=str, help="Specify the path of the audio file"
)

jp_podcast_parser.add_argument(
    "--move-audio",
    "--ma",
    action="store_true",
    help="Moves the audios to the Anki folder.",
)
args = jp_podcast_parser.parse_args()
