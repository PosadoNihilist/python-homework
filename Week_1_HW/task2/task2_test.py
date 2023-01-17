import unittest
from task2 import *

class Test(unittest.TestCase):
    def test_sorting(self):
        test_data = read_data("input.txt")
        desired_data = read_data("desired_output.txt")
        result = format_data(test_data)
        self.assertEqual(result, desired_data)

if __name__ == '__main__':
    unittest.main()