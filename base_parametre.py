# https://api.exchangeratesapi.io/latest?base=USD

import requests
currency = 'PHP'
url = f'https://api.exchangeratesapi.io/latest?base={currency}'
response = requests.get(url)

if response.status_code == 200:
    response_json = response.json()
        
    # print(bp)
    f = open('exchange/base_parametre.json', 'w')
    f.write(str(response_json))
    f.write('\n')
    f.close

elif response.status_code == 404:
    print('Not found')