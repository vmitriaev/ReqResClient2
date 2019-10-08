from src.constructors import request_constructor, response_json_constructor, error_constructor

request_params = ['get', 'https://reqres.in/api/users', None]

print(response_json_constructor(request_constructor(request_params[0], request_params[1], request_params[2])))