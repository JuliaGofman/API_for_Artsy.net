'''
В этой задаче необходимо воспользоваться API сайта artsy.net

API проекта Artsy предоставляет информацию о некоторых деятелях искусства,
их работах, выставках.

В рамках данной задачи вам понадобятся сведения о деятелях искусства.

Вам даны идентификаторы художников в базе Artsy.
Для каждого идентификатора получите информацию о имени художника и годе рождения.
Выведите имена художников в порядке неубывания года рождения. В случае если у художников
одинаковый год рождения, выведите их имена в лексикографическом порядке.

В большинстве случаев, для получения доступа к API необходимо зарегистрироваться в проекте,
создать свое приложение, и получить уникальный ключ (или токен), и в дальнейшем все запросы
к API осуществляются при помощи этого ключа.

Чтобы начать работу с API проекта Artsy, вам необходимо пройти на стартовую страницу
документации к API https://developers.artsy.net/start и выполнить необходимые шаги, а именно
зарегистрироваться, создать приложение, и получить пару идентификаторов Client Id и
Client Secret.

После этого необходимо получить токен доступа к API.
'''

import requests
import json

client_id = '8a87071933a1056713f3'
client_secret = '8bd8ae1aebcb93977256ec6a2a80d13d'

for_token = requests.post('https://api.artsy.net/api/tokens/xapp_token',
                      data={'client_id': client_id, 'client_secret': client_secret})

token_text = json.loads(for_token.text)

token = token_text['token']

headers = {'X-Xapp-Token': token}

list_answer = {}

with open ('dataset_24476_4.txt') as f:
    for i in f:
        id_artist = i.strip()

        api_url = 'https://api.artsy.net/api/artists/'+id_artist
        res = requests.get(api_url, headers=headers)
        res.encoding = 'utf-8'

        answer = res.json()

        list_answer[answer['birthday']] = answer['sortable_name']

with open ('text1.txt', 'w', encoding='utf-8') as f1:
    for k, v in sorted(list_answer.items()):
        f1.write("{}\n".format(v))  
    
    
    
    
    
    
    
    
    