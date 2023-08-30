# Data Scraping and Transformation Script
This Python script utilizes Selenium to scrape data from two distinct websites, transforming it into Pandas DataFrames, and subsequently exporting the data into CSV files. Additionally, it includes functionality to push the generated CSV files to an AWS (Amazon Web Services) S3 bucket. While this script may not necessarily be intended for general use, it serves as a practical example of web scraping and data processing.

## Overview
The script performs the following actions:

-Web Scraping:

-Utilizes Selenium to scrape data from two websites.
The first website, "https://www.scrapethissite.com/pages/simple/", is used to obtain information on country size, population, capital, and area.
The second website, "https://en.wikipedia.org/wiki/List_of_countries_by_coffee_production", is used to retrieve data on coffee production by country.
Data Transformation:

-For each website, the scraped data is organized into separate Pandas DataFrames.
The first DataFrame contains information about country size and population, with columns: "Country Name," "Capital," "Population," and "Area(km2)."
The second DataFrame contains data on coffee production, with columns: "Rank," "Country Name," "Bags Made," "Tonnes," and "Pounds."
CSV File Creation:

-The script creates two CSV files in the local directory:
CountrySizePopData.csv for the country size and population data.
CountryCoffeeData.csv for the coffee production data.

-AWS Integration (Optional):
I then uploaded the csv files to an amazon AWS S3 Bucket to practice pushing the data gained from the code to the cloud.








