# Standard
import argparse

# Pip
# None

# Custom
# None

my_parser = argparse.ArgumentParser()
my_parser.add_argument("--website", "--w", type=str, help="Enter the page manually")
my_parser.add_argument("--automatic", "--a", action = "store_true",
                       help="downloads the first page saved in the directory")

args = my_parser.parse_args()