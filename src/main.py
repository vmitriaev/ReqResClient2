from src.constructors import request_constructor, response_json_constructor, error_constructor, response_code_handler

while True:
    basic_url = 'https://reqres.in/api/'
    print('For exit type STOP.' + '\n')
    request_method = input('Type method: ')
    if request_method.lower() in ('stop', 'break', 'exit'):
        break
    elif request_method.lower() == 'get':
        request_url = input('Type url: ' + basic_url)
        if request_url.lower == 'stop':
            break
        else:
            request_params = [request_method, basic_url + request_url, None]
            request_data = request_constructor(request_params[0], request_params[1], request_params[2])
            response_json = response_json_constructor(request_data)
            response_code = response_code_handler(request_data.status_code)
            print(response_code + response_json)
    elif request_method.lower() in ('post', 'put', 'patch'):
        request_url = input('Type url: ' + basic_url)
        if request_url.lower() == 'stop':
            break
        else:
            request_body = input('Your JSON: ')
            request_params = [request_method, basic_url + request_url, request_body]
            request_data = request_constructor(request_params[0], request_params[1], request_params[2])
            response_json = response_json_constructor(request_data)
            response_code = response_code_handler(request_data.status_code)
            print(response_code + response_json)
    elif request_method.lower() == 'delete':
        request_url = input('Type url: ' + basic_url)
        if request_url.lower == 'stop':
            break
        else:
            request_params = [request_method, basic_url + request_url, None]
            request_data = request_constructor(request_params[0], request_params[1], request_params[2])
            response_code = response_code_handler(request_data.status_code)
            print(response_code)
    else:
        print(error_constructor('unknown method ' + request_method.upper()))
