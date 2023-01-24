import unittest
from main import *

AddNewUser("Mike")
AddNewUser("Bob")
AddNewChat("First Chat", [100001, 100002])
AddNewMessage(200001, 100001, "hi bob")
AddNewMessage(200001, 100002, "hi mike")
AddNewUser("Carl")
AddNewChat("Second Chat", [100001, 100002, 100003])
AddNewMessage(200002, 100003, "hi guys")
AddNewMessage(200002, 100001, "hi carl")
AddNewMessage(200002, 100002, "hi carl")

class Test(unittest.TestCase):
    def test_ListOfUserChats(self):
        expected_data = ("[[200001, 'First Chat', [100001, 100002], '"
        + str(chat_storage.get_chat(200001).cr_time) +
        "'], [200002, 'Second Chat', [100001, 100002, 100003], '"
        + str(chat_storage.get_chat(200002).cr_time) +
        "']]")
        
        result = str(ListOfUserChats(100001))
        self.assertEqual(result, expected_data)
    def test_ListOfChatMessages(self):
        expected_data = ("[[300001, 200001, 100001, 'hi bob', '"
        + str(message_storage.get_message(300001).cr_time) +
        "'], [300002, 200001, 100002, 'hi mike', '"
        + str(message_storage.get_message(300002).cr_time) +
        "']]")
        
        result = str(ListOfChatMessages(200001))
        self.assertEqual(result, expected_data)

if __name__ == '__main__':
    unittest.main()
