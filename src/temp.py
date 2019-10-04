import requests, json

default_url = 'https://reqres.in/api/'

mass = ['get', 'https://reqres.in/api/users/2', None]


def request_constructor(method, endpoint, body):
    if method == 'get':
        request = requests.get(url=endpoint, data=body)
        return request
    elif method == 'post':
        request = requests.post(url=endpoint, data=body)
        return request
    elif method == 'put':
        request = requests.put(url=endpoint, data=body)
        return request
    elif method == 'patch':
        request = requests.patch(url=endpoint, data=body)
        return request
    elif method == 'delete':
        request = requests.delete(url=endpoint, data=body)
        return request
    else:
        return 'wrong method'


request_data = request_constructor(mass[0], mass[1], mass[2])

response_data = json.dumps(request_data.json(), sort_keys=True, indent=2)

print(response_data)
