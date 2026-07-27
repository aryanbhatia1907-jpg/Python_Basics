import requests

# Get real weather for Delhi RIGHT NOW
response = requests.get(
    "https://wttr.in/Delhi?format=3"        # Only change place to see real time weather
)
print(response.text)
# Output: Delhi: ⛅️  +32°C

# ↑ .text = read the response as plain text
# ↑ .json() = read it as a dictionary (when server sends data)