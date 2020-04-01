import requests
from requests.exceptions import HTTPError

for url in ['http://www.google.com', 'http://www.twitter.com']:
    try:
        response = requests.get(url)

        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('**************')
        print(f'The request to {url} succeeded with status code: {response.status_code}')
        print(f'The content of the reponse has {len(response.text)} characters')
        print('--------------')