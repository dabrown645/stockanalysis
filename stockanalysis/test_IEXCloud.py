import unittest
import IEXCloudAPI as api
import json

class IEXCloud_test(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        import json
        with open('config.json') as cfg:
            config = json.load(cfg)
        token =f'token={config["sandbox_iex"]}'
        #print(f'token` {token}')
        self.iex = api.IEXCloud(token=token, sandbox=True )
        self.ticker = 'aapl'
        #print(f'token: from instance: {self.iex.token}')


    #def test_TIME_SERIES_INTRADAY(self):
    #    #"TIME_SERIES_INTRADAY": ("symbol", "interval", "outputsize", "datatype"),
    #    target = 'Time Series (60min)'
    #    results = self.alpha.TIME_SERIES_INTRADAY(symbol=self.ticker, interval="60min")
    #    self.assertIn(target, results.keys(), f'{target} not in results')
    def test_0_get_available_functions(self):
        results = self.iex.get_available_functions()
        self.assertEqual(len(results), 5, f'did not get enough entries {len(results)}')
        target = 'company'
        self.assertIn(target, results, f'{target} not found in results')
        target = 'dividends'
        self.assertIn(target, results, f'{target} not found in results')
        target = 'balance_sheet'
        self.assertIn(target, results, f'{target} not found in results')
        target = 'cash_flow'
        self.assertIn(target, results, f'{target} not found in results')
        target = 'income'
        self.assertIn(target, results, f'{target} not found in results')

    def test_0_get_function_arugments(self):
        # test with only 1 argument
        target = "company"
        results = self.iex.get_function_arguments(target)
        arg_list = []
        for arg in results:
            arg_list.append(arg[0])
        self.assertIn('symbol', arg_list, f'Needed to find symbol in the list of arguments')
        # test with parmeter arguments type = "p"
        target = "dividends"
        results = self.iex.get_function_arguments(target)
        arg_list = []
        for arg in results:
            arg_list.append(arg[0])
        self.assertIn('symbol', arg_list, f'Needed to find symbol in the list of arguments')
        # test with query arguments type = "q"
        target = "balance_sheet"
        results = self.iex.get_function_arguments(target)
        arg_list = []
        for arg in results:
            arg_list.append(arg[0])
        self.assertIn('symbol', arg_list, f'Needed to find symbol in the list of arguments')

    def test_1_company(self):
        results = self.iex.company(symbol=self.ticker)
        self.assertIn('symbol', results, f'Needed to find symbol in the list of arguments')

    def test_1_dividends(self):
        #results = self.iex.dividends(symbol=self.ticker)
        #self.assertIn('exDate', results[0], f'Needed to find symbol in the list of arguments')

        results = self.iex.dividends(symbol=self.ticker, range='5y')
        self.assertIn('exDate', results[0], f'Needed to find symbol in the list of arguments')

        results = self.iex.dividends(symbol=self.ticker, range='2y')
        self.assertIn('exDate', results[0], f'Needed to find symbol in the list of arguments')

        results = self.iex.dividends(symbol=self.ticker, range='1y')
        self.assertIn('exDate', results[0], f'Needed to find symbol in the list of arguments')

        results = self.iex.dividends(symbol=self.ticker, range='ytd')
        self.assertIn('exDate', results[0], f'Needed to find symbol in the list of arguments')

        results = self.iex.dividends(symbol=self.ticker, range='6m')
        self.assertIn('exDate', results[0], f'Needed to find symbol in the list of arguments')

        results = self.iex.dividends(symbol=self.ticker, range='3m')
        self.assertIn('exDate', results[0], f'Needed to find symbol in the list of arguments')

        #results = self.iex.dividends(symbol=self.ticker, range='1m')
        #self.assertIn('exDate', results[0], f'Needed to find symbol in the list of arguments')

        with self.assertRaises(ValueError):
            results = self.iex.dividends(symbol=self.ticker, range='xxxx')

    def test_1_balance_sheet(self):
        results = self.iex.balance_sheet(symbol=self.ticker, period='annual', last=1)
        self.assertIn('symbol', results, f'Needed to find symbol in the list of arguments')

        results = self.iex.balance_sheet(symbol=self.ticker, period='quarter', last=12)
        self.assertIn('symbol', results, f'Needed to find symbol in the list of arguments')

        with self.assertRaises(ValueError):
            results = self.iex.balance_sheet(symbol=self.ticker, period='annuals', last=1)

        with self.assertRaises(ValueError):
            results = self.iex.balance_sheet(symbol=self.ticker, period='annual', last=13)

        with self.assertRaises(ValueError):
            results = self.iex.balance_sheet(symbol=self.ticker, period='period', last=12)

    def test_1_cash_flow(self):
        results = self.iex.cash_flow(symbol=self.ticker, period='annual', last=1)
        self.assertIn('symbol', results, f'Needed to find symbol in the list of arguments')

        results = self.iex.cash_flow(symbol=self.ticker, period='quarter', last=12)
        self.assertIn('symbol', results, f'Needed to find symbol in the list of arguments')

        with self.assertRaises(ValueError):
            results = self.iex.cash_flow(symbol=self.ticker, period='annuals', last=1)

        with self.assertRaises(ValueError):
            results = self.iex.cash_flow(symbol=self.ticker, period='annual', last=13)

        with self.assertRaises(ValueError):
            results = self.iex.cash_flow(symbol=self.ticker, period='period', last=12)

    def test_1_income(self):
        results = self.iex.income(symbol=self.ticker, period='annual', last=1)
        self.assertIn('symbol', results, f'Needed to find symbol in the list of arguments')

        results = self.iex.income(symbol=self.ticker, period='quarter', last=12)
        self.assertIn('symbol', results, f'Needed to find symbol in the list of arguments')

        with self.assertRaises(ValueError):
            results = self.iex.income(symbol=self.ticker, period='annuals', last=1)

        with self.assertRaises(ValueError):
            results = self.iex.income(symbol=self.ticker, period='quarter', last=13)

        with self.assertRaises(ValueError):
            results = self.iex.income(symbol=self.ticker, period='period', last=12)

    def test_9_add_function_definitions(self):
        self.iex.add_function_definitions("book", ("symbol", "r", None))
        target = "test"
        results = self.iex.get_function_arguments("book")
        self.assertIn('symbol', results, f'Needed to find symbol in the list of arguments')

if __name__ == "__main__":
    unittest.main(verbosity=3)
