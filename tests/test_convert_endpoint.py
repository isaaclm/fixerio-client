import unittest
import requests
from datetime import datetime
from unittest.mock import patch
from fixerio.fixerio_client import FixerioClient, FixerioException


class FixerioConvertTestCase(unittest.TestCase):

    def setUp(self):
        self.access_key = 'your-access-key'
        self.date_as_str = "2006-12-24"
        self.date_as_date = datetime.strptime(self.date_as_str, "%Y-%m-%d").date()
        self.client = FixerioClient(self.access_key)
        self.expected_url = "http://data.fixer.io/api/convert"

    @patch('requests.get')
    def test_url(self, mock_requests_get):
        from_ccy = "USD"
        to_ccy = "EUR"
        amount = 100

        expected_payload = {
            "access_key": self.access_key,
            "from": from_ccy,
            "to": to_ccy,
            "amount": amount
        }

        self.client._convert(from_ccy, to_ccy, amount)

        mock_requests_get.assert_called_with(self.expected_url, params=expected_payload)

    @patch("requests.get")
    def test_request_error_raises_fixer_exception(self, mock_requests_get):
        from_ccy = "USD"
        to_ccy = "EUR"
        amount = 100

        mock_requests_get.side_effect = requests.exceptions.RequestException("Request failed")

        with self.assertRaises(FixerioException):
            self.client._convert(from_ccy, to_ccy, amount)

    @patch("requests.get")
    def test_date_in_payload(self, mock_requests_get):
        from_ccy = "USD"
        to_ccy = "EUR"
        amount = 100

        expected_payload = {
            "access_key": self.access_key,
            "from": from_ccy,
            "to": to_ccy,
            "amount": amount,
            "date": self.date_as_str
        }

        self.client._convert(from_ccy, to_ccy, amount, date=self.date_as_date)

        mock_requests_get.assert_called_with(self.expected_url, params=expected_payload)

    @patch("requests.get")
    def test_date_string_in_payload(self, mock_requests_get):
        from_ccy = "USD"
        to_ccy = "EUR"
        amount = 100

        expected_payload = {
            "access_key": self.access_key,
            "from": from_ccy,
            "to": to_ccy,
            "amount": amount,
            "date": self.date_as_str
        }

        self.client._convert(from_ccy, to_ccy, amount, date=self.date_as_str)

        mock_requests_get.assert_called_with(self.expected_url, params=expected_payload)
