#--- https://pypi.org/project/requests/
#--- pip install requests

# We can install from our CMD section
# Also we can install from Terminal 
# Also we can install form Extensions


import requests
res = requests.get('https://jsonplaceholder.typicode.com/posts')
# print(res.status_code)
print(res.json())

 