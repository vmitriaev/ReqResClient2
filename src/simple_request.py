import requests, json


def send_post_request():
    url = 'https://reqres.in/api/users'
    params = {
        "name": "morpheus",
        "job": "leader"
    }
    post_response_data = requests.post(url, json=params)
    response_status_code = post_response_data.status_code
    response_body = json.dumps(post_response_data.json(), sort_keys=True, indent=2)
    return ('Status: ' + str(response_status_code) + '\n' + response_body)


print(send_post_request())
