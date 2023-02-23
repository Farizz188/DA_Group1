# Lab 8
# Demonstrate unit-testing

import unittest

class TestUrl(unittest.TestCase):

    def test_correct_url(self):
        url = 'http://172.18.58.80/snow'
        if url == 'http://172.18.58.80/snow':
            print("The URL is valid")
        else:
            print("The URL is invalid")
        self.assertEqual(url, 'http://172.18.58.80/snow')

if __name__ == '__main__':
    unittest.main()
