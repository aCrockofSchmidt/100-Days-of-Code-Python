import os

import requests
import datetime as dt
from dateutil.relativedelta import relativedelta

TEQUILA_APIKEY = os.environ.get("TEQUILA_API_KEY")

class FlightSearch:

    def code_search(self, city):
        """ this method returns IATA CODES for submitted cities"""

        tequila_location_endpoint = "https://tequila-api.kiwi.com/locations/query"

        tequila_location_params = {
            "term": city,
            "location_types": "city",
        }

        tequila_header = {
            "apikey": TEQUILA_APIKEY
        }

        tequila_code_response = requests.get(
            url=tequila_location_endpoint,
            headers=tequila_header,
            params=tequila_location_params
        )
        tequila_code_response.raise_for_status()
        code_data = tequila_code_response.json()["locations"]
        return code_data[0]["code"]

    def price_search(self, city_code):
        """this method returns flight data based on submitted city AITA code"""

        home_city = "LON"
        tomorrow = dt.date.today() + dt.timedelta(1)
        six_months = tomorrow + relativedelta(months=6)

        tequila_search_endpoint = "https://tequila-api.kiwi.com/v2/search"

        tequila_search_params = {
            "fly_from": home_city,
            "fly_to": city_code,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "date_from": tomorrow.strftime("%d/%m/%Y"),
            "date_to": six_months.strftime("%d/%m/%Y"),
            "flight_type": "round",
            "one_for_city": 1,
            "curr": "GBP",
            "max_stopovers": 0,
        }

        tequila_header = {
            "apikey": "ZDSTH6eYt5X5Uo2P_az-0DSD708lNUmW"
        }

        price_response = requests.get(
            url=tequila_search_endpoint,
            headers=tequila_header,
            params=tequila_search_params,
        )
        price_response.raise_for_status()
        price_data = price_response.json()["data"][0]
        return price_data

