import requests

from bs4 import BeautifulSoup

# URL that we want to scrape.
url = "https://www.zillow.com/missoula-mt/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22west%22%3A-114.76198615332031%2C%22east%22%3A-113.38732184667968%2C%22south%22%3A46.532002850210795%2C%22north%22%3A47.29000274332481%7D%2C%22usersSearchTerm%22%3A%22Missoula%2C%20MT%22%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A53359%2C%22regionType%22%3A6%7D%5D%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D"

# Get request to the URL
response = requests.get(url)

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
