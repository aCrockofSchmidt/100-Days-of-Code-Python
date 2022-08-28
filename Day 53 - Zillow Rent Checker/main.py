import requests
from bs4 import BeautifulSoup
import json

GOOGLE_FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLScaYfmNdEb6sdzPjgO5ML7WAJyDMvOsKiCl51sWQXbn_wPi4A/viewform?usp=sf_link"
ZILLOW_URL = "https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.64481631640625%2C%22east%22%3A-122.22184268359375%2C%22south%22%3A37.64220165564354%2C%22north%22%3A37.90814309464718%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A665005%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D"

zillow_header = {
    "accept-language": "en-US,en;q=0.9",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
    "access-control-allow-credentials": "true",
}

response = requests.get(ZILLOW_URL, headers=zillow_header)
rental_data = response.text

soup = BeautifulSoup(rental_data, "lxml")
print(soup.text)

# rentals = json.loads(soup.find(name="script", attrs={"type": "application/ld+json"}))
# print(rentals)
# for listing in rentals:
#     print(listing.getText)


# ZILLOW IS NO LONGER WORKING WITH MY BROWSER SO I'VE STOPPED ATTEMPTING TO FINISH THIS CHALLENGE
# IT BECAME OBVIOUS THAT THE WEBSITE HAS ALTERED SINCE THE CHALLENGE WAS CREATED ANYWAY
# RESULTS ARE STORED IN A SCRIPT WHICH ALTERED THE CAPSTONE AND RENDERED THE INSTRUCTOR SOLUTION USELESS
# THIS TRULY WAS REDUNDANT ANYWAY - THIS SCRAPING SECTION OF THE COURSE NEEDS UPDATING BADLY



