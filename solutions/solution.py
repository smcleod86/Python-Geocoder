import geocoder
import requests

# declare destinations list
destinations = ['Space Needle',
  'Crater Lake',
  'Golden Gate Bridge',
  'Yosemite National Park',
  'Las Vegas, Nevada',
  'Grand Canyon National Park',
  'Aspen, Colorado',
  'Mount Rushmore',
  'Yellowstone National Park',
  'Sandpoint, Idaho',
  'Banff National Park',
  'Capilano Suspension Bridge']

def geocode(list):
  API_BASE_URL = "https://api.darksky.net/forecast/c73c375afbedccd447f98b4e275bb84c/37.8267,-122.4233"

  for city in list:
  point = geocoder.arcgis(city)
  point.json

  full_api_url = API_BASE_URL + {g.lat} + "," + {g.lng}
  result = requests.request('GET', full_api_url).json()


  print(f'the {city} is located at latitude: {point.lat} & longitude: {point.lng}')
  print(f'At the {city} right now, it\'s: {result.summary} with a current temperature of {result.temperature}')

geocode(destinations) 