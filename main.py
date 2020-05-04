# Written by Tyler Paplham
# -----------------------------------
# This is a simple web scraping script
# to retrieve a list of the current FDA
# approved drugs and dump them into a
# text file. This script was built for
# the MyMedicineAsssistant Alexa skill.
# -----------------------------------

import os
import requests
import string
from bs4 import BeautifulSoup

if os.path.exists("fda_drug_list.txt"):
    os.remove("fda_drug_list.txt")

output_file = open("fda_drug_list.txt", "a")
base_url = "https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm?event=browseByLetter.page&productLetter="
alpha_list = list(string.ascii_uppercase)

for letter in alpha_list:
    url = base_url + letter
    request_object = requests.get(url)
    if request_object.status_code == 200:
        soup = BeautifulSoup(request_object.content, "html.parser")
        drugs = soup.find_all('a', title="Click to expand drug name")
        for drug in drugs:
            output_file.write(drug.text + "\n")

output_file.close()
print("--------\nOPERATION COMPLETED.\n--------")
