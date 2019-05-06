class AlphaVantage(object):
    """This class can make any call to AlphaVantage api"""

    def __init__(self, api_key,
                 default_accelertion=0.01,
                 default_datatype="csv",
                 default_fastdmatype=0,
                 default_fastdperiod=3,
                 default_fastkperiod=5,
                 default_fastlimit=0.01,
                 default_slowlimit=0.01,
                 default_fastperiod=12,
                 default_matype=0,
                 default_maximum=0.02,
                 default_ndevdn=2,
                 default_ndevup=2,
                 default_outputsize="full",
                 default_signalperiod=9,
                 default_slowperiod=26,
                 default_slowdmatype=0,
                 default_slowdperiod=3,
                 default_slowkmatype=0,
                 default_slowkperiod=3,
                 default_timeperiod1=7,
                 default_timeperiod2=14,
                 default_timeperiod3=28,
                 ):
        super(AlphaVantage, self).__init__()
        self.api_key = api_key
        self.accepted_datatypes = ("csv", "json")

        if default_datatype not in self.accepted_datatypes:
            raise ValueError('%s datatype is not among the accepted: %s' % (self.accepted_datatypes, default_datatypes))

        self.defaults = {
            "acceleration": default_accelertion,
            "datatype": default_datatype,
            "fastdmatype": default_fastdmatype,
            "fastdperiod": default_fastdperiod,
            "fastkperiod": default_fastkperiod,
            "fastlimit": default_fastlimit,
            "fastperiod": default_fastperiod,
            "matype": default_matype,
            "maximum": default_maximum,
            "ndevdn": default_ndevdn,
            "ndevup": default_ndevup,
            "outputsize": default_outputsize,
            "slowlimit": default_slowlimit,
            "signalperiod": default_signalperiod,
            "slowperiod": default_slowperiod,
            "slowdmatype": default_slowdmatype,
            "slowdperiod": default_slowdperiod,
            "slowkmatype": default_slowkmatype,
            "slowkperiod": default_slowkperiod,
            "timeperiod1": default_timeperiod1,
            "timeperiod2": default_timeperiod2,
            "timeperiod3": default_timeperiod3,
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

            "RSI": ("symbol", "interval", "time_period", "series_type", "datatype"),
            "STOCHRSI": ("symbol", "interval", "time_period", "series_type", "fastkperiod", "fastdperiod", "fastdmatype", "datatype"),
            "WILLR": ("symbol", "interval", "time_period", "datatype"),
            "ADX": ("symbol", "interval", "time_period", "datatype"),
            "ADXR": ("symbol", "interval", "time_period", "datatype"),
            "APO": ("symbol", "interval", "series_type", "fastperiod", "slowperiod", "matype", "datatype"),
            "PPO": ("symbol", "interval", "series_type", "fastperiod", "slowperiod", "matype", "datatype"),
            "MOM": ("symbol", "interval", "time_period", "series_type", "datatype"),
            "BOP": ("symbol", "interval", "datatype"),
            "CCI": ("symbol", "interval", "time_period", "datatype"),
            "CMO": ("symbol", "interval", "time_period", "series_type", "datatype"),
            "ROC": ("symbol", "interval", "time_period", "series_type", "datatype"),
            "ROCR": ("symbol", "interval", "time_period", "series_type", "datatype"),
            "AROON": ("symbol", "interval", "time_period", "datatype"),
            "AROONOSC": ("symbol", "interval", "time_period", "datatype"),
            "MFI": ("symbol", "interval", "time_period", "datatype"),
            "TRIX": ("symbol", "interval", "time_period", "series_type", "datatype"),
            "ULTOSC": ("symbol", "interval", "timeperiod1", "timeperiod2", "timeperiod3", "datatype"),
            "DX": ("symbol", "interval", "time_period", "datatype"),
            "MINUS_DI": ("symbol", "interval", "time_period", "datatype"),
            "PLUS_DI": ("symbol", "interval", "time_period", "datatype"),
            "MINUS_DM": ("symbol", "interval", "time_period", "datatype"),
            "PLUS_DM": ("symbol", "interval", "time_period", "datatype"),
            "BBANDS": ("symbol", "interval", "time_period", "series_type", "nbdevup", "nbdevdn",  "matype", "datatype"),
            "MIDPOINT": ("symbol", "interval", "time_period", "series_type", "datatype"),
            "MIDPRICE": ("symbol", "interval", "time_period", "datatype"),
            "SAR": ("symbol", "interval", "acceleration", "maximum", "datatype"),
            "TRANGE": ("symbol", "interval", "datatype"),
            "ATR": ("symbol", "interval", "time_period", "datatype"),
            "NATR": ("symbol", "interval", "time_period", "datatype"),
            "AD": ("symbol", "interval", "datatype"),
            "ADOSC": ("symbol", "interval", "fastperiod", "slowperiod", "datatype"),
            "OBV": ("symbol", "interval", "datatype"),
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
            print(f'url {url}')
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


