import requests
import os

API_KEY = os.getenv("API_KEY")
API_URL = "https://api.example.com/data"

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

response = requests.get(API_URL, headers=headers)

print("API Status:", response.status_code)