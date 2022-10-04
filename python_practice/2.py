import requests
import json

url = 'https://reqres.in/api/products/3'

res = requests.get(url).json()



print(res['data'])