import requests

url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"

try:
    response = requests.get(url)
    response.raise_for_status()  # Check if the request was successful
    print(response.json())  # Print the JSON content of the response
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
      