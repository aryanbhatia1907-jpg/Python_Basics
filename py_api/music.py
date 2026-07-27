import requests

# Search any song on Spotify data!
artist = input("Enter artist name: ")
response = requests.get(
    f"https://itunes.apple.com/search?term={artist}&limit=5"
)
data = response.json()

for i, song in enumerate(data['results'], 1):
    print(f"{i}. {song['trackName']} — {song['artistName']}")