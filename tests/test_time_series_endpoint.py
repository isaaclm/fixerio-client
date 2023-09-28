import unittest
import requests
from datetime import datetime
from unittest.mock import patch
from fixerio.fixerio_client import FixerioClient, FixerioException


class FixerioTimeSeriesTestCase(unittest.TestCase):

    def setUp(self):
        self.access_key = 'your-access-key'
        self.base_url = "http://test.url"
        self.start_date_as_str = "2006-12-24"
        self.start_date_as_date = datetime.strptime(self.start_date_as_str, "%Y-%m-%d").date()
        self.end_date_as_str = "2006-12-24"
        self.end_date_as_date = datetime.strptime(self.start_date_as_str, "%Y-%m-%d").date()
        self.client = FixerioClient(self.access_key)
        self.client.base_url = self.base_url
        self.expected_url = f"{self.base_url}/timeseries"

    @patch('requests.get')
    def test_url_with_dates(self, mock_requests_get):
        expected_payload = {
            "access_key": self.access_key,
            "start_date": self.start_date_as_str,
            "end_date": self.end_date_as_str
        }

        self.client._time_series(self.start_date_as_date, self.end_date_as_date)

        mock_requests_get.assert_called_with(self.expected_url, params=expected_payload)\

    @patch('requests.get')
    def test_url_with_date_strings(self, mock_requests_get):
        expected_payload = {
            "access_key": self.access_key,
            "start_date": self.start_date_as_str,
            "end_date": self.end_date_as_str
        }

        self.client._time_series(self.start_date_as_str, self.end_date_as_str)

        mock_requests_get.assert_called_with(self.expected_url, params=expected_payload)

    @patch("requests.get")
    def test_request_error_raises_fixer_exception(self, mock_requests_get):
        mock_requests_get.side_effect = requests.exceptions.RequestException("Request failed")

        with self.assertRaises(FixerioException):
            self.client._time_series(self.start_date_as_date, self.end_date_as_date)

    @patch("requests.get")
    def test_symbol_in_payload(self, mock_requests_get):
        symbols = ["USD", "EUR"]

        expected_payload = {
            "access_key": self.access_key,
            "start_date": self.start_date_as_str,
            "end_date": self.end_date_as_str,
            "symbols": ",".join(symbols)
        }

        self.client._time_series(self.start_date_as_date, self.end_date_as_date, symbols=symbols)

        mock_requests_get.assert_called_with(self.expected_url, params=expected_payload)

    @patch("requests.get")
    def test_base_in_payload(self, mock_requests_get):
        base = "GBP"

        expected_payload = {
            "access_key": self.access_key,
            "start_date": self.start_date_as_str,
            "end_date": self.end_date_as_str,
            "base": base
        }

        self.client._time_series(self.start_date_as_date, self.end_date_as_date, base=base)

        mock_requests_get.assert_called_with(self.expected_url, params=expected_payload)

    @patch("requests.get")
    def test_symbols_and_base_in_payload(self, mock_requests_get):
        symbols = ["USD", "EUR"]
        base = "GBP"

        expected_payload = {
            "access_key": self.access_key,
            "start_date": self.start_date_as_str,
            "end_date": self.end_date_as_str,
            "symbols" : ",".join(symbols),
            "base": base
        }

        self.client._time_series(self.start_date_as_date, self.end_date_as_date, symbols=symbols, base=base)

        mock_requests_get.assert_called_with(self.expected_url, params=expected_payload)
