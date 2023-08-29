import requests
from bs4 import BeautifulSoup
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

        # Initialize dictionaries to store the data
        country_capital_dict = {}
        country_population_dict = {}
        country_area_dict = {}

        # Loop through the elements and create key-value pairs
        for country_name, country_capital, country_pop, country_area in zip(country_names, country_capitals, country_pops, country_areas):
            country = country_name.text.strip()
            capital = country_capital.text.strip()
            pop = country_pop.text.strip()
            area = country_area.text.strip()

            country_capital_dict[country] = capital
            country_population_dict[country] = pop
            country_area_dict[country] = area

        return country_capital_dict, country_population_dict, country_area_dict

    else:
        print("Failed to retrieve the webpage")
        return None, None, None

# Call the function and store the results in variables
capital_dict, population_dict, area_dict = scrape_country_data()

if capital_dict:
    print(capital_dict)

    # Sort the countries by population
    sorted_population = sorted(population_dict.items(), key=lambda item: int(item[1]))
    print(sorted_population)

    # Sort the countries by area
    sorted_area = sorted(area_dict.items(), key=lambda item: float(item[1]))
    print(sorted_area)


