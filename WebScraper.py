import requests
from bs4 import BeautifulSoup

# specify the URL of the webpage you want to scrape
url = "https://minsoo-kim.duckdns.org"

# send a GET request to the URL
response = requests.get(url)

# check if the request was successful (status code 200)
if response.status_code == 200:
    # parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(response.content, "html.parser")

    # find all the links on the page and print their href values
    links = soup.find_all("a")
    for link in links:
        print(link.get("href"))

    # find all the images on the page and print their src values
    images = soup.find_all("img")
    for image in images:
        print(image.get("src"))

    # find the title of the page and print it
    title = soup.find("title")
    print("Title: " + title.text)
else:
    print("Error: Could not retrieve content from " + url)