# https://ipapi.co/

import requests
api_find_url = "https://api.ipify.org/?format=json"
res = requests.get(api_find_url)
if res.status_code == 200:
    data = res.json()
    ip = data.get('ip')


ip_locaiton_url = f'https://ipapi.co/{ip}/json/'
r = requests.get(ip_locaiton_url)
if r.status_code == 200:
    ip_details = r.json()
    city = ip_details.get('city')
    region = ip_details.get('region')
    country = ip_details.get('country_name')

sentence = f'Ip ({ip}) is located in {city} {region}, {country}.'
print(sentence)