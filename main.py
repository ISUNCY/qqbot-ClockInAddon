import time
from imageHandler import ImageHandler
from messageListener import MessageListener
from messageSender import MessageSender
from messageGetter import MessageGetter
from dataHandler import DataHandler
import datetime

# messageListener = MessageListener()
# messageListener.setUserId("1907435186")

# while True:
#     messageListener.checkUserMessage()
#     newMessageList = messageListener.handelUserMessage();
#     for message in newMessageList:
#         if (message.get("message") == "🦌"):
#             userId = message.get("user_id")
#             messageId = message.get("message_id")
#             dateTime = datetime.datetime.fromtimestamp(message.get("time"))
#             imageHandler = ImageHandler(str(userId)+str(message.get("time"))+".png")
#             userName = message.get("user_name")
#             imageHandler.month = dateTime.month
#             imageHandler.userId = userId    
#             imageHandler.userName = userName        
#             DataHandler.addRecord(userId, userName, dateTime.month, dateTime.day)
#             messageGetter = MessageGetter()
#             messageGetter.setMessageReplay(message.get("message_id"))
#             messageGetter.addTextMessage("成功🦌了")
#             messageGetter.addImageMessage(imageHandler.getImage())
#             MessageSender.send_private_message(message.get("user_id"), messageGetter.getMessage())

#     time.sleep(3)

messageListener = MessageListener()
messageListener.setGroupId("850723286")

while True:
    messageListener.checkGroupMessage()
    newMessageList = messageListener.handelGroupMessage();
    for message in newMessageList:
        if message.get("message") == "🦌" or message.get("message") == "鹿":
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
            MessageSender.send_group_msg("850723286", messageGetter.getMessage())

    time.sleep(3)