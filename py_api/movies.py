import requests

api_key = "c7f6cf5b"
movie = input("Enter movie name: ")

url = f"https://www.omdbapi.com/?t={movie}&apikey={api_key}"
response = requests.get(url)
data = response.json()                  # .JSON used to convert data comes in string format from API to dict ,then we can access data like below
print(f"Title: {data['Title']}")
print(f"Year: {data['Year']}")
print(f"Rating: {data['imdbRating']}")
print(f"Plot: {data['Plot']}")
print(f"Cast: {data['Actors']}")
