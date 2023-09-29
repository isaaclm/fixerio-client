import unittest
import requests
from unittest.mock import patch
from fixerio.fixerio_client import FixerioClient, FixerioException


class FixerioLatestTestCase(unittest.TestCase):

    def setUp(self):
        self.access_key = 'your-access-key'
        self.client = FixerioClient(self.access_key)
        self.expected_url = "http://data.fixer.io/api/latest"

    @patch('requests.get')
    def test_url(self, mock_requests_get):
        expected_payload = {
            "access_key": self.access_key
        }

        self.client._latest()

        mock_requests_get.assert_called_with(self.expected_url, params=expected_payload)

    @patch("requests.get")
    def test_request_error_raises_fixer_exception(self, mock_requests_get):
        mock_requests_get.side_effect = requests.exceptions.RequestException("Request failed")

        with self.assertRaises(FixerioException):
            self.client._latest()

    @patch("requests.get")
    def test_symbol_in_payload(self, mock_requests_get):
        symbols = ["USD", "EUR"]

        expected_payload = {
            "access_key": self.access_key,
            "symbols": ",".join(symbols)
        }

        self.client._latest(symbols=symbols)

        mock_requests_get.assert_called_with(self.expected_url, params=expected_payload)

    @patch("requests.get")
    def test_base_in_payload(self, mock_requests_get):
        base = "GBP"

        expected_payload = {
            "access_key": self.access_key,
            "base": base
        }

        self.client._latest(base=base)

        mock_requests_get.assert_called_with(self.expected_url, params=expected_payload)

    @patch("requests.get")
    def test_symbols_and_base_in_payload(self, mock_requests_get):
        symbols = ["USD", "EUR"]
        base = "GBP"

        expected_payload = {
            "access_key": self.access_key,
            "symbols": ",".join(symbols),
            "base": base
        }

        self.client._latest(symbols=symbols, base=base)

        mock_requests_get.assert_called_with(self.expected_url, params=expected_payload)
