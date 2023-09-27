from .basic_client import BasicClient
from .fixerio_client import BASE_HTTPS_URL


class ProfessionalPlusClient(BasicClient):
    """ A client for the Fixer.io Professional Plus Plan. """

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

    def get_time_series(self, start_date, end_date, symbols=None, base=None):
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
        return self._time_series(start_date, end_date, symbols=symbols, base=base)

    def get_fluctuation(self, start_date, end_date, symbols=None, base=None):
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
        return self._fluctuation(start_date, end_date, symbols=symbols, base=base)
