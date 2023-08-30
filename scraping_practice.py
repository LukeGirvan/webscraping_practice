import requests
from bs4 import BeautifulSoup
import pandas as pd
# Scraping a dummy site to practice extracting data from websites

def scrape_country_data():
    # Send a GET request to the website
    url = "https://www.scrapethissite.com/pages/simple/"
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all elements with class "country-name"
        country_names = soup.find_all(class_="country-name")

        # Find all elements with class "country-capital"
        country_capitals = soup.find_all(class_="country-capital")

        # Find all elements with class "country-population"
        country_pops = soup.find_all(class_="country-population")

        # Find all elements with class "country-area"
        country_areas = soup.find_all(class_="country-area")

        # Make a list to store the data before we put it in a pandas dataframe
        data = []

        # Loop through the data on the website and append it in a list of all 4 to data which we will add to a dataframe later
        for country_name, country_capital, country_pop, country_area in zip(country_names, country_capitals, country_pops, country_areas):
            country = country_name.text.strip()
            capital = country_capital.text.strip()
            pop = country_pop.text.strip()
            area = country_area.text.strip()

            row = [country, capital, pop, area]
            data.append(row)
        # Make the dataframe and name the columns appropriately
        panda_df = pd.DataFrame(data, columns=["Country Name", "Capital", "Population", "Area(km2)"])
        return panda_df
    else:
        print("Failed to retrieve the webpage")
        return None, None, None

print(scrape_country_data())


