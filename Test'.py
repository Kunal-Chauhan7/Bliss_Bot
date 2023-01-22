import json

import requests
category = 'happiness'
api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
response = requests.get(api_url, headers={'X-Api-Key': 'KlbRiHTjlcttpUxd9rufUQ==EVLlxjMxJjNfFYdW'})
if response.status_code == requests.codes.ok:
    result = json.loads(response.text)
    print(result[0])
else:
    print("Error:", response.status_code, response.text)