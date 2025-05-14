import time
from imageHandler import ImageHandler
from messageListener import MessageListener
from messageSender import MessageSender
from messageGetter import MessageGetter
from dataHandler import DataHandler
import datetime
import json

#加载配置文件
def loadSettings():
    userList,groupList,userListeners,groupListeners = [],[],[],[]
    settingFileName = "settings.json"
    with open(settingFileName, 'r', encoding='utf-8') as file:
        data = json.load(file)
        userList = data.get("userList")
        groupList = data.get("groupList")

    for userId in userList:
        userListener = MessageListener()
        userListener.setUserId(userId=userId)
        userListeners.append(userListener)

    for groupId in groupList:
        groupListener = MessageListener()
        groupListener.setGroupId(groupId=groupId)
        groupListeners.append(groupListener)

    return userListeners,groupListeners

#检查消息是否触发
def checkMessage(message):
    return message == "🦌" or message == "鹿"

#处理群组消息
def handleGroupMessage(messageListener):
    messageListener.checkGroupMessage()
    newMessageList = messageListener.handelGroupMessage();
    for message in newMessageList:
        if checkMessage(message.get("message")):
            userId = message.get("user_id")
            messageId = message.get("message_id")
            dateTime = datetime.datetime.fromtimestamp(message.get("time"))
            imageHandler = ImageHandler(str(userId)+str(message.get("time"))+".png")
            userName = message.get("user_name")
            imageHandler.month = dateTime.month
            imageHandler.userId = userId    
            imageHandler.userName = userName        
            DataHandler.addRecord(userId, userName, dateTime.month, dateTime.day)
            messageGetter = MessageGetter()
            messageGetter.setMessageReplay(message.get("message_id"))
            messageGetter.addTextMessage("成功🦌了")
            messageGetter.addImageMessage(imageHandler.getImage())
            MessageSender.send_group_msg(messageListener.groupId, messageGetter.getMessage())

#处理个人消息
def hadlePrivateMessage(messageListener):
    messageListener.checkUserMessage()
    newMessageList = messageListener.handelUserMessage();
    for message in newMessageList:
        if (checkMessage(message.get("message"))):
            userId = message.get("user_id")
            messageId = message.get("message_id")
            dateTime = datetime.datetime.fromtimestamp(message.get("time"))
            imageHandler = ImageHandler(str(userId)+str(message.get("time"))+".png")
            userName = message.get("user_name")
            imageHandler.month = dateTime.month
            imageHandler.userId = userId    
            imageHandler.userName = userName        
            DataHandler.addRecord(userId, userName, dateTime.month, dateTime.day)
            messageGetter = MessageGetter()
            messageGetter.setMessageReplay(message.get("message_id"))
            messageGetter.addTextMessage("成功🦌了")
            messageGetter.addImageMessage(imageHandler.getImage())
            MessageSender.send_private_message(message.get("user_id"), messageGetter.getMessage())

if __name__ == "__main__":

    userListeners,groupListeners = loadSettings()
        
    while True:
        try :
                
            if userListeners != []:
                for messageListener in groupListeners:
                    handleGroupMessage(messageListener)
            if groupListeners != []:
                for messageListener in userListeners:
                    hadlePrivateMessage(messageListener)
            time.sleep(2)
        except Exception as e:
            print("Error: ", e)
            time.sleep(2)