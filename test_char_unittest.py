import unittest
import requests
import json
from my_task import get_charachter_details

class TestGetChar(unittest.TestCase):

    def test_correct_char(self):
    	data = {"name": "luke"}
    	result = requests.get(url="http://127.0.0.1:5000/char_details/", json=data)
    	self.assertEqual(result.status_code, 200)


    def test_incorrect_char(self):
    	data = {"name": "eeeeeeeee"}
    	result = requests.get(url="http://127.0.0.1:5000/char_details/", json=data)
    	self.assertEqual(json.loads(result.text)[0]["status code"], 404)


if __name__ == '__main__':
    unittest.main()
