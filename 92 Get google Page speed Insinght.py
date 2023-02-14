#--- Google page insist api uses------------

import requests
test_url = input("Enter url: ")
api_key = "AIzaSyChiuq6m379pWJ6hYXIq7wvQ1gPPtDe24w"
api_url = f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={test_url}&key={api_key}'

res = requests.get(api_url)
if res.status_code == 200:
    print(res.json())
else:
    print('Something Worng')