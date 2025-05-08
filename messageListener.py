import requests
from dataHandler import DataHandler

class MessageListener:
    def __init__(self):
        self.userId = ""
        self.groupId = ""
        self.userMessageInfoQueue = []
        self.groupMessageInfoQueue = []
        self.listenMaxCount = 10

    def setUserId(self, userId):
        if userId != self.userId:
            self.userMessageInfoQueue.clear()
        self.userId = userId

    def setGroupId(self, groupId):
        if groupId != self.groupId:
            self.groupMessageInfoQueue.clear()
        self.groupId = groupId
    def checkUserMessage(self):
        data = {
            "user_id": self.userId,
            "message_seq": "",
            "count": self.listenMaxCount,
            "reverseOrder": "false"
        }
        data = requests.post("http://127.0.0.1:3000/get_friend_msg_history", data=data, headers={"authorization": "isuncy"})
        data = data.json()
        messageList = data.get("data").get("messages")
        for message in messageList:
            messageId = message.get("message_id")
            userId = str(message.get("user_id"))
            if not DataHandler.findMessageId(messageId) and userId == self.userId:
                DataHandler.addMessageId(messageId)
                print("New message from user:", message.get("raw_message"))
                self.userMessageInfoQueue.append({
                    "message_id": messageId,
                    "user_id": message.get("user_id"),
                    "message": message.get("raw_message"),
                    "time": message.get("time"),
                    "user_name": message.get("sender").get("nickname")
                })

    #返回消息列表并清空缓存
    def handelUserMessage(self) :
        self.checkUserMessage()
        messages = self.userMessageInfoQueue.copy()
        self.userMessageInfoQueue.clear()
        return messages
    
    def checkGroupMessage(self):
        data = {
            "group_id": self.groupId,
            "message_seq": "",
            "count": self.listenMaxCount,
            "reverseOrder": "false"
        }
        data = requests.post("http://127.0.0.1:3000/get_group_msg_history", data=data, headers={"authorization": "isuncy"})
        data = data.json()
        messageList = data.get("data").get("messages")
        for message in messageList:
            messageId = message.get("message_id")
            if not DataHandler.findMessageId(messageId):
                DataHandler.addMessageId(messageId)
                print("New message from user "+message.get("sender").get("nickname")+":", message.get("raw_message"))
                self.groupMessageInfoQueue.append({
                    "message_id": messageId,
                    "user_id": message.get("user_id"),
                    "message": message.get("raw_message"),
                    "time": message.get("time"),
                    "user_name": message.get("sender").get("nickname")
                })

    def handelGroupMessage(self) :
        self.checkGroupMessage()
        messages = self.groupMessageInfoQueue.copy()
        self.groupMessageInfoQueue.clear()
        return messages
