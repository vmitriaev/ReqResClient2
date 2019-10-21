import requests

url = 'https://reqres.in/api/user/2'
params = {
    'MS_WHC': {
        'CgPN': '79152268007',
        'CdPN': '79299016973',
        'Type': 0
    }
}

response = requests.get(url, json=params)
print(response.status_code, response.text)
