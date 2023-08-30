from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
# Scraping a site with data on country size and population

def scrape_country_data():
    # Send a GET request to the website
    driver = webdriver.Chrome()
    url = "https://www.scrapethissite.com/pages/simple/"
    response = driver.get(url)

    # Check if the request was successful

    # Find all elements with class "country-name"
    country_names = driver.find_elements(By.CLASS_NAME, "country-name")

    # Find all elements with class "country-capital"
    country_capitals = driver.find_elements(By.CLASS_NAME,"country-capital")

    # Find all elements with class "country-population"
    country_pops = driver.find_elements(By.CLASS_NAME,"country-population")

    # Find all elements with class "country-area"
    country_areas = driver.find_elements(By.CLASS_NAME,"country-area")

    # Make a list to store the data before we put it in a pandas dataframe
    data = []

    for country_name, country_capital, country_pop, country_area in zip(country_names, country_capitals, country_pops, country_areas):
        country = country_name.text.strip()
        capital = country_capital.text.strip()
        pop = country_pop.text.strip()
        area = country_area.text.strip()

        row = [country, capital, pop, area]
        data.append(row)

    scrape_df = pd.DataFrame(data, columns=["Country Name", "Capital", "Population", "Area(km2)"])

    # Turning the data into a csv file and uploading to an aws s3 bucket
    
    scrape_df.to_csv("CountrySizePopData.csv", index=False,)


    # Now getting data from wikipedia this is about countries and how much coffee the produce each year 

    driver.get("https://en.wikipedia.org/wiki/List_of_countries_by_coffee_production")

    wiki_store = []

    # Had to fix an issue that appeared when splitting the data by hard coding and manually renaming countries with multiple words in their name

    for i in range(1,52):
        wikki_data = driver.find_element(By.XPATH,f'//*[@id="mw-content-text"]/div[1]/table/tbody/tr[{i}]')
        row = wikki_data.text.split(' ')
        if row[1] == "China(2013–14":
            row[1] = "China"
            row.remove(row[2])
        if row[1] == "Ivory":
            row[1] = "Ivory Coast"
            row.remove(row[2])
        if row[1] == "Costa":
            row[1] = "Costa Rica"
            row.remove(row[2])
        if row[1] == "Papua":
            row[1] = "Papua New Guinea"
            row.remove(row[2])
            row.remove(row[2])
        if row[1] == "El":
            row[1] = "El Salvador"
            row.remove(row[2])
        if row[1] == "Dominican":
            row[1] = "Dominican Republic"
            row.remove(row[2])
        if row[1] == "Democratic":
            row[1] = "Democratic Republic of the congo"
            row.remove(row[2])
            row.remove(row[2])
            row.remove(row[2])
            row.remove(row[2])
        if row[1] == "Timor":
            row[1] = "Timor Leste"
            row.remove(row[2])
        if row[1] == "Central":
            row[1] = "Central African Republic"
            row.remove(row[2])
            row.remove(row[2])
        if row[1] == "Sierra":
            row[1] = "Sierra Leone"
            row.remove(row[2])
        if row[1] == "Trinidad":
            row[1] = "Trinidad and Tobago"
            row.remove(row[2])
            row.remove(row[2])
        wiki_store.append(row)

    # Turning the data to a pandas dataframe 
    
    wiki_df = pd.DataFrame(wiki_store, columns=["Rank", "Country Name", "Bags Made", "Tonnes", "Pounds"])

    # Turning the data into a csv file and uploading to an aws s3 bucket
    
    wiki_df.to_csv("CountryCoffeeData.csv", sep=',', index=False,)


    

print(scrape_country_data())


