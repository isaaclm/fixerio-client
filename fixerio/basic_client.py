from .free_client import FreeClient
from .url import BASE_HTTPS_URL

class BasicClient(FreeClient):
    """ A client for the Fixer.io Basic Plan. """

    def __init__(self, access_key, symbols=None, base=None):
        """
        :param access_key: your API Key.
        :type access_key: str or unicode
        :param symbols: currency symbols to request specific exchange rates.
        :type symbols: list or tuple
        :param base: currency symbol for base currency. The default base currency is EUR.
        :type base: str
        """
        super().__init__(access_key)
        self.base_url = BASE_HTTPS_URL
        self.symbols = symbols
        self.base = base

    def get_symbols(self):
        """ Gets all supported currencies with their respective three-letter currency codes and names.

        :return: all supported currencies with their respective three-letter currency codes and names.
        :rtype: dict
        :raises FixerioException: if any error making a request.
        """
        return self._symbols()

    def get_latest(self, symbols=None, base=None):
        """ Gets the exchange rate data for the currencies you have requested.

        :param symbols: a list of comma-separated currency codes to limit output currencies.
        :type symbols: list or tuple
        :param base: the three-letter currency code of your preferred base currency.
        :type base: str
        :return: the exchange rate data for the currencies you have requested.
        :rtype: dict
        :raises FixerioException: if any error making a request.
        """
        return self._latest(symbols=symbols, base=base)

    def get_historical_rates(self, date, symbols=None, base=None):
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
        return self._historical_rates(date, symbols=symbols, base=base)

    def convert_amount(self, from_ccy, to_ccy, amount, date=None):
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
        self._convert(from_ccy, to_ccy, amount, date=date)
