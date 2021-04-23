import requests
import json
import colorama
from colorama import Fore, Back

URL_GET_TOURNAMENT = "https://app.msrvbattle.ru/tournaments/admin?page=1&stateFilter=FINISHED"

URL_DELETE_TOURNAMENT = "https://app.msrvbattle.ru/tournaments/admin/"


def can_and_del():
    Tournaments = requests.get("https://app.msrvbattle.ru/tournaments/admin?page=1&stateFilter=FINISHED", headers=
    {"accept": "*/*", "Authorization": "Plain 39259b70-0be5-48eb-bafe-0d4111ed5c72"})
    json_Tournament = Tournaments.json()
    print(json_Tournament)
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
