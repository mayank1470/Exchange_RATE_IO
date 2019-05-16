import urllib
import json
api_base='https://api.exchangeratesapi.io/'
get_latest='latest'
base_code=input('Enter the Base Currency Code: ')
#get_old=input('Enter the date in YYYY-DD-MM format')
response=urllib.request.urlopen(api_base+get_latest+'?base='+base_code).read()
data=json.loads(response)
# print(data)
base_currency=data.get('base')
print('Base currency set to: ',base_currency)
exchange_rates_base=data.get('rates')
# print(exchange_rates_base)
remitter_currency=input('Enter Remitter currency code: ')
try:
  remit_exchange_rate=exchange_rates_base.get(remitter_currency) 
except:
  print('Remitter Currency not supported')
quantity=float(input('Enter the amount to convert: '))
amount=str(remit_exchange_rate*quantity)
print('Converted amount: ',remitter_currency+amount)
print('Current Exchange Rate is: ',remit_exchange_rate)
