import requests

# Without API key
CITY = "Delhi"
url = f"https://wttr.in/{CITY}?format=%C+%t"

response = requests.get(url)

if response.status_code == 200:
    print(f"Weather in {CITY}: {response.text.strip()}")
else:
    print("Error fetching weather data")

#With Api key requirment

# import requests
#
# API_KEY = "your_openweathermap_api_key"
# CITY = "Delhi"
#
# url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
#
# response = requests.get(url)
# data = response.json()
#
# print(f"Weather in {CITY}: {data['main']['temp']}°C, {data['weather'][0]['description']}")
