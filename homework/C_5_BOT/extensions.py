import json
import requests
from config import exchanges
from config import TOKEN_API

class APIException(Exception):
    pass


class Convertor:
    @staticmethod
    def get_price(base, sym, amount):
        try:
            base_key = exchanges[base]
            sym_key2 = base_key
        except KeyError:
            raise APIException(f"Currency {base} not found!")
        try:
            sym_key = exchanges[sym]
        except KeyError:
            raise APIException(f"Currency {sym} not found!")
        if base_key == sym_key:
            raise APIException(f'Unable to transfer identical currencies {base}!')
        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Failed to process quantity {amount}!')
# if your API plan allows you to convert endpoint -
# convert any amount from one currency to another
# and  using real-time exchange rates
# use the following api setting
        # r = requests.get(f"http://api.exchangeratesapi.io/v1/convert"
        #          f"?access_key=TOKEN_API"
        #          f"&from=base_key"
        #          f"&to=sym_key"
        #          f"&amount=amount_sum")
# if free api
        r = requests.get(f"http://api.exchangeratesapi.io/latest"
                         f"?access_key={TOKEN_API}")
        resp = json.loads(r.content)
        sym = resp['rates'][sym_key]
        base = resp['rates'][sym_key2]
# free api
        new_price = sym / base * amount
        # resp = json.loads(r.content)
        # new_price = resp['rates'][sym_key] * amount  # paid api
        new_price = round(new_price, 3)
        # print(new_price)
        message = f"the price 1 {sym_key2} is {round(sym / base,3)} {sym_key} \n \
the conversion amount is {new_price} {sym_key}"

        return message
