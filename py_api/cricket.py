import requests

response=requests.get("https://cricapi.com/api/cricket?apikey=YOUR_KEY")

print(response.text)