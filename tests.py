import unittest
from unittest.mock import patch, MagicMock

from main import add
from main import len_joke, get_joke

class TestMocks(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,3),5)

    @patch('main.get_joke')
    def test_len_joke(self, mock_get_joke):
        mock_get_joke.return_value = 'one'
        self.assertEqual(len_joke(),3)

    @patch('main.requests')
    def test_joke(self, mock_request):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'setup' : 'what are you eating',
            'punchline' : 'I am eating nothing'
        }
        mock_request.get.return_value = mock_response
        setup = mock_response.json()['setup']
        punchline = mock_response.json()['punchline']
        joke = 'question : ' +setup +'\nand\nanswer : '+punchline
        self.assertEqual(get_joke(),joke)



if __name__ == '__main__':
    unittest.main()
