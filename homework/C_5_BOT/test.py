import json
import requests
from config import TOKEN_API


exchanges = {
'U.S.dollar': 'USD',
    'Euro': 'EUR',
'Chinese_yuan': 'CNY'
}

base_key = "USD"
sym_key = "RUB"
sym_key2 = base_key
amount = 11

r = requests.get(f"http://api.exchangeratesapi.io/latest"
                 f"?access_key=5d3e03177c6d424d17f58f27362a845d&format")
resp = json.loads(r.content)
sym = resp['rates'][sym_key]
base = resp['rates'][sym_key2]
print(sym, sym_key)
print(base, sym_key2)
new_price = sym/base * amount
print(new_price)
#print(TOKEN_API)
print(resp)
                #f"http://api.exchangeratesapi.io/latest"
                 #f"?access_key=5d3e03177c6d424d17f58f27362a845d&format=1"
                 #f"base={base_key}"
                 #f"&symbols={sym_key}"

                #f"http://api.exchangeratesapi.io/v1/convert"
                 #f"?access_key=TOKEN_API"
                 #f"&from=base_key"
                 #f"&to=sym_key"
                 #f"&amount=amount_sum"