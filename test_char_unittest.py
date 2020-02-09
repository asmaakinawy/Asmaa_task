import unittest
import requests
from my_task import get_charachter_details

class TestGetChar(unittest.TestCase):

    def test_correct_char(self):
    	data = {"name": "luke"}
    	result = requests.get(url="http://127.0.0.1:5000/char_details/", json=data)
    	self.assertEqual(result.status_code, 200)


        def test_incorrect_char(self):
    	data = {"name": "eele"}
    	result = requests.get(url="http://127.0.0.1:5000/char_details/", json=data)
    	self.assertEqual(result.status_code, 404)


if __name__ == '__main__':
    unittest.main()
