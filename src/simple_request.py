import requests

url = 'https://reqres.in/api/users'
params = {
    "name": "morpheus",
    "job": "leader"
}

response = requests.post(url, json=params)

print(response.status_code, response.text)
