# https://api.exchangeratesapi.io/history?start_at=2018-01-01&end_at=2018-09-01

import requests
start = '2019-02-01'
end = '2020-11-01'
url = f'https://api.exchangeratesapi.io/history?start_at={start}&end_at={end}'

response = requests.get(url)

if response.status_code == 200:
    response_json = response.json()    
    f = open('exchange/period.json', 'w')  
    f.write(str(response_json))   
    f.close
elif response.status_code == 404:
    print('Not found')



