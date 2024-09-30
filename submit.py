import requests
import cgi, cgitb

form = cgi.FieldStorage()

firstname = form.getvalue('first_name')
lastname = form.getvalue('last_ name')
email = form.getvalue('email')

if not firstname or not lastname or not email:
    print("Invalid!")
else:
    # The API endpoint
    url = "https://mc7g45ywnh12hpdrs99bq57llz91.auth.marketingcloudapis.com/v2/token"

    # Data to be sent
    data = {
        "grant_type": "client_credentials",
        "client_id": "et5iefljur0vxnuirhv7ou7n",
        "client_secret": "eVX9BFxgjABMVVqafq2Kk4sV",
        "account_id": "514012664"
    }

    # A POST request to the API
    response = requests.post(url, json=data)

    # Print the response

    print(response.json()['access_token'])

    access_token = response.json()['access_token']

    endpoint = 'https://mc7g45ywnh12hpdrs99bq57llz91.rest.marketingcloudapis.com/data/v1/async/dataextensions/key:8D4BF5FD-081B-41A6-AFAE-19E576536431/rows'

    data = {
      "items": [
        {
          "firstname": f"{firstname}",
          "lastname": f"{lastname}",
          "email": f"{email}"
        }
      ]
    }

    headers = { 'Authorization':f'Bearer {access_token}',
              'Content-Type':'application/json'
    }

    response = requests.post(endpoint,headers=headers,json=data)
    print(response.json())
