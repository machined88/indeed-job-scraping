# Indeed Job Scrapping made by Machined88
import pandas as pd
import requests
import os
from bs4 import BeautifulSoup
from tabulate import tabulate
from time import sleep

print("> > > INDEED JOB SCRAPPER (FR) < < <\n")
userprofile = os.environ["USERPROFILE"]
path = os.path.join(userprofile, "Documents", "job_research_data.csv")      # Set location to save data

while True:
    language_list_fr = ["francais", "français", "french", "france", "fr", "fra"]
    language_list_usa = ["usa", "united states of america", "america", "us"]
    language_list_gb = ["gb", "uk", "england", "scotland", "nothern ireland", "wales"]
    language_list_spa = ["spain", "spa", "sp", "espana", "es", "españa"]
    language_list_ger = ["ger", "germany", "deutsch", "deutschland", "de"]
    language_all = language_list_usa + language_list_fr + language_list_gb + language_list_ger + language_list_spa

    language = input("Enter your location -> (France), (USA), (United Kingdom/UK), (Spain/Espana), (Germany/Deutschland): ").lower()
    while language not in language_all:
        print("nop! retry")
        language = input("Enter your location -> (France), (USA), (UK), (Spain/España): ").lower()
    
    def get_url(position, location):
        if language in language_list_fr:
            template = "https://fr.indeed.com/emplois?q={}&l={}"
            url = template.format(position, location)
            return url
        elif language in language_list_usa:
            template = "https://www.indeed.com/jobs?q={}&l={}"
            url = template.format(position, location)
            return url
        elif language in language_list_gb:
            template = "https://www.indeed.co.uk/jobs?q={}&l={}"
            url = template.format(position, location)
            return url
        elif language in language_list_spa:
            template = "https://es.indeed.com/jobs?q={}&l={}"
            url = template.format(position, location)
            return url
        elif language in language_list_ger:
            template = "https://de.indeed.com/jobs?q={}&l={}"
            url = template.format(position, location)
            return url

    def main(response):
        if response.ok == True:
            soup = BeautifulSoup(response.text, "html5lib")
            cards = soup.find_all("div", "jobsearch-SerpJobCard")
            index = 0

            while index < len(cards):
                try:            #Salary
                    job_salary = cards[index].find("span", "salaryText").text 
                    job_salary = job_salary.replace("\n", "")
                    job_salary = job_salary.replace("\xa0", "")
                    job_salaries.append(job_salary)
                except:
                    job_salaries.append(None)

                try:            #Job title
                    job_title = cards[index].find("h2", "title").text.strip()
                    if cards[index].find("span", "new"):
                        job_title = job_title.replace(cards[index].find("span", "new").text, "")
                    job_title.replace("\n", "")
                    job_titles.append(job_title)
                except:
                    job_salaries.append(None)

                try:            #Company
                    job_company = cards[index].find("span", "company").text.strip()
                    job_companies.append(job_company)
                except:
                    job_companies.append(None)

                try:            #Location
                    job_location = cards[index].find("span", "location accessible-contrast-color-location").text.strip()
                    job_locations.append(job_location)
                except:
                    job_locations.append(None)

                try:            #Date posted
                    job_date = cards[index].find("span", "date").text
                    date_posted.append(job_date)
                except:
                    date_posted.append(None)

                index += 1

    job_titles = []     # Lists to store extracted data
    job_companies = []
    job_locations = []
    date_posted = []
    job_salaries = []

    user_position = input("Enter job position: ")
    user_location = input("Enter job location: ")
    url = get_url(user_position, user_location)
    response0 = requests.get(url)

    url10 = url + "&start=10"    # Access 2nd page
    response10 = requests.get(url10)

    url20 = url + "&start=20"    # Access 3rd page
    response20 = requests.get(url20)

    url30 = url + "&start=30"    # Access 4th page
    response30 = requests.get(url30)

    url40 = url + "&start=40"    # Access 5th page
    response40 = requests.get(url40)

    url50 = url + "&start=50"     # Access 6th page
    response50 = requests.get(url50)

    main(response0)
    main(response10)
    main(response20)
    main(response30)
    main(response40)
    main(response50)

    if len(job_titles) > 0:
        data = {                        #Format data for pd.DataFrame
            'Title': job_titles, 
            'Company': job_companies, 
            'Location': job_locations,
            'Posted at': date_posted,
            'Salary': job_salaries
            }

        scrapper_dataframe = pd.DataFrame(data)    # Print data
        # print(tabulate(scrapper_dataframe, headers="keys", tablefmt="grid", showindex=False))
        pd.set_option("display.max_rows", 50, "display.max_columns", 50, 'display.expand_frame_repr', False) 
        print(tabulate(scrapper_dataframe, headers="keys", tablefmt="fancy_grid"))

        ask_save_file = input("\nDo you want to save this data into a .csv file on /Users/<user>/Documents ? (yes/no): ").lower()     # Save data
        if ask_save_file == "yes" or ask_save_file == "y":
            if os.path.isfile(path) == True:
                ask_replace = input("This file already exists, do you want to replace it ? (yes/no): ").lower()
                if ask_replace == "yes" or ask_replace == "y":
                    scrapper_dataframe.to_csv(path, index=False, encoding='utf-8')
                    print("\n--- .csv file saved on /Users/<user>/Documents ---")
            else:
                scrapper_dataframe.to_csv(path, index=False, encoding='utf-8')
                print("\n--- .csv file saved on /Users/<user>/Documents ---")
    else:
        print("No result found.\n")

    new_research = input("Do you want to make another research ? (yes/no): ").lower()     # Ask user for new research
    if new_research == "yes" or new_research == "y":
        continue
    else:
        input('Press ENTER to exit')
        break
