import requests, json

with open('config.json') as config_file:
    conf = json.load(config_file)

services_list = conf['services']

default_url = conf['default_url']

a = input('К какому сервису запрос?' + '\n' + str(services_list) + '\n')

e = default_url + '/' + a.lower()

print(e)
