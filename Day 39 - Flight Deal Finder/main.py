# from pprint import pprint
import data_manager
import flight_search
import notification_manager

# this hard coded data was used in development to prevent going over the sheety monthly call limit

# HARD_DATA = [
#     {"city": "Paris", "iataCode": "PAR", "lowestPrice": 54, "id": 2},
#     {"city": "Berlin", "iataCode": "BER", "lowestPrice": 42, "id": 3},
#     {"city": "Tokyo", "iataCode": "TYO", "lowestPrice": 485, "id": 4},
#     {"city": "Sydney", "iataCode": "SYD", "lowestPrice": 551, "id": 5},
#     {"city": "Istanbul", "iataCode": "IST", "lowestPrice": 95, "id": 6},
#     {"city": "Kuala Lumpur", "iataCode": "KUL", "lowestPrice": 414, "id": 7},
#     {"city": "New York", "iataCode": "NYC", "lowestPrice": 240, "id": 8},
#     {"city": "San Francisco", "iataCode": "SFO", "lowestPrice": 260, "id": 9},
#     {"city": "Cape Town", "iataCode": "CPT", "lowestPrice": 378, "id": 10},
# ]

sheety_data_manager = data_manager.DataManager()
tequila = flight_search.FlightSearch()
notification = notification_manager.NotificationManager()

#sheet_data = HARD_DATA
sheet_data = sheety_data_manager.sheety_get()

# the following loop determines if spreadsheet has city iata codes present and provides one if not
for city in sheet_data:
    if city["iataCode"] == "":
        city["iataCode"] = tequila.code_search(city["city"])
        sheety_data_manager.sheety_put(city["id"], city["iataCode"])

# this creates a list of city iata codes for use in the price search functionality
city_list = {item["iataCode"]: item["lowestPrice"] for item in sheet_data}

for iata in city_list.keys():
    try:
        price_data = tequila.price_search(iata)
    except IndexError:
        print(f"There are no flights to {iata} during this time frame.")
    else:
        if price_data["price"] > city_list[iata]:
            print("No Deals")
        else:
            notification.send_notification(
                price_data["price"],
                price_data["cityFrom"],
                price_data["route"][0]["flyFrom"],
                price_data["cityTo"],
                price_data["route"][0]["flyTo"],
                price_data["route"][0]["local_departure"].split("T", 1)[0],
                price_data["route"][1]["local_arrival"].split("T", 1)[0]
            )
