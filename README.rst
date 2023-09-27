A Python client for `Fixer.io`_
===============================

`Fixer.io`_ is a simple and lightweight JSON API for current and historical foreign
exchange (forex) rates. Fixer.io:

This library contains clients for each tier of the fixer.io subscriptions, from
free up to professional plus. Each tier extends the prior, so if you upgrade your
subscription, you can simply swap out your client by changing 1 line of code.

Installation
------------

You can get the source from GitHub at
https://github.com/isaaclm/fixerio-client.

Usage
-----

Get the latest foreign exchange reference rates in JSON format. You can request specific rates
by specifying the symbols as in this example.

.. code:: python

    >>> import fixerio

    >>> fxrio = fixerio.FreeClient(access_key='YOUR FREE ACCESS KEY')
    >>> fxrio.get_latest(symbols=["USD", "CNY", "CAD", "JPY", "GBP", "CHF"])
    '''
     {
       u'rates':
       {
         u'USD': 1.050282,
         u'CNY': 7.678637,
         u'CAD': 1.419047,
         u'JPY': 157.141116,
         u'GBP': 0.866294,
         u'CHF': 0.966654
       },
       u'success': True,
       u'timestamp': 1695832924,
       u'base': u'EUR',
       u'date': u'2023-09-27'
     }
    '''

If you don't specify the symbols you will request all rates for your
base currency.

Note that the only available base currency on the free subscription is 'EUR'.

Get the list of available currencies.

.. code:: python

    >>> import fixerio

    >>> fxrio = fixerio.FreeClient(access_key='YOUR FREE ACCESS KEY')
    >>> fxrio.get_symbols()
    '''
     {
       u'success': True,
       u'symbols':
       {
         u'AED': u'United Arab Emirates Dirham',
         u'AFN': u'Afghan Afghani',
         u'ALL': u'Albanian Lek',
         ...
         u'ZWL': u'Zimbabwean Dollar'
       }
     }
    '''

Get historical rates for any day since 1999.

.. code:: python

    >>> import fixerio
    >>> from datetime import date, timedelta

    >>> yesterday = date.today() - timedelta(days=1)
    >>> fxrio = fixerio.FreeClient(access_key='YOUR FREE ACCESS KEY')
    >>> fxrio.historical_rates(yesterday)
    '''
     {
       u'rates':
       {
         u'USD': 1.05692,
         u'GBP': 0.870168
       },
       u'success': True,
       u'timestamp': 1695772799,
       u'historical': True,
       u'base': u'EUR',
       u'date': u'2023-09-26'
     }
    '''


Useful Links
-----

Fixer.io: https://fixer.io/

Fixer.io documentation: https://fixer.io/documentation