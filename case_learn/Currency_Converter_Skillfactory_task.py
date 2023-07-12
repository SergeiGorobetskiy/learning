# API all currency https://openexchangerates.org/account/app-ids
import requests

r = requests.get('https://openexchangerates.org/api/latest.json?app_id=19fcedb50cd34bf6944efacd266e5135&base=USD&callback=someCallbackFunction')
#https://openexchangerates.org/api/latest.json?app_id=19fcedb50cd34bf6944efacd266e5135&base=USD&callback=AED
print (r.content)