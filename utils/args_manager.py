# Standard
import argparse

# Pip
# None

# Custom
# None

my_parser = argparse.ArgumentParser()
my_parser.add_argument("--website", "--w", type=str,
                       help="Enter the page manually")
my_parser.add_argument(
    "--automatic",
    "--a",
    action="store_true",
    help="downloads the first page saved in the directory",
)
my_parser.add_argument("--clear", "--c", action="store_true",
                       help="clears old files")

my_parser.add_argument("--move-audio","--ma",action="store_true", 
help="Moves the audios to the Anki folder.")
args = my_parser.parse_args()
