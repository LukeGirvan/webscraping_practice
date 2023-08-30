# Web Scraping Practice: Country Data Extraction
This Python script demonstrates web scraping techniques using the requests library to make HTTP requests and BeautifulSoup for parsing HTML content. The goal is to extract data from a sample website and put it into a pandas dataframe for further analysis.

## Code Explanation
This script performs the following tasks:

-Sends a GET request to the specified website: ScrapeThisSite Simple Page.

-Parses the HTML content of the page using BeautifulSoup.

-Extracts data from elements with the following classes:
country-name: Country names.
country-capital: Capital cities.
country-population: Population figures.
country-area: Country areas in square kilometers.

-Creates a Pandas DataFrame to store the extracted data, with columns named appropriately: "Country Name," "Capital," "Population," and "Area(km2)."

-Returns the Pandas DataFrame containing the extracted data.

### Error Handling
If the script fails to retrieve the webpage (HTTP status code other than 200), it will print "Failed to retrieve the webpage" and return None.

Ensure that you respect the website's terms of service and policies while scraping data from it.

This script serves as a basic example of web scraping for educational purposes. For more complex and real-world scenarios, consider using more robust tools and handling potential issues like exceptions and error handling.







