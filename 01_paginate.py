import requests

client_id = 'a1b2c3d4e5f6g7h8i9j0'

api_key = 'a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6'

session = requests.session()

session.auth = (client_id, api_key)

url = 'https://api.amp.cisco.com/v1/computers'

response = session.get(url)

response_json = response.json()

for computer in response_json['data']:
    print(computer['connector_guid'], computer['hostname'])

while 'next' in response_json['metadata']['links']:
    next_url = response_json['metadata']['links']['next']
    response = session.get(next_url)
    response_json = response.json()
    for computer in response_json['data']:
        print(computer['connector_guid'], computer['hostname'])
