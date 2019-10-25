import requests, json

url = 'https://reqres.in/api/users'

name = input('enter name: ')
job = input('enter job: ')

params = {
    "name": name,
    "job": job
}

response = requests.post(url, json=params)

print(response.request)

print('\nStatus: ' + str(response.status_code))

print(json.dumps(response.json(), sort_keys=True, indent=2))
