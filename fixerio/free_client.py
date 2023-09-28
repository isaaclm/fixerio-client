from .fixerio_client import FixerioClient
from .url import BASE_HTTP_URL

class FreeClient(FixerioClient):
    """ A client for the Fixer.io Free Plan. """

    def __init__(self, access_key, symbols=None):
        """
        :param access_key: your API Key.
        :type access_key: str or unicode
        :param symbols: currency symbols to request specific exchange rates.
        :type symbols: list or tuple
        """
        super().__init__(access_key)
        self.base_url = BASE_HTTP_URL
        self.symbols = symbols

    def get_symbols(self):
        """ Gets all supported currencies with their respective three-letter currency codes and names.

        :return: all supported currencies with their respective three-letter currency codes and names.
        :rtype: dict
        :raises FixerioException: if any error making a request.
        """
        return self._symbols()

    def get_latest(self, symbols=None):
        """ Gets the exchange rate data for the currencies you have requested.

        :param symbols: a list of comma-separated currency codes to limit output currencies.
        :type symbols: list or tuple
        :return: the exchange rate data for the currencies you have requested.
        :rtype: dict
        :raises FixerioException: if any error making a request.
        """
        return self._latest(symbols=symbols)

    def get_historical_rates(self, date, symbols=None):
        """ Gets historical rates for any day since `date`.
        Historical rates are available for most currencies all the way back to the year of 1999.

        :param date: a date in the past for which historical rates are requested.
        :type date: date or str (in YYYY-MM-DD format)
        :param symbols: a list of currency codes to limit output currencies.
        :type symbols: list or tuple
        :return: the historical exchange rate data for the currencies you have requested.
        :rtype: dict
        :raises FixerioException: if any error making a request.
        """
        return self._historical_rates(date, symbols=symbols)
