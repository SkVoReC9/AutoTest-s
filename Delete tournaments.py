import requests
import json
from threading import Thread

URL_GET_TOURNAMENT = "https://app.msrvbattle.ru/tournaments/admin?page=1&stateFilter=FINISHED"

URL_DELETE_TOURNAMET = "https://app.msrvbattle.ru/tournaments/admin/"

def can_and_del(index):
    Tournaments = requests.get("https://app.msrvbattle.ru/tournaments/admin?page=1&stateFilter=FINISHED", headers=
        {"accept": "*/*", "Authorization": "Plain cd6b1605-e996-455e-94cc-176e6c434062"})
    json_Tournament = Tournaments.json()
    for j in json_Tournament["items"]:
        g = j["code"]
        print(g)
        data = {"reason": "организатором"}
        cancel = requests.put("https://app.msrvbattle.ru/tournaments/admin/"+g+"/cancel", headers=
        {"accept": "*/*", "Authorization": "Plain cd6b1605-e996-455e-94cc-176e6c434062", "Content-Type": "application/json"}, data=json.dumps(data))
        if cancel.status_code == 200:
            delete = requests.delete(URL_DELETE_TOURNAMET+g, headers=
            {"accept": "*/*", "Authorization": "Plain cd6b1605-e996-455e-94cc-176e6c434062", "Content-Type": "application/json"})
            if delete.status_code == 200:
                print("Success Cancel and Delete tournament: {}", g)


if __name__==  "__main__":
    index = 1
    for i in range(1, 9):
        can_and_del(index)
        index += 1
