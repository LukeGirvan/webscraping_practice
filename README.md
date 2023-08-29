# Web Scraping Practice: Country Data Extraction
This Python script demonstrates web scraping techniques using the requests library to make HTTP requests and BeautifulSoup for parsing HTML content. The goal is to extract data from a sample website and organize it into dictionaries for further analysis.

## Code Explanation
- The script begins by sending a GET request to the specified URL and checks if the request was successful (HTTP status code 200).

- It then uses BeautifulSoup to parse the HTML content of the webpage and extracts data by finding elements with specific CSS classes.

- The extracted data is stored in dictionaries where the country name serves as the key and the respective data (capital, population, or area) serves as the value.

- Finally, the script prints the extracted data and sorts the data based on population and area for further analysis.

### Error Handling
If the GET request fails (status code other than 200), the script prints a message indicating the failure.
Note
This code is intended for educational purposes and practice in web scraping. Always respect the website's terms of service and robots.txt file when scraping data from websites, and consider the legality and ethics of web scraping in any specific context.

