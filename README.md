# ReadMe
This is a Python script for scraping audio content and metadata from the Japanese Podcast 101 website. It is designed to help you efficiently download audio files and prepare them for use in Anki, a popular spaced repetition flashcard program. The script utilizes web scraping techniques to extract data from the website and organize it for your learning needs.

## Prerequisites

Before using this script, make sure you have the following prerequisites installed:

- Python
- Required Python packages (installable via pip):
  - requests
  - BeautifulSoup (imported as Bs in the script)

You can install the required packages using pip with the following commands:

```bash
pip install requests
pip install beautifulsoup4
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

## How the Script Works

The script uses web scraping to extract audio content and metadata from the Japanese Podcast 101 website. It does the following:

1. Downloads the webpage content from the specified HTML file.

2. Parses the HTML using BeautifulSoup.

3. Extracts audio content for vocabulary and dialogue sections.

4. Retrieves tags associated with the content.

5. Downloads audio files, naming them according to the title and tags.

6. Organizes the audio files for use in Anki, creating appropriate tags.

## Example Usage

Here's an example of how to use the script:

```bash
python main.py --website path/to/your/website.html
```

This command will scrape the specified HTML file and download the audio content, organizing it for Anki.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Special thanks to the developers of BeautifulSoup and the requests library for making web scraping and HTTP requests easier.
- Japanese Podcast 101 for providing valuable language learning resources.

Please feel free to open issues or contribute to this project if you encounter any problems or have suggestions for improvements. Happy learning!


# 📋 Disclaimer and known issues
Any usage of the script is under user's responsibility only. Users of the script must act according to site's terms.

As of today, Innovative Language's terms of use does not forbid usage of crawlers or scrapers on any of their sites. This may change in the future, so be aware.

If you like the services Innovative Language provides you should consider a monthly subscription. Basic programs start at around $5 per month and include support from native speaker teachers.

As with all websites, the site's structure may change in the future and thus, as often happens with scraping scripts, deprecate it. It is not really a question of if the site's source code will change but rather when (so enjoy it while it's still working 😁)

# Similar projects 
https://github.com/nedlir/languagepod101-scraper