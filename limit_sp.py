# https://api.exchangeratesapi.io/history?start_at=2018-01-01&end_at=2018-09-01&symbols=ILS,JPY

import requests
start_at = '2018-01-01'
end_at = '2018-09-01'
symbols = 'ILS,JPY'

url = f'https://api.exchangeratesapi.io/history?start_at={start_at}&end_at={end_at}&symbols={symbols}'

response = requests.get(url)

if response.status_code == 200:    
    limit_sp = response.json()
    f = open('exchange/limit_sp.json', 'a')        
    f.write(str(limit_sp))        
    f.close
    
elif response.status_code == 404:
    print('Not found')



