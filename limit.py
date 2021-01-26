# https://api.exchangeratesapi.io/history?start_at=2018-01-01&end_at=2018-09-01

import requests
start_at = '2018-01-01'
end_at = '2018-09-01'

url = f'https://api.exchangeratesapi.io/history?start_at={start_at}&end_at={end_at}'

response = requests.get(url)

if response.status_code == 200:    
    limit = response.json()
    f = open('exchange/limit.json', 'w')    
    f.write(str(limit))        
    f.close        
elif response.status_code == 404:
    print('Not found')



