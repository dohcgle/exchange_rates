# https://api.exchangeratesapi.io/latest?symbols=USD,ZAR

import requests
symbols = 'USD,ZAR'
url = f'https://api.exchangeratesapi.io/latest?symbols={symbols}'

response = requests.get(url)

if response.status_code == 200:
    response_json = response.json()
    sp = response_json['rates']       
    f = open('exchange/specific_exchange.json', 'w') 
    f.write(str(sp))    
    f.close
elif response.status_code == 404:
    print('Not found')

