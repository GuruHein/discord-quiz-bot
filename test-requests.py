import requests
import json

response = requests.get("http://127.0.0.1:8000/questions/random")
data = response.json()
print(data['answers'])

# print(response.headers)