import requests, json


def error_constructor(message):
    '''Вывод сообщения об ошибке'''
    errorMessage = ('ERROR: ' + message)
    lines = '-' * len(errorMessage)
    return '\n' + lines + '\n' + errorMessage + '\n' + lines + '\n'


def request_constructor(method, endpoint, body):
    if method == 'get':
        request = requests.get(url=endpoint)
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
        request = requests.delete(url=endpoint)
        return request
    else:
        return error_constructor('UNKNOWN METHOD')


def response_json_constructor(request_data):
    response_data = json.dumps(request_data.json(), sort_keys=True, indent=2)
    return 'Response:\n' + response_data


def response_code_handler(response_code):
    if response_code == 200:
        return '\nStatus: OK\nCode: 200\n'
    elif response_code == 201:
        return '\nStatus: CREATED\nCode: 201\n'
    elif response_code == 204:
        return '\nStatus: DELETED\nCode: 204\nResponse: NO CONTENT\n'
    elif response_code == 400:
        return '\nStatus: BAD REQUEST\nCode: 400\n'
    elif response_code == 404:
        return '\nStatus: NOT FOUND\nCode: 404\n'
    else:
        return error_constructor('unknown status code: ' + str(response_code))
