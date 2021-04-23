import requests
import json

GET_TOURNAMENT_URL = "https://app.msrvbattle.ru/tournaments/admin?page=1&stateFilter=NOT_FINISHED"
PATH_TO_USERS = "C:/Users/Александр/Desktop/Работа/AutoTest-s/700user.txt"

Get_tour = requests.get(GET_TOURNAMENT_URL, headers={"application": "*/*", "Content-Type": "application/json",
                                                     "Authorization": "Plain 0c69c4b2-2f67-4557-b502-67217d511571"})
# print(Get_tour.json())

with open(PATH_TO_USERS) as users_file:
    users = users_file.read().splitlines()
print(users)

json_tournaments = Get_tour.json()

j = 0
l = 29
for i in json_tournaments["items"]:
    codes = i["code"]
    print(codes)
    data = users[j:l]
    print(data)
    parts_bots = requests.post("https://app.msrvbattle.ru/tournaments/admin/"+codes+"/bots/participate",
                               headers={"application": "*/*", "Content-Type": "application/json",
                                                            "Authorization": "Plain 0c69c4b2-2f67-4557-b502-67217d511571"},
                               data=json.dumps(data))
    if parts_bots.status_code == 200:
        print("Success reg bots to ", codes)
        j = j+1+29
        l = l+3+29
    else:
        print("Error reg bots to", codes, "Error Code", parts_bots.status_code, "Text Error", parts_bots.text)
