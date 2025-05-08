class MessageGetter:
    def __init__(self):
        self.message = []

    def addTextMessage(self, message):
        self.message.append({
            "type": "text", 
            "data": {
                "text": message
            }
        })
    
    def addImageMessage(self, imageData):
        self.message.append({
            "type": "image", 
            "data": {
                "file": imageData
            }
        })
    
    def setMessageReplay(self, messageId):
        self.message.insert(0, {
            "type": "reply", 
            "data": {
                "id": messageId
            }
        })

    def getMessage(self):
        return self.message.copy()
    

    