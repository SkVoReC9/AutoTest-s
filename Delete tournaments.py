import requests
import json
from colorama import Fore, Back

URL_GET_TOURNAMENT = "https://app.msrvbattle.ru/tournaments/admin?page=1&stateFilter=FINISHED"

URL_DELETE_TOURNAMENT = "https://app.msrvbattle.ru/tournaments/admin/"


def can_and_del():
    log_and_pass = {"login": "Boomer_23", "password": "rein2612"}
    get_token = requests.post("https://app.msrvbattle.ru/auth/signinForm", headers=
    {"application": "*/*", "Content-Type": "application/json"}, data=json.dumps(log_and_pass))
    token = get_token.headers['authorization']
    tournaments = requests.get(URL_GET_TOURNAMENT, headers=
    {"accept": "*/*", "Authorization": str(token)})
    json_Tournament = tournaments.json()
    for j in json_Tournament["items"]:
        g = j["code"]
        print(g)
        data = {"reason": "организатором"}
        cancel = requests.put("https://app.msrvbattle.ru/tournaments/admin/" + g + "/cancel", headers=
        {"accept": "*/*", "Authorization": "Plain cd6b1605-e996-455e-94cc-176e6c434062",
         "Content-Type": "application/json"}, data=json.dumps(data))
        if cancel.status_code == 200:
            delete = requests.delete(URL_DELETE_TOURNAMENT + g, headers=
            {"accept": "*/*", "Authorization": "Plain cd6b1605-e996-455e-94cc-176e6c434062",
             "Content-Type": "application/json"})
            if delete.status_code == 200:
                print(Fore("Success Cancel and Delete tournament:", "Green"), g)


if __name__ == "__main__":
    index = 1
    for i in range(1, 9):
        can_and_del()
        index += 1
