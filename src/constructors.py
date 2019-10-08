import requests, json


def error_constructor(message):
    '''Вывод сообщения об ошибке'''
    errorMessage = ('ERROR: ' + message)
    lines = '-' * len(errorMessage)
    return '\n' + lines + '\n' + errorMessage + '\n' + lines + '\n'


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
        return error_constructor('WRONG METHOD')


def response_json_constructor(request_data):
    response_data = json.dumps(request_data.json(), sort_keys=True, indent=2)
    return response_data
