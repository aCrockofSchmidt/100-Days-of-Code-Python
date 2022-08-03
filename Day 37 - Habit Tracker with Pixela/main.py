import requests
from datetime import datetime as dt

USERNAME = "acrockofschmidt"
TOKEN = "hjyu487UK331br58"
GRAPH = "graph12"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# successfully created an account - therefore commented out so as not to run again
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph12",
    "name": "Cycling Graph",
    "unit": "KM",
    "type": "float",
    "color": "momiji",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# successfully created base graph - therefore commented out so as not to run again
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

data_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}"

today = dt.now()
print(today.strftime("%Y%m%d"))

data_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "15.5",
}

# response = requests.post(url=data_endpoint, json=data_config, headers=headers)
# print(response.text)

# update/change already submitted data

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/{today.strftime('%Y%m%d')}"

update_config = {
    "quantity": "7.75"
}

# response = requests.put(url=update_endpoint, json=update_config, headers=headers)
# print(response.text)

# delete pixel

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/20220801"

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)
