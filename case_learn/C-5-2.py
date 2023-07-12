# попробуем получить данные с API

import requests
# запрос на сервер по адресу
print('\u001b[33m', 'статус полученного ответа')
r = requests.get('https://baconipsum.com/api/?type=all-meat&paras=3&start-with-lorem=1&format=html')
# статус полученного ответа

print ('\u001b[38m',r.status_code)

print('\u001b[33m','json-ответ')
r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')
# попробуем поймать json-ответ

print('\u001b[38m',r.content)

# поменяем наш код и превратим данный текст в список,

import json
print('\u001b[33m','из ответа делаем список')
r = requests.get('https://api.github.com')

print('\u001b[38m',r.content)

# делаем его словарём.
print('\u001b[33m','из ответа делаем словарь')
r = requests.get('https://api.github.com')

d = json.loads(r.content)
# делаем из полученных байтов Python-объект для удобной работы

print('\u001b[38m',type(d))
# обращаемся к полученному объекту
# как к словарю и попробуем напечатать одно из его значений
print('\u001b[38m',d['following_url'])

# пробуем отправить POST-запрос
print('\u001b[33m','POST-запрос')
r = requests.post('https://httpbin.org/post', data = {'key':'value'})
# отправляем пост-запрос
# содержимое ответа и его обработка происходит так же,
# как и с ГЕТ-запросами, разницы нет
print('\u001b[38m', r.content)