# Python Web-Scraper for FDA Approved Medications
A python script to scrape all current FDA approved drugs from [fda.gov](https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm).

## Background
This script was created to scrape a list of all current FDA approved drugs in order to create a custom Alexa skill slot type that validates drug names.

## Implementation
The scraper uses the [request](https://requests.readthedocs.io/en/master/) module to make an HTTP request to retrieve the webpage. The [beautiful soup](https://www.crummy.com/software/BeautifulSoup/) module then turns the HTML content into an object that can return certain HTML elements based on filtering arguments. This is used to get all the drug names from each alphabetical webpage (there is a webpage for drugs starting with 'A', 'B', and so on). These drug names are appended to *fda_drug_list.txt*  which serves as the final output of the web-scraper.

## Running the Scraper
This project uses [pipenv](https://github.com/pypa/pipenv) for dependency management. You can install pipenv for your user account using `pip install --user pipenv`.

After pipenv is installed:

1. Run `pipenv install` in the script's directory to install dependencies
2. Run the code using the command `pipenv run python3 main.py`
