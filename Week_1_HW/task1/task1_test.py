import unittest
from task1 import *

class Test(unittest.TestCase):
    def test_sorting(self):
        test_data = "1. Котов Алексей: 3\n2. Белова Юлия: 3\n3. Шахвалиева Юлиана: 4"
        desired_data = "name,grade\nБелова Юлия,3\nКотов Алексей,3\nШахвалиева Юлиана,4\n"
        result = format_data(test_data)
        self.assertEqual(result, desired_data)

if __name__ == '__main__':
    unittest.main()