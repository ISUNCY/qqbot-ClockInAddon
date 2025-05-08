import sqlite3

class DataHandler :
    
    @staticmethod
    def addRecord(userId, userName, month, day):
        conn = sqlite3.connect("ClockInRecord.db")
        cursor = conn.cursor()
        #查找是否已经存在当天记录
        cursor.execute("SELECT * FROM clock_in WHERE user_id = ? AND month = ? AND day = ?", (userId, month, day))
        result = cursor.fetchone()
        if result:
            # 如果存在，更新记录
            cursor.execute("UPDATE clock_in SET count = count + 1 WHERE user_id = ? AND month = ? AND day = ?", (userId, month, day))
        else:
            # 如果不存在，插入新记录
            cursor.execute("INSERT INTO clock_in (user_id, user_name, month, day, count) VALUES (?, ?, ?, ?, ?)", (userId, userName, month, day, 1))
        conn.commit()
        conn.close()

    @staticmethod
    def getCount(userId, month, day):
        conn = sqlite3.connect("ClockInRecord.db")
        cursor = conn.cursor()
        cursor.execute("SELECT count FROM clock_in WHERE user_id = ? AND month = ? AND day = ?", (userId, month, day))
        result = cursor.fetchone()
        conn.close()
        if result is None:
            return 0
        return result
    
    @staticmethod
    def findMessageId(messageId):
        conn = sqlite3.connect("ClockInRecord.db")
        cursor = conn.cursor()
        cursor.execute("select * from message where message_id = ?", (messageId,))
        result = cursor.fetchone()
        conn.close()
        if result is not None:
            return True
        return False
    
    @staticmethod
    def addMessageId(messageId):
        if DataHandler.findMessageId(messageId):
            return;
        conn = sqlite3.connect("ClockInRecord.db")
        cursor = conn.cursor()
        cursor.execute("insert into message (message_id) values (?)", (messageId,))
        conn.commit()
        cursor.fetchone()
        conn.close()
