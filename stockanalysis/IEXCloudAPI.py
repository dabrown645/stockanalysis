class IEXCloud(object):
    """This class can make any call to AlphaVantage api"""

    def __init__(self, token, sandbox=False):
        super(IEXCloud, self).__init__()
        self.token = token
        self.sandbox = sandbox
        if self.sandbox:
            self.baseurl = 'https://sandbox.iexapis.com/stable/stock'
        else:
            self.baseurl = 'https://cloud.iexapis.com/stable/stock'


        self.functions_defs = {"company":           (("symbol", "r", None,),),
                               "dividends":         (("symbol", "r", None,),
                                                     ("range", "q", ("next", "1y", "2y", "5y", "ytd", "6m", "3m", "1m",),)
                                                    ),
                               "balance_sheet":     (("symbol", "r", None,),
                                                     ("period", "q", ("annual", "quarter",),),
                                                     ("last", "q", (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),)
                                                    ),
                               "cash_flow":         (("symbol", "r", None,),
                                                     ("period", "q", ("annual", "quarter",)),
                                                     ("last", "q", (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,),)
                                                    ),
                               "income":            (("symbol", "r", None,),
                                                     ("period", "q", ("annual", "quarter",),),
                                                     ("last", "q", (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,),)
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

            arg_list = []
            for tuple in self.functions_defs[function_name]:
                #print(f'tuple: {tuple}')
                arg_list.append(tuple[0])
            #print(f'arg_list: {arg_list}')
            arg_list = set(arg_list)

            args = set(params.keys())

            #print('*'*20)
            #print(f'arg_list: {arg_list}')
            #print(f'args: {args}')
            if args.issubset(arg_list):
                pass
            else:
                raise ValueError("function %s needs the following arguments: %s.\nGot: %s.\nDefaults: %s" % (
                function_name, arg_list, args, self.defaults))

            bind_vars = {
                "apikey": self.token,
                "function": function_name
            }

            #print(f'params: {params}')
            #print(f'bind_vars: {bind_vars}')
            bind_vars.update(params)
            #print(f'bind_vars: {bind_vars}')

            str = ''
            seperator = '?'
            #print(f'--- for loop ---')
            for item in self.functions_defs[function_name]:
                #print(f'item: {item}')
                #print(f'bind_vars: {bind_vars}')
                if item[0] in bind_vars:
                    #print(f'\titem[1]: {item[1]}')
                    if item[1] == "r":
                        #print(f'\t\t{item[1]}')
                        #print(f'\t\tbind_vrs[item[0]]: {bind_vars[item[0]]}')
                        #print(f'\t\titem[2]: {item[2]}')
                        str = f'{str}/{bind_vars[item[0]]}/{function_name.replace("_", "-")}'
                    elif item[1] == "p":
                        #print(f'\t\t{item[1]}')
                        #print(f'\t\tbind_vrs[item[0]]: {bind_vars[item[0]]}')
                        #print(f'\t\titem[2]: {item[2]}')
                        if bind_vars[item[0]] in item[2]:
                            #print(f'\t\t\tFound in item[2]')
                            #print(f'\t\t\tbind_vrs[item[0]]: {bind_vars[item[0]]}')
                            #print(f'\t\t\titem[2]: {item[2]}')
                            str = f'{str}/{bind_vars[item[0]]}'
                        else:
                            #print(f'\t\t\tNOT Found in item[2]')
                            #print(f'\t\t\tbind_vrs[item[0]]: {bind_vars[item[0]]}')
                            #print(f'\t\t\titem[2]: {item[2]}')
                            raise ValueError(f"function ({function_name}/{item[0]}) has has an invalid value {bind_vars[item[0]]}")
                    elif item[1] == 'q':
                        #print(f'\t\t{item[1]}')
                        #print(f'\t\tbind_vrs[item[0]]: {bind_vars[item[0]]}')
                        #print(f'\t\titem[2]: {item[2]}')
                        if bind_vars[item[0]] in item[2]:
                            #print(f'\t\t\tFound in item[2]')
                            #print(f'\t\t\tbind_vrs[item[0]]: {bind_vars[item[0]]}')
                            #print(f'\t\t\titem[2]: {item[2]}')
                            str = f'{str}{seperator}{item[0]}={bind_vars[item[0]]}'
                            if seperator == "?":
                                seperator = '&'
                        else:
                            #print(f'\t\t\tNOT Found in item[2]')
                            #print(f'\t\t\tbind_vrs[item[0]]: {bind_vars[item[0]]}')
                            #print(f'\t\t\titem[2]: {item[2]}')
                            raise ValueError(f"function {function_name}/{item[0]} has has an invalid value {bind_vars[item[0]]}")
                    else:
                        raise ValueError(f"function {function_name}/{item[0]} has has an invalid type (second entry in tuple")
                #else:
                #    print(f'item[0] ({item[0]} not in bind_vars')
                #    raise ValueError(f"function {function_name/item[0]} has has an invalid parameter value (third entry in tuple")

            url = f'{self.baseurl}{str}{seperator}{self.token}'
            #print(f'url: {self.baseurl}{str}{seperator}{self.token}')

            data = requests.get(url)
            return data.json()

        return __get

    def __getattr__(self, k):
        """If the attribute is not found in the the object and if is present in function definition. Create the function for the api call and return it"""
        defs = object.__getattribute__(self, "functions_defs")
        if k in defs:
            return self._get(k)


