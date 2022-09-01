import unittest
from crud import insert_file

class insertFile(unittest.TestCase):
    def test_insert_file(self):
        actual_result = insert_file('DarkMatter', '.pdf', 'Physics')
        expected_result = True
        self.assertEqual(actual_result, expected_result)


