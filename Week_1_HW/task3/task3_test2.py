import unittest
from task3 import *

class Test(unittest.TestCase):
    def test_sorting(self):
        test_data = "I don't know when the decision was made. If I had gone to university I would have studied medicine."
        desired_data = "I don't know when \nthe decision was \nmade. If I had gone \nto university I \nwould have studied \nmedicine.\n"
        result = format_text(test_data)
        self.assertEqual(result, desired_data)

if __name__ == '__main__':
    unittest.main()