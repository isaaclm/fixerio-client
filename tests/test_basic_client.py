import unittest
from unittest.mock import patch

import fixerio.free_client
from fixerio.basic_client import BasicClient


class FixerioBasicClientTestCase(unittest.TestCase):

    @patch('fixerio.basic_client.BasicClient._symbols')  # Mocking the _symbols method
    def test_get_symbols_calls_symbols_once_and_returns_value(self, mock_symbols):
        client = BasicClient(access_key='test-access-key')

        expected_return_value = {"USD": "US Dollar", "EUR": "Euro"}
        mock_symbols.return_value = expected_return_value

        result = client.get_symbols()

        mock_symbols.assert_called_once()

        self.assertEqual(result, expected_return_value)

    @patch('fixerio.basic_client.BasicClient._latest')  # Mocking the _latest method
    def test_get_latest_calls_latest_once_and_returns_value(self, mock_latest):
        client = BasicClient(access_key='test-access-key')

        expected_return_value = {"USD": 1.0, "EUR": 0.85}
        mock_latest.return_value = expected_return_value

        result = client.get_latest(symbols=["USD", "EUR"], base="USD")

        mock_latest.assert_called_once()

        self.assertEqual(result, expected_return_value)

    @patch('fixerio.basic_client.BasicClient._historical_rates')  # Mocking the _historical_rates method
    def test_get_historical_rates_calls_historical_rates_once_and_returns_value(self, mock_historical_rates):
        client = BasicClient(access_key='test-access-key')

        date = "2001-01-01"
        expected_return_value = {"USD": 1.1, "GBP": 0.9, "date": date}
        mock_historical_rates.return_value = expected_return_value

        result = client._historical_rates(date, symbols=["USD", "EUR"], base="USD")

        mock_historical_rates.assert_called_once()

        self.assertEqual(result, expected_return_value)

    @patch('fixerio.basic_client.BasicClient._convert')  # Mocking the _convert method
    def test_convert_amount_rates_calls_convert_once_and_returns_value(self, mock_convert):
        client = BasicClient(access_key='test-access-key')

        expected_return_value = {"result": 85.0}
        mock_convert.return_value = expected_return_value

        result = client.convert_amount("USD", "EUR", 100)

        mock_convert.assert_called_once()

        self.assertEqual(result, expected_return_value)

    def test_inherited_from_cheaper_subscriptions(self):
        self.assertTrue(issubclass(BasicClient, fixerio.free_client.FreeClient))
