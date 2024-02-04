# News-Reader-App

This Python script is designed to scrape heading and overview of news from a URL The output/fetched information is saved in JSON format.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)

## Prerequisites

- Python 3.x
- Required Python libraries (install via `pip install -r requirements.txt`):
  - `PyPDF2`
  - `bs4`
  - `requests`

## Installation

1. Clone the repository:

   ```bash
   https://github.com/yash1302/News-Reader-App.git
   ```

2. Navigate to the project directory:

   ```bash
   cd NEWS-READER-APP
   ```

3. Setup virtual environment:
   ```bash
   python -m venv NEWS-READER-APP
   ```
4. Activate virtual environment:
   ```bash
   source NEWS-READER-APP/Scripts/activate
   ```
5. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Edit the `config.json` file to configure the URL and Number of pages to extract information from.

2. Run the main script:

   ```bash
   python main.py
   ```

3. The extracted information will be stored in `output.json` file in the project directory.

## Configuration

- **config.json**: This file contains the input configuration for the script i.e. URL of the PDF file and number of pages to extract information from.

## Author

- Yashvardhan Jadhav
