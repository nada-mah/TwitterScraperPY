# Twitter Scraper
This project is a Python script that scrapes Twitter accounts for mentions of a specific stock symbol. It uses Selenium and BeautifulSoup libraries to extract data from the HTML content of the Twitter profiles.
## Requirements

- Python (version 3.6 or higher)
- Selenium library
- webdriver-manager library
- BeautifulSoup library
- schedule library


## Installation

1. Clone the repository:

- `git clone https://github.com/your-username/twitter-scraper.git`

2. Install the required Python libraries

3. Set up environment variables:

- Create a `.env` file in the project directory.
- Add the following lines to the `.env` file:

  ```
  USERNAME=your_twitter_username
  PASSWORD=your_twitter_password
  ```

## Usage

1. Run the script:

- `python script.py`


2. Enter the Twitter account URLs:

- The script will prompt you to enter 10 Twitter account URLs.
- Make sure to provide valid URLs in the format `https://twitter.com/username`.

3. Enter the stock symbol:

- The script will prompt you to enter the stock symbol to search for.
- Enter the symbol starting with a "$" sign (e.g., $TSLA).

4. Enter the time interval:

- The script will prompt you to enter the time interval in minutes between scraping sessions.
- Enter an integer value representing the time interval.

5. View the results:

- The script will display the initial count of mentions of the stock symbol in the profiles.
- It will then start scraping the profiles periodically according to the specified time interval.
- The updated count of mentions will be displayed after each scraping session.
