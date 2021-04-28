import requests
import json
from colorama import Fore, Style

GET_TOURNAMENT_URL = "https://app.msrvbattle.ru/tournaments/admin?page=1&stateFilter=NOT_FINISHED"
PATH_TO_USERS = "C:/Users/Александр/Desktop/Работа/AutoTest-s/700user.txt"

log_and_pass = {"login": "Boomer_23", "password": "rein2612"}
Get_Token = requests.post("https://app.msrvbattle.ru/auth/signinForm",
                          headers={"application": "*/*", "Content-Type": "application/json"},
                          data=json.dumps(log_and_pass))
Token = Get_Token.headers['authorization']
Get_tour = requests.get(GET_TOURNAMENT_URL, headers={"application": "*/*", "Content-Type": "application/json",
                                                     "Authorization": str(Token)})
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
    parts_bots = requests.post("https://app.msrvbattle.ru/tournaments/admin/" + codes + "/bots/participate",
                               headers={"application": "*/*", "Content-Type": "application/json",
                                        "Authorization": "Plain 0c69c4b2-2f67-4557-b502-67217d511571"},
                               data=json.dumps(data))
    if parts_bots.status_code == 200:
        print("Success reg bots to ", codes)
        j = j + 1 + 29
        l = l + 3 + 29
    else:
        print(Fore.RED + "Error reg bots to " + codes, Fore.MAGENTA + "Error Code", parts_bots.status_code,
              "Text Error", parts_bots.text)
        print(Style.RESET_ALL)
