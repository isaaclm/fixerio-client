import unittest
import requests
from unittest.mock import patch
from fixerio.fixerio_client import FixerioClient, FixerioException


class FixerioSymbolsTestCase(unittest.TestCase):

    def setUp(self):
        self.access_key = 'your-access-key'
        self.base_url = "http://test.url"
        self.client = FixerioClient(self.access_key)
        self.client.base_url = self.base_url
        self.expected_url = f"{self.base_url}/symbols"

    @patch('requests.get')
    def test_url(self, mock_requests_get):
        expected_payload = {
            "access_key": self.access_key
        }

        self.client._symbols()

        mock_requests_get.assert_called_with(self.expected_url, params=expected_payload)

    @patch("requests.get")
    def test_request_error_raises_fixer_exception(self, mock_requests_get):
        mock_requests_get.side_effect = requests.exceptions.RequestException("Request failed")

        with self.assertRaises(FixerioException):
            self.client._symbols()
