import requests
import random
from bs4 import BeautifulSoup

# URL that we want to scrape.
url = "https://www.zillow.com/missoula-mt/homes/for_sale/"

user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
]

headers = {
    'User-Agent': random.choice(user_agents)
}

# Get request to the URL
# Had to add headers to mimic a browser request. 
# Zillow knows I am sending THE BOTS.
response = requests.get(url, headers=headers)

#Validate that the request went through.
if response.status_code == 200:
    # response.text is apart of the response object and contains the HTML of the page including the status response and the headers.

    html_content = response.text
    print("Page scraped successfully!")

    # Parse the HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    print(soup.title)

else:
    print(f"Failed to retrieve the page. Status code:", response.status_code)
