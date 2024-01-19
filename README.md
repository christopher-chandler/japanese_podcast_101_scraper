# Japanese Podcast 101 scrapper
This is a Python script for scraping audio content and metadata from the Japanese Podcast 101 website. It is designed to help you efficiently download audio files and prepare them for use in Anki, a popular spaced repetition flashcard program. The script utilizes web scraping techniques to extract data from the website and organize it for your learning needs.

## Prerequisites

You can install the required packages using pip with the following commands:

```bash
pip install -r requirements
```

## Getting Started

To get started with this script, follow these steps:

1. Clone or download this repository to your local machine.

2. Ensure you have the required prerequisites installed.

3. Make sure you have HTML files from the Japanese Podcast 101 website that you want to scrape. You can either specify the HTML file using the `--website` argument or let the script automatically find an HTML file in the current directory.

4. Run the script by executing `main.py`.

## Usage

The script provides several options, which you can specify using command-line arguments:
- `--website`: Specify the path to the HTML file from the Japanese Podcast 101 website. This option allows you to manually provide the HTML content to scrape.
- `--automatic`: If you don't specify the `--website` argument, the script will automatically search for HTML files in the current directory and use the first one it finds for scraping.
- `--clear`: Use this option to clean up any temporary data files created during the scraping process.
- `--move_audio`: This option moves the downloaded audio files to a designated folder.
- `--file_path`: This option designate the folder for the audio files.


## How the Script Works

The script uses web scraping to extract audio content and metadata from the Japanese Podcast 101 website. 
It does the following:

1. Downloads the webpage content from the specified HTML file.
2. Parses the HTML using BeautifulSoup.
3. Extracts audio content for vocabulary and dialogue sections.
4. Retrieves tags associated with the content.
5. Downloads audio files, naming them according to the title and tags.
6. Organizes the audio files for use in Anki, creating appropriate tags.

## Example Usage

Here's an example of how to use the script:

You have to manually download the source code of the webpage and 
then pass the respective file path to the argument. 

```bash
python main.py --website path/to/your/website.html
```

This command will scrape the specified HTML file and download the audio content, organizing it for Anki.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
Please feel free to open issues or contribute to this project if you encounter 
any problems or have suggestions for improvements. Happy learning!


# 📋 Disclaimer and Recognized Issues
The script's usage is solely the responsibility of the user. Users must adhere to the site's terms.

As of the present date, Innovative Language's terms of use do not explicitly prohibit the use of crawlers or scrapers on any of their sites. However, this policy may change in the future, so users should stay informed.

If you appreciate the services offered by Innovative Language, consider opting for a monthly subscription. Basic programs are available starting at approximately $5 per month, inclusive of support from native speaker teachers.

Like all websites, the site's structure may undergo changes in the future, potentially rendering scraping scripts obsolete. The likelihood of the site's source code evolving is not a matter of "if" but rather "when," so make the most of it while it still functions 😁.

# 🔒 License
The content featured on the websites belongs to the original creators (Innovative Language), and I disclaim any association with it.

The license provided pertains solely to the script and not to the downloaded content.

# Similar projects 
https://github.com/nedlir/languagepod101-scraper
