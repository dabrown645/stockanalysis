class AlphaVantage(object):
    """This class can make any call to AlphaVantage api"""

    def __init__(self, api_key,
                 default_datatype="csv",
                 default_fastdmatype=0,
                 default_fastdperiod=3,
                 default_fastkperiod=5,
                 default_fastlimit=0.01,
                 default_slowlimit=0.01,
                 default_fastperiod=12,
                 default_signalperiod=9,
                 default_slowperiod=26,
                 default_slowdmatype=0,
                 default_slowdperiod=3,
                 default_slowkmatype=0,
                 default_slowkperiod=3,
                 default_outputsize="full",
                 ):
        super(AlphaVantage, self).__init__()
        self.api_key = api_key
        self.accepted_datatypes = ("csv", "json")

        if default_datatype not in self.accepted_datatypes:
            raise ValueError('%s datatype is not among the accepted: %s' % (self.accepted_datatypes, default_datatypes))

        self.defaults = {
            "datatype": default_datatype,
            "fastdmatype": default_fastdmatype,
            "fastdperiod": default_fastdperiod,
            "fastkperiod": default_fastkperiod,
            "fastlimit": default_fastlimit,
            "slowlimit": default_slowlimit,
            "fastperiod": default_fastperiod,
            "signalperiod": default_signalperiod,
            "slowperiod": default_slowperiod,
            "slowdmatype": default_slowdmatype,
            "slowdperiod": default_slowdperiod,
            "slowkmatype": default_slowkmatype,
            "slowkperiod": default_slowkperiod,
            "outputsize": default_outputsize,
        }

        self.functions_defs = {
            # STOCKS
            "TIME_SERIES_INTRADAY": ("symbol", "interval", "outputsize", "datatype"),
            "TIME_SERIES_DAILY": ("symbol", "outputsize", "datatype"),
            "TIME_SERIES_DAILY_ADJUSTED": ("symbol", "outputsize", "datatype"),
            "TIME_SERIES_WEEKLY": ("symbol", "outputsize", "datatype"),
            "TIME_SERIES_WEEKLY_ADJUSTED": ("symbol", "outputsize", "datatype"),
            "TIME_SERIES_MONTHLY": ("symbol", "outputsize", "datatype"),
            "TIME_SERIES_MONTHLY_ADJUSTED": ("symbol", "outputsize", "datatype"),
            "GLOBAL_QUOTE": ("symbol", "datatype"),
            "SYMBOL_SEARCH": ("keywords", "datatype"),
            # FOREX
            "FX_INTRADAY": ("from_symbol", "to_symbol", "interval", "outputsize", "datatype"),
            "FX_DAILY": ("from_symbol", "to_symbol", "outputsize", "datatype"),
            "FX_WEEKLY": ("from_symbol", "to_symbol", "outputsize", "datatype"),
            "FX_MONTHLY": ("from_symbol", "to_symbol", "outputsize", "datatype"),
            # CRYPTO
            "CURRENCY_EXCHANGE_RATE": ("from_currency", "to_currency"),
            "DIGITAL_CURRENCY_DAILY": ("symbol", "market"),
            "DIGITAL_CURRENCY_WEEKLY": ("symbol", "market"),
            "DIGITAL_CURRENCY_MONTHLY": ("symbol", "market"),
            # INDICTORS
            "SMA": ("symbol", "interval", "time_period", "series_type", "datatype"),
            "EMA": ("symbol", "interval", "time_period", "series_type", "datatype"),
            "WMA": ("symbol", "interval", "time_period", "series_type", "datatype"),
            "DEMA": ("symbol", "interval", "time_period", "series_type", "datatype"),
            "TEMA": ("symbol", "interval", "time_period", "series_type", "datatype"),
            "TRIMA": ("symbol", "interval", "time_period", "series_type", "datatype"),
            "KAMA": ("symbol", "interval", "time_period", "series_type", "datatype"),
            "MAMA": ("symbol", "interval", "series_type", "fastlimit", "slowlimit", "datatype"),
            "VWAP": ("symbol", "interval", "datatype"),
            "T3": ("symbol", "interval", "time_period", "series_type", "datatype"),
            "MACD": ("symbol", "interval", "series_type", "fastperiod", "slowperiod", "signalperiod", "datatype"),
            "MACDEXT": ("symbol", "interval", "series_type", "fastperiod", "slowperiod", "signalperiod", "datatype"),
            "STOCH": ("symbol", "interval", "fastkperiod", "slowkperiod", "slowdperiod", "slowkmatype", "slowdmatype", "datatype"),
            "STOCHF": ("symbol", "interval", "fastkperiod", "fastdperiod", "fastdmatype", "datatype"),
            "RSI": ("symbol", "interval", "series_type", "datatype"),
            "STOCHRSI": ("symbol", "interval", "series_type", "datatype"),
            "WILLR": ("symbol", "interval", "series_type", "datatype"),
            "ADX": ("symbol", "interval", "series_type", "datatype"),
            "ADXR": ("symbol", "interval", "series_type", "datatype"),
            "APO": ("symbol", "interval", "series_type", "datatype"),
            "PPO": ("symbol", "interval", "series_type", "datatype"),
            "MOM": ("symbol", "interval", "series_type", "datatype"),
            "BOP": ("symbol", "interval", "series_type", "datatype"),
            "CCI": ("symbol", "interval", "series_type", "datatype"),
            "CMO": ("symbol", "interval", "series_type", "datatype"),
            "ROC": ("symbol", "interval", "series_type", "datatype"),
            "ROCR": ("symbol", "interval", "series_type", "datatype"),
            "AROON": ("symbol", "interval", "series_type", "datatype"),
            "AROONOSC": ("symbol", "interval", "series_type", "datatype"),
            "MFI": ("symbol", "interval", "series_type", "datatype"),
            "TRIX": ("symbol", "interval", "series_type", "datatype"),
            "ULTOSC": ("symbol", "interval", "series_type", "datatype"),
            "DX": ("symbol", "interval", "series_type", "datatype"),
            "MINUS_DI": ("symbol", "interval", "series_type", "datatype"),
            "PLUS_DI": ("symbol", "interval", "series_type", "datatype"),
            "MINUS_DM": ("symbol", "interval", "series_type", "datatype"),
            "PLUS_DM": ("symbol", "interval", "series_type", "datatype"),
            "BBANDS": ("symbol", "interval", "series_type", "datatype"),
            "MIDPOINT": ("symbol", "interval", "series_type", "datatype"),
            "MIDPRICE": ("symbol", "interval", "series_type", "datatype"),
            "SAR": ("symbol", "interval", "series_type", "datatype"),
            "TRANGE": ("symbol", "interval", "series_type", "datatype"),
            "ATR": ("symbol", "interval", "series_type", "datatype"),
            "NATR": ("symbol", "interval", "series_type", "datatype"),
            "AD": ("symbol", "interval", "series_type", "datatype"),
            "ADOSC": ("symbol", "interval", "series_type", "datatype"),
            "OBV": ("symbol", "interval", "series_type", "datatype"),
            "HT_TRENDLINE": ("symbol", "interval", "series_type", "datatype"),
            "HT_SINE": ("symbol", "interval", "series_type", "datatype"),
            "HT_TRENDMODE": ("symbol", "interval", "series_type", "datatype"),
            "HT_DCPERIOD": ("symbol", "interval", "series_type", "datatype"),
            "HT_DCPHASE": ("symbol", "interval", "series_type", "datatype"),
            "HT_PHASOR": ("symbol", "interval", "series_type", "datatype")
        }

    def add_function_definitions(self, function_name, argument_list):
        """add (or overwrites) a function definition. function_name is the name as definied in AlphaVantage's doc,
        argument_list is a list or tuple of argument names passed to that function"""

        self.functions_defs[function_name] = argument_list

    def get_available_functions(self):
        """return the names of available functions"""
        return self.functions_defs.keys()

    def get_function_arguments(self, function_name):
        """return the arguments of a expected by a given function"""
        try:
            return self.functions_defs[function_name]
        except KeyError as e:
            raise KeyError(
                "%s is not among the defined functions. You can add it using self.add_function_definitions(function_name, argument_list)")

    def _get(self, function_name):
        """You should never have to call this magic function direclty. It will create a function for the API call and return it to you"""

        def __get(**params):
            import requests

            arg_list = set(self.functions_defs[function_name])

            required_defaults = {}
            for k in self.functions_defs[function_name]:
                if k in self.defaults:
                    required_defaults[k] = self.defaults[k]

            for k in required_defaults:
                if k not in params:
                    params[k] = required_defaults[k]

            args = set(params.keys())

            if arg_list != args:
                raise ValueError("function %s needs the following arguments: %s.\nGot: %s.\nDefaults: %s" % (
                function_name, arg_list, args, self.defaults))

            if "datatype" in params:
                datatype = params["datatype"]
            else:
                datatype = self.default_datatype

            bind_vars = {
                "apikey": self.api_key,
                "function": function_name
            }

            bind_vars.update(params)

            str_vars = []
            for k, v in bind_vars.items():
                str_vars.append("%s=%s" % (k, v))
            str_vars = '&'.join(str_vars)

            url = "https://www.alphavantage.co/query?%s" % str_vars
            print(f"url: {url}")
            data = requests.get(url)

            if datatype == "csv":
                import io
                return io.BytesIO(data.content)

            import json
            return json.loads(data.content)

        return __get

    def __getattr__(self, k):
        """If the attribute is not found in the the object and if is present in function definition. Create the function for the api call and return it"""
        defs = object.__getattribute__(self, "functions_defs")
        if k in defs:
            return self._get(k)


if __name__ == "__main__":
    import json
    alpha = AlphaVantage(api_key="&apikey=BXCLSC7GAHP5UGGO", default_datatype="json")
    #ticker = input("Enter ticker: ")
    #ticker = ticker.upper()
    ticker = "IBM"

    ### STOCKS
    #print(f'available functions: {alpha.get_available_functions()}')
    ##"TIME_SERIES_INTRADAY": ("symbol", "interval", "outputsize", "datatype"),
    #results = alpha.TIME_SERIES_INTRADAY(symbol=ticker, interval="60min", outputsize="compact", datatype="json"),
    #print(json.dumps(results, indent=4, sort_keys=True))
    ##"TIME_SERIES_DAILY": ("symbol", "outputsize", "datatype"),
    #results = alpha.TIME_SERIES_DAILY(symbol=ticker, outputsize="compact", datatype="json"),
    #print(json.dumps(results, indent=4, sort_keys=True))
    ##"TIME_SERIES_DAILY_ADJUSTED": ("symbol", "outputsize", "datatype"),
    #results = alpha.TIME_SERIES_DAILY_ADJUSTED(symbol=ticker, outputsize="compact", datatype="json"),
    #print(json.dumps(results, indent=4, sort_keys=True))
    ##"TIME_SERIES_WEEKLY": ("symbol", "outputsize", "datatype"),
    #results = alpha.TIME_SERIES_WEEKLY(symbol=ticker, outputsize="compact", datatype="json"),
    #print(json.dumps(results, indent=4, sort_keys=True))
    ##"TIME_SERIES_WEEKLY_ADJUSTED": ("symbol", "outputsize", "datatype"),
    #results = alpha.TIME_SERIES_WEEKLY_ADJUSTED(symbol=ticker, outputsize="compact", datatype="json"),
    #print(json.dumps(results, indent=4, sort_keys=True))
    ##"TIME_SERIES_MONTHLY": ("symbol", "outputsize", "datatype"),
    #results = alpha.TIME_SERIES_MONTHLY(symbol=ticker, outputsize="compact", datatype="json"),
    #print(json.dumps(results, indent=4, sort_keys=True))
    ##"TIME_SERIES_MONTHLY_ADJUSTED": ("symbol", "outputsize" "datatype"),
    #results = alpha.TIME_SERIES_MONTHLY_ADJUSTED(symbol=ticker, outputsize="compact", datatype="json"),
    #print(json.dumps(results, indent=4, sort_keys=True))
    ##"GLOBAL_QUOTE": ("symbol", "datatype"),
    #results = alpha.GLOBAL_QUOTE(symbol=ticker, datatype="json"),
    #print(json.dumps(results, indent=4, sort_keys=True))
    ##"SYMBOL_SEARCH": ("keywords", "datatype"),
    #results = alpha.SYMBOL_SEARCH(keywords=ticker, datatype="json"),
    #print(json.dumps(results, indent=4, sort_keys=True))


    ### FOREX
    ##"FX_INTRADAY": ("from_symbol", "to_symbol", "interval", "outputsize", "datatype"),
    #results = alpha.FX_INTRADAY(from_symbol="EUR", to_symbol="USD", interval="60min", outputsize="compact", datatype="json")
    #print(json.dumps(results, indent=4, sort_keys=True))
    ##"FX_DAILY": ("from_symbol", "to_symbol", "interval", "outputsize", "datatype"),
    #results = alpha.FX_DAILY(from_symbol="EUR", to_symbol="USD", outputsize="compact", datatype="json")
    #print(json.dumps(results, indent=4, sort_keys=True))
    ##"FX_WEEKLY": ("from_symbol", "to_symbol", "interval", "outputsize", "datatype"),
    #results = alpha.FX_WEEKLY(from_symbol="EUR", to_symbol="USD", outputsize="compact", datatype="json")
    #print(json.dumps(results, indent=4, sort_keys=True))
    ##"FX_MONTHLY": ("from_symbol", "to_symbol", "interval", "outputsize", "datatype"),
    #results = alpha.FX_MONTHLY(from_symbol="EUR", to_symbol="USD", outputsize="compact", datatype="json")
    #print(json.dumps(results, indent=4, sort_keys=True))

    ### CRYPTO
    ##"CURRENCY_EXCHANGE_RATE": ("from_currency", "to_currency", "datatype"),
    #results = alpha.CURRENCY_EXCHANGE_RATE(from_currency="EUR", to_currency="USD")
    #print(json.dumps(results, indent=4, sort_keys=True))
    ##"DIGITAL_CURRENCY_DAILY": ("symbol", "market", "datatype"),
    #results = alpha.DIGITAL_CURRENCY_DAILY(symbol="BTC", market="CNY")
    #print(json.dumps(results, indent=4, sort_keys=True))
    ##"DIGITAL_CURRENCY_WEEKLY": ("symbol", "market", "datatype"),
    #results = alpha.DIGITAL_CURRENCY_WEEKLY(symbol="BTC", market="CNY")
    #print(json.dumps(results, indent=4, sort_keys=True))
    ##"DIGITAL_CURRENCY_MONTHLY": ("symbol", "market", "datatype"),
    #results = alpha.DIGITAL_CURRENCY_MONTHLY(symbol="BTC", market="CNY")
    #print(json.dumps(results, indent=4, sort_keys=True))

    ### INDICTORS
    ##"SMA": ("symbol", "interval", "time_period", "series_type", "datatype"),
    #results = alpha.SMA(symbol=ticker, interval="monthly", time_period="60", series_type="close")
    #print(json.dumps(results, indent=4, sort_keys=True))
    ##"EMA": ("symbol", "interval", "time_period", "series_type", "datatype"),
    #results = alpha.EMA(symbol=ticker, interval="monthly", time_period="60", series_type="close")
    #print(json.dumps(results, indent=4, sort_keys=True))
    ##"WMA": ("symbol", "interval", "time_period", "series_type", "datatype"),
    #results = alpha.WMA(symbol=ticker, interval="monthly", time_period="60", series_type="close")
    #print(json.dumps(results, indent=4, sort_keys=True))
    ##"DEMA": ("symbol", "interval", "time_period", "series_type", "datatype"),
    #results = alpha.DEMA(symbol=ticker, interval="monthly", time_period=60, series_type="closed")
    #print(json.dumps(results, indent=4, sort_keys=True))
    ##"TEMA": ("symbol", "interval", "time_period", "series_type", "datatype"),
    #results = alpha.TEMA(symbol=ticker, interval="monthly", time_period=60, series_type="closed")
    #print(json.dumps(results, indent=4, sort_keys=True))
    ##"TRIMA": ("symbol", "interval", "time_period", "series_type", "datatype"),
    #results = alpha.TRIMA(symbol=ticker, interval="monthly", time_period=60, series_type="closed")
    #print(json.dumps(results, indent=4, sort_keys=True))
    ##"KAMA": ("symbol", "interval", "time_period", "series_type", "datatype"),
    #results = alpha.KAMA(symbol=ticker, interval="monthly", time_period=60, series_type="closed")
    #print(json.dumps(results, indent=4, sort_keys=True))
    ##"MAMA": ("symbol", "interval", "series_type", "fastlimit", "slowlimit", "datatype"),
    #results = alpha.MAMA(symbol=ticker, interval="monthly",fastlimit=0.02, slowlimit=0.01, series_type="closed")
    #print(json.dumps(results, indent=4, sort_keys=True))
    ##"VWAP": ("symbol", "interval", "datatype")
    #results = alpha.VWAP(symbol=ticker, interval="60min")
    #print(json.dumps(results, indent=4, sort_keys=True))
    ##"T3": ("symbol", "interval", "time_period", "series_type", "datatype"),
    #results = alpha.T3(symbol=ticker, interval="weekly", time_period=60, series_type="close")
    #print(json.dumps(results, indent=4, sort_keys=True))
    ##"MACD": ("symbol", "interval", "series_type", "fastperiod", "slowperiod", "signalperiod", "datatype"),
    #results = alpha.MACD(symbol=ticker, interval="monthly", fastperiod=12, slowperiod=26, signalperiod=9, series_type="close")
    #print(json.dumps(results, indent=4, sort_keys=True))
    ##"MACDEXT": ("symbol", "interval", "series_type", "datatype"),
    #results = alpha.MACDEXT(symbol=ticker, interval="monthly", fastperiod=12, slowperiod=26, signalperiod=9, series_type="close")
    #print(json.dumps(results, indent=4, sort_keys=True))
    ##"STOCH": ("symbol", "interval", "fastkperiod", "slowkperiod", "slowdperiod", "slowkmatype", "slowdmatype", "datatype"),
    #results = alpha.STOCH(symbol=ticker, interval="monthly", fastkperiod=5, slowkperiod=3, slowdperiod=3, slowkmatype=0, slowdmatype=0)
    #print(json.dumps(results, indent=4, sort_keys=True))
    #"STOCHF": ("symbol", "interval", "fastkperiod", "fastdperiod", "fastdmatype", "datatype"),
    results = alpha.STOCHF(symbol=ticker, interval="monthly", fastkperiod=5, fastdperiod=3, fastdmatype=0)
    print(json.dumps(results, indent=4, sort_keys=True))
    #"RSI": ("symbol", "interval", "series_type", "datatype"),
    #"STOCHRSI": ("symbol", "interval", "series_type", "datatype"),
    #"WILLR": ("symbol", "interval", "series_type", "datatype"),
    #"ADX": ("symbol", "interval", "series_type", "datatype"),
    #"ADXR": ("symbol", "interval", "series_type", "datatype"),
    #"APO": ("symbol", "interval", "series_type", "datatype"),
    #"PPO": ("symbol", "interval", "series_type", "datatype"),
    #"MOM": ("symbol", "interval", "series_type", "datatype"),
    #"BOP": ("symbol", "interval", "series_type", "datatype"),
    #"CCI": ("symbol", "interval", "series_type", "datatype"),
    #"CMO": ("symbol", "interval", "series_type", "datatype"),
    #"ROC": ("symbol", "interval", "series_type", "datatype"),
    #"ROCR": ("symbol", "interval", "series_type", "datatype"),
    #"AROON": ("symbol", "interval", "series_type", "datatype"),
    #"AROONOSC": ("symbol", "interval", "series_type", "datatype"),
    #"MFI": ("symbol", "interval", "series_type", "datatype"),
    #"TRIX": ("symbol", "interval", "series_type", "datatype"),
    #"ULTOSC": ("symbol", "interval", "series_type", "datatype"),
    #"DX": ("symbol", "interval", "series_type", "datatype"),
    #"MINUS_DI": ("symbol", "interval", "series_type", "datatype"),
    #"PLUS_DI": ("symbol", "interval", "series_type", "datatype"),
    #"MINUS_DM": ("symbol", "interval", "series_type", "datatype"),
    #"PLUS_DM": ("symbol", "interval", "series_type", "datatype"),
    #"BBANDS": ("symbol", "interval", "series_type", "datatype"),
    #"MIDPOINT": ("symbol", "interval", "series_type", "datatype"),
    #"MIDPRICE": ("symbol", "interval", "series_type", "datatype"),
    #"SAR": ("symbol", "interval", "series_type", "datatype"),
    #"TRANGE": ("symbol", "interval", "series_type", "datatype"),
    #"ATR": ("symbol", "interval", "series_type", "datatype"),
    #"NATR": ("symbol", "interval", "series_type", "datatype"),
    #"AD": ("symbol", "interval", "series_type", "datatype"),
    #"ADOSC": ("symbol", "interval", "series_type", "datatype"),
    #"OBV": ("symbol", "interval", "series_type", "datatype"),
    #"HT_TRENDLINE": ("symbol", "interval", "series_type", "datatype"),
    #"HT_SINE": ("symbol", "interval", "series_type", "datatype"),
    #"HT_TRENDMODE": ("symbol", "interval", "series_type", "datatype"),
    #"HT_DCPERIOD": ("symbol", "interval", "series_type", "datatype"),
    #"HT_DCPHASE": ("symbol", "interval", "series_type", "datatype"),
    #"HT_PHASOR": ("symbol", "interval", "series_type", "datatype")
    #"WMA": ("symbol", "interval", "series_type", "datatype"),
    #"DEMA": ("symbol", "interval", "series_type", "datatype"),
    #"TEMA": ("symbol", "interval", "series_type", "datatype"),
    #"TRIMA": ("symbol", "interval", "series_type", "datatype"),
    #"KAMA": ("symbol", "interval", "series_type", "datatype"),
    #"MAMA": ("symbol", "interval", "series_type", "datatype"),
    #"T3": ("symbol", "interval", "series_type", "datatype"),
    #"MACD": ("symbol", "interval", "series_type", "datatype"),
    #"MACDEXT": ("symbol", "interval", "series_type", "datatype"),
    #"STOCH": ("symbol", "interval", "series_type", "datatype"ibm),
    #"STOCHF": ("symbol", "interval", "series_type", "datatype"),
    #"RSI": ("symbol", "interval", "series_type", "datatype"),
    #"STOCHRSI": ("symbol", "interval", "series_type", "datatype"),
    #"WILLR": ("symbol", "interval", "series_type", "datatype"),
    #"ADX": ("symbol", "interval", "series_type", "datatype"),
    #"ADXR": ("symbol", "interval", "series_type", "datatype"),
    #"APO": ("symbol", "interval", "series_type", "datatype"),
    #"PPO": ("symbol", "interval", "series_type", "datatype"),
    #"MOM": ("symbol", "interval", "series_type", "datatype"),
    #"BOP": ("symbol", "interval", "series_type", "datatype"),
    #"CCI": ("symbol", "interval", "series_type", "datatype"),
    #"CMO": ("symbol", "interval", "series_type", "datatype"),
    #"ROC": ("symbol", "interval", "series_type", "datatype"),
    #"ROCR": ("symbol", "interval", "series_type", "datatype"),
    #"AROON": ("symbol", "interval", "series_type", "datatype"),
    #"AROONOSC": ("symbol", "interval", "series_type", "datatype"),
    #"MFI": ("symbol", "interval", "series_type", "datatype"),
    #"TRIX": ("symbol", "interval", "series_type", "datatype"),
    #"ULTOSC": ("symbol", "interval", "series_type", "datatype"),
    #"DX": ("symbol", "interval", "series_type", "datatype"),
    #"MINUS_DI": ("symbol", "interval", "series_type", "datatype"),
    #"PLUS_DI": ("symbol", "interval", "series_type", "datatype"),
    #"MINUS_DM": ("symbol", "interval", "series_type", "datatype"),
    #"PLUS_DM": ("symbol", "interval", "series_type", "datatype"),
    #"BBANDS": ("symbol", "interval", "series_type", "datatype"),
    #"MIDPOINT": ("symbol", "interval", "series_type", "datatype"),
    #"MIDPRICE": ("symbol", "interval", "series_type", "datatype"),
    #"SAR": ("symbol", "interval", "series_type", "datatype"),
    #"TRANGE": ("symbol", "interval", "series_type", "datatype"),
    #"ATR": ("symbol", "interval", "series_type", "datatype"),
    #"NATR": ("symbol", "interval", "series_type", "datatype"),
    #"AD": ("symbol", "interval", "series_type", "datatype"),
    #"ADOSC": ("symbol", "interval", "series_type", "datatype"),
    #"OBV": ("symbol", "interval", "series_type", "datatype"),
    #"HT_TRENDLINE": ("symbol", "interval", "series_type", "datatype"),
    #"HT_SINE": ("symbol", "interval", "series_type", "datatype"),
    #"HT_TRENDMODE": ("symbol", "interval", "series_type", "datatype"),
    #"HT_DCPERIOD": ("symbol", "interval", "series_type", "datatype"),
    #"HT_DCPHASE": ("symbol", "interval", "series_type", "datatype"),
    #"HT_PHASOR": ("symbol", "interval", "series_type", "datatype")
