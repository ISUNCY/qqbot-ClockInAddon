import requests
import json
class MessageSender:

    def send_private_message(user_id, message): 
        data = {
            "user_id": user_id,
            "message": message
        }
        json_data = json.dumps(data)
        requests.post("http://127.0.0.1:3000/send_private_msg", data=json_data, headers={"authorization": "isuncy"})


    def send_group_msg(group_id, message) :
        data = {
            "group_id": group_id,
            "message": message
        }
        json_data = json.dumps(data)
        requests.post("http://127.0.0.1:3000/send_group_msg", data=json_data, headers={"authorization": "isuncy"})
    
