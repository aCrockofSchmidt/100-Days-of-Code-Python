import requests

sheety_endpoint = "https://api.sheety.co/bc3b9fa45f39d8978d4e55aee4d69a6f/flightDeals/prices"


class DataManager:

    def sheety_get(self):
        """ this method retrieves data from Google spreadsheet"""
        sheety_response = requests.get(url=sheety_endpoint)
        sheety_response.raise_for_status()
        data = sheety_response.json()
        return data["prices"]

    def sheety_put(self, row, code):
        """this method adds new data to Google spreadsheet"""
        sheety_put_endpoint = f"{sheety_endpoint}/{row}"

        inputs = {
            "price": {
                "iataCode": code,
            }
        }

        sheety_put_response = requests.put(url=sheety_put_endpoint, json=inputs)
        sheety_put_response.raise_for_status()


