import requests
import json


GET_NEWS = "https://feed-internal.dev.arenum.games/api/v1/internal/feed/news?start=0&max=1000"
DELETE_NEWS = "https://feed-internal.dev.arenum.games/api/v1/internal/feed/news/"

Get_news = requests.get(GET_NEWS, headers={"accept": "*/*", "Content-Type": "application/json", "Authorization": "Plain 39259b70-0be5-48eb-bafe-0d4111ed5c72"})
print(Get_news.json())
for i in range(1, 830):
    delete = requests.delete(DELETE_NEWS+str(i), headers={"application": "*/*", "Content-Type": "application/json", "Authorization": "Plain 39259b70-0be5-48eb-bafe-0d4111ed5c72"})
