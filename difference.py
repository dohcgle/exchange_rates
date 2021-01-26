# https://api.exchangeratesapi.io/2010-01-12'

import requests
url_1999 = f'https://api.exchangeratesapi.io/2010-01-12'


response_1999 = requests.get(url_1999)

if response_1999.status_code == 200:
    response_json = response_1999.json()
    rub_1999 = response_json['rates']['RUB']

    url_latest = f'https://api.exchangeratesapi.io/latest'
    response_latest = requests.get(url_latest).json()
    rub_latest = response_latest['rates']['RUB']

    def_rub = rub_latest - rub_1999

    f = open('exchange/data_difference.json', 'a')
    f.write(str(def_rub))
    f.write('\n')
    f.close    
elif response_1999.status_code == 404:
    print('Not Found.')

print(def_rub)