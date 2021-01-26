# https://api.exchangeratesapi.io/history?start_at=2018-01-01&end_at=2018-09-01&base=USD

import requests
start_at = '2018-01-01'
end_at = '2018-09-01'
base = 'JPY'

url = f'https://api.exchangeratesapi.io/history?start_at={start_at}&end_at={end_at}&base={base}'

response = requests.get(url)

if response.status_code == 200:    
    historical_rates = response.json()
    f = open('exchange/historical_rates.json', 'w')        
    f.write(str(historical_rates))        
    f.close
    
elif response.status_code == 404:
    print('Not found')



