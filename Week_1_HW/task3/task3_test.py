import unittest
from task3 import *

class Test(unittest.TestCase):
    def test_sorting(self):
        test_data = "She married a very nice young architect from Belfast, whom she met on a bus."
        desired_data = "She married a very \nnice young architect \nfrom Belfast, whom \nshe met on a bus.\n"
        result = format_text(test_data)
        self.assertEqual(result, desired_data)

if __name__ == '__main__':
    unittest.main()