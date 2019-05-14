class IEXCloud(object):
    """This class can make any call to AlphaVantage api"""

    def __init__(self, token, sandbox=False):
        super(IEXCloud, self).__init__()
        self.api_key = token
        if sandbox:
            baseurl = 'https://sandbox.iexapis.com/stable/stock'
        else:
            baseurl = 'https://cloud.iexapis.com/stable/stock'

        #if default_datatype not in self.accepted_datatypes:
        #    raise ValueError('%s datatype is not among the accepted: %s' % (self.accepted_datatypes, default_datatypes))

        #self.defaults = {
        #    "acceleration": default_accelertion,
        #    "datatype": default_datatype,
        #    "fastdmatype": default_fastdmatype,
        #    "fastdperiod": default_fastdperiod,
        #    "fastkperiod": default_fastkperiod,
        #    "fastlimit": default_fastlimit,
        #    "fastperiod": default_fastperiod,
        #    "matype": default_matype,
        #    "maximum": default_maximum,
        #    "ndevdn": default_ndevdn,
        #    "ndevup": default_ndevup,
        #    "outputsize": default_outputsize,
        #    "slowlimit": default_slowlimit,
        #    "signalperiod": default_signalperiod,
        #    "slowperiod": default_slowperiod,
        #    "slowdmatype": default_slowdmatype,
        #    "slowdperiod": default_slowdperiod,
        #    "slowkmatype": default_slowkmatype,
        #    "slowkperiod": default_slowkperiod,
        #    "timeperiod1": default_timeperiod1,
        #    "timeperiod2": default_timeperiod2,
        #    "timeperiod3": default_timeperiod3,
        #}

        self.functions_defs = {"company":           (("symbol", "r", None)),
                               "dividend":          (("symbol", "r", None),
                                                     ("range", ("next", "1yr", "2yr", "5Yr", "9mo", "6mo", "3mo"))
                                                    ),
                               "balance-sheet":     (("symbol", "r", None),
                                                     ("period", "q", ("annual", "quarter")),
                                                     ("last", "q", (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
                                                    ),
                               "cash-flow":         (("symbol", "r", None),
                                                     ("period", "q", ("annual", "quarter")),
                                                     ("last", "q", (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
                                                    ),
                               "income":            (("symbol", "r", None),
                                                     ("period", "q", ("annual", "quarter")),
                                                     ("last", "q", (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
                                                    ),

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

            if sandbox:
                url = f"https://sandbox.iexapis.com/stock/{str_vars}"
            else:
                url = f"https://cloud.iexapis.com/stock/{str_vars}"

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


