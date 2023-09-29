import unittest
from unittest.mock import patch
from fixerio.free_client import FreeClient


class FixerioFreeClientTestCase(unittest.TestCase):

    @patch('fixerio.free_client.FreeClient._symbols')  # Mocking the _symbols method
    def test_get_symbols_calls_symbols_once_and_returns_value(self, mock_symbols):
        client = FreeClient(access_key='test-access-key')

        expected_return_value = {"USD": "US Dollar", "EUR": "Euro"}
        mock_symbols.return_value = expected_return_value

        result = client.get_symbols()

        mock_symbols.assert_called_once()

        self.assertEqual(result, expected_return_value)

    @patch('fixerio.free_client.FreeClient._latest')  # Mocking the _latest method
    def test_get_latest_calls_latest_once_and_returns_value(self, mock_latest):
        client = FreeClient(access_key='test-access-key')

        expected_return_value = {"USD": 1.1, "GBP": 0.9}
        mock_latest.return_value = expected_return_value

        result = client.get_latest()

        mock_latest.assert_called_once()

        self.assertEqual(result, expected_return_value)

    @patch('fixerio.free_client.FreeClient._historical_rates')  # Mocking the _historical_rates method
    def test_get_historical_rates_calls_historical_rates_once_and_returns_value(self, mock_historical_rates):
        client = FreeClient(access_key='test-access-key')

        date = "2001-01-01"
        expected_return_value = {"USD": 1.1, "EUR": 1.0, "date": date}
        mock_historical_rates.return_value = expected_return_value

        result = client._historical_rates(date, symbols=["USD", "EUR"])

        mock_historical_rates.assert_called_once()

        self.assertEqual(result, expected_return_value)
