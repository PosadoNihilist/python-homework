import unittest
from task5 import *

class Test(unittest.TestCase):
    def test_sorting(self):
        test_data = ["eat","tea","tan","ate","nat","bat", "tab", "man", "not", "ton"]
        desired_data = [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat', 'tab'], ['man'], ['not', 'ton']]
        result = find_anagrams(test_data)
        self.assertEqual(result, desired_data)

if __name__ == '__main__':
    unittest.main()