import datetime
import requests
from .exceptions import FixerioException
from .url import BASE_HTTP_URL


class FixerioClient(object):
    """ A client for Fixer.io. """
    base_url = BASE_HTTP_URL

    def __init__(self, access_key, symbols=None, base=None):
        """
        :param access_key: your API Key.
        :type access_key: str or unicode
        :param symbols: currency symbols to request specific exchange rates.
        :type symbols: list or tuple
        :param base: currency symbol for base currency. The default base currency is EUR.
        :type base: str
        """
        self.access_key = access_key
        self.symbols = symbols
        self.base = base

    def _create_payload(self, **kwargs):
        """ Creates a payload with no None values.

        :param kwargs: keyword arguments for payload creation.
        :return: a payload.
        :rtype: dict
        """
        payload = {'access_key': self.access_key}

        # Define a mapping for variable name translation as 'from' is a reserved keyword
        variable_mapping = {
            "from_ccy": "from",
            "to_ccy": "to"
        }

        for key, value in kwargs.items():
            # Check if the variable name is in the mapping and translate it
            if key in variable_mapping:
                mapped_key = variable_mapping[key]
            else:
                mapped_key = key

            if value is not None:
                if isinstance(value, (str, int, float)):
                    payload[mapped_key] = value
                elif isinstance(value, (list, tuple)) and all(isinstance(item, str) for item in value):
                    payload[mapped_key] = ','.join(value)

        return payload

    def _symbols(self):
        """ Gets all supported currencies with their respective three-letter currency codes and names.

        :return: all supported currencies with their respective three-letter currency codes and names.
        :rtype: dict
        :raises FixerioException: if any error making a request.
        """
        try:
            payload = self._create_payload()

            url = f"{self.base_url}/symbols"

            response = requests.get(url, params=payload)

            response.raise_for_status()

            return response.json()
        except requests.exceptions.RequestException as ex:
            raise FixerioException(str(ex))

    def _latest(self, symbols=None, base=None):
        """ Gets the exchange rate data for the currencies you have requested.

        :param symbols: a list of comma-separated currency codes to limit output currencies.
        :type symbols: list or tuple
        :param base: the three-letter currency code of your preferred base currency.
        :type base: str
        :return: the exchange rate data for the currencies you have requested.
        :rtype: dict
        :raises FixerioException: if any error making a request.
        """
        try:
            symbols = symbols if (symbols is not None) else self.symbols
            base = base if (base is not None) else self.base

            payload = self._create_payload(symbols=symbols, base=base)

            url = f"{self.base_url}/latest"

            response = requests.get(url, params=payload)

            response.raise_for_status()

            return response.json()
        except requests.exceptions.RequestException as ex:
            raise FixerioException(str(ex))

    def _historical_rates(self, date, symbols=None, base=None):
        """ Gets historical rates for any day since `date`.
        Historical rates are available for most currencies all the way back to the year of 1999.

        :param date: a date in the past for which historical rates are requested.
        :type date: date or str (in YYYY-MM-DD format)
        :param symbols: a list of currency codes to limit output currencies.
        :type symbols: list or tuple
        :param base: the three-letter currency code of your preferred base currency.
        :type base: str
        :return: the historical exchange rate data for the currencies you have requested.
        :rtype: dict
        :raises FixerioException: if any error making a request.
        """
        try:
            if isinstance(date, datetime.date):
                # Convert date to ISO 8601 format.
                date = date.isoformat()

            symbols = symbols if (symbols is not None) else self.symbols
            base = base if (base is not None) else self.base

            symbols = symbols or self.symbols
            payload = self._create_payload(symbols=symbols, base=base)

            url = f"{self.base_url}/{date}"

            response = requests.get(url, params=payload)

            response.raise_for_status()

            return response.json()
        except requests.exceptions.RequestException as ex:
            raise FixerioException(str(ex))

    def _convert(self, from_ccy, to_ccy, amount, date=None):
        """ Converts an amount from one currency to another

        :param from_ccy: the three-letter currency code of the currency you would like to convert from.
        :type from_ccy: str
        :param to_ccy: the three-letter currency code of the currency you would like to convert to.
        :type to_ccy: str
        :param amount: the amount to be converted.
        :type amount: int or float
        :param date: specify a date to use historical rates for this conversion.
        :type date: date or str (in YYYY-MM-DD format)
        :return: your conversion result.
        :rtype: dict
        :raises FixerioException: if any error making a request.
        """
        try:
            if isinstance(date, datetime.date):
                # Convert date to ISO 8601 format.
                date = date.isoformat()

            payload = self._create_payload(from_ccy=from_ccy, to_ccy=to_ccy, amount=amount, date=date)

            url = f"{self.base_url}/convert"

            response = requests.get(url, params=payload)

            response.raise_for_status()

            return response.json()
        except requests.exceptions.RequestException as ex:
            raise FixerioException(str(ex))

    def _time_series(self, start_date, end_date, symbols=None, base=None):
        """ Gets daily historical rates between two dates of your choice, with a maximum time frame of 365 days.

        :param start_date: the start date of your preferred timeframe.
        :type start_date: date or str (in YYYY-MM-DD format)
        :param end_date: the end date of your preferred timeframe.
        :type end_date: date or str (in YYYY-MM-DD format)
        :param symbols: a list of currency codes to limit output currencies.
        :type symbols: list or tuple
        :param base: the three-letter currency code of your preferred base currency.
        :type base: str
        :return: the time series of exchange rates for the currencies you have requested.
        :rtype: dict
        :raises FixerioException: if any error making a request.
        """
        try:
            if isinstance(start_date, datetime.date):
                # Convert date to ISO 8601 format.
                start_date = start_date.isoformat()

            if isinstance(end_date, datetime.date):
                # Convert date to ISO 8601 format.
                end_date = end_date.isoformat()

            symbols = symbols if (symbols is not None) else self.symbols
            base = base if (base is not None) else self.base

            payload = self._create_payload(start_date=start_date, end_date=end_date, symbols=symbols, base=base)

            url = f"{self.base_url}/timeseries"

            response = requests.get(url, params=payload)

            response.raise_for_status()

            return response.json()
        except requests.exceptions.RequestException as ex:
            raise FixerioException(str(ex))

    def _fluctuation(self, start_date, end_date, symbols=None, base=None):
        """ Gets the starting and ending rates with absolute and percentage changes over the fluctuation timeframe.

        :param start_date: the start date of your preferred fluctuation timeframe.
        :type start_date: date or str (in YYYY-MM-DD format)
        :param end_date: the end date of your preferred fluctuation timeframe.
        :type end_date: date or str (in YYYY-MM-DD format)
        :param symbols: a list of currency codes to limit output currencies.
        :type symbols: list or tuple
        :param base: the three-letter currency code of your preferred base currency.
        :type base: str
        :return: the exchange rate and fluctuation data for the currencies you have requested.
        :rtype: dict
        :raises FixerioException: if any error making a request.
        """
        try:
            if isinstance(start_date, datetime.date):
                # Convert date to ISO 8601 format.
                start_date = start_date.isoformat()

            if isinstance(end_date, datetime.date):
                # Convert date to ISO 8601 format.
                end_date = end_date.isoformat()

            symbols = symbols if (symbols is not None) else self.symbols
            base = base if (base is not None) else self.base

            payload = self._create_payload(start_date=start_date, end_date=end_date, symbols=symbols, base=base)

            url = f"{self.base_url}/fluctuation"

            response = requests.get(url, params=payload)

            response.raise_for_status()

            return response.json()
        except requests.exceptions.RequestException as ex:
            raise FixerioException(str(ex))
