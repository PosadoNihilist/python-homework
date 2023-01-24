from datetime import datetime

user_id_generator = 100000
chat_id_generator= 200000
message_id_generator = 300000

class User:
    def __init__(self, username):
        self.username = username
        self.cr_time = str(datetime.now())
        self.list_chats = []
        self.list_messages = []
        
    def set_id(self, id):
        self.id = id
    
    def add_new_chat(self, chat):
        self.list_chats.append(chat)
    
    def add_new_message(self, message):
        self.list_messages.append(message)

class Chat:
    def __init__(self, name, users):
        self.name = name
        self.users = users
        self.cr_time = str(datetime.now())
        self.list_messages = []
        
    def set_id(self, id):
        self.id = id  
    
    def add_new_message(self, message):
        self.list_messages.append(message)
    
class Message:
    def __init__(self, chat_id, author_id, text):
        self.chat_id = chat_id
        self.author_id = author_id
        self.text = text
        self.cr_time = str(datetime.now())
    def set_id(self, id):
        self.id = id  
        
class UserStorage:
    def __init__(self):
        self.__RECORDS = {}
    
    def get_user(self, id):
        return self.__RECORDS.get(id, None)
    
    def add_user(self, user):
        global user_id_generator
        user_id_generator += 1 
        user.set_id(user_id_generator)
        self.__RECORDS[user_id_generator] = user
        return user.id

class ChatStorage:
    def __init__(self):
        self.__RECORDS = {}
    
    def get_chat(self, id):
        return self.__RECORDS.get(id, None)
    
    def add_chat(self, chat):
        global chat_id_generator
        chat_id_generator += 1
        chat.set_id(chat_id_generator)
        self.__RECORDS[chat_id_generator] = chat
        for user in chat.users:
            user_storage.get_user(user).add_new_chat(chat)
        return chat.id

class MessageStorage:
    def __init__(self):
        self.__RECORDS = {}
    
    def get_message(self, id):
        return self.__RECORDS.get(id, None)
    
    def add_message(self, message):
        global message_id_generator
        message_id_generator += 1 
        message.set_id(message_id_generator)
        self.__RECORDS[message_id_generator] = message
        user = message.author_id
        chat = message.chat_id
        user_storage.get_user(user).add_new_message(message)
        chat_storage.get_chat(chat).add_new_message(message)
        return message.id

user_storage = UserStorage()
chat_storage = ChatStorage()
message_storage = MessageStorage()

def AddNewUser(username):
    NewUser = User(username)
    return(user_storage.add_user(NewUser))

def AddNewChat(chat_name, users):
    NewChat = Chat(chat_name, users)
    return(chat_storage.add_chat(NewChat))

def AddNewMessage(chat_id, author_id, text):
    NewMessage = Message(chat_id, author_id, text)
    return(message_storage.add_message(NewMessage))

def ListOfUserChats(user):
    result = []
    for elem in user_storage.get_user(user).list_chats:
        result.append([elem.id, elem.name, elem.users, elem.cr_time])
    result.sort(key = lambda l: l[3])
    return(result)
        
def ListOfChatMessages(chat):
    result = []
    for elem in chat_storage.get_chat(chat).list_messages:
        result.append([elem.id, elem.chat_id, elem.author_id, elem.text, elem.cr_time])
    result.sort(key = lambda l: l[4])
    return(result)