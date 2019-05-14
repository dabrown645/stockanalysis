import unittest
import IEXCloudAPI as api

class IEXCloud_test(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        import json
        with open('config.json') as cfg:
            config = json.load(cfg)
        token =f'token={config["sandbox_iex"]}'
        sandbox_iex = 'Tpk_9b5136fd522b4ef8bafac263b1031c0f'
        self.iex = api.IEXCloud(token=token )
        self.ticker = 'aapl'
        print(f'token` from instance: {self.iex.api_key}')


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
        target = 'dividend'
        self.assertIn(target, results, f'{target} not found in results')
        target = 'balance-sheet'
        self.assertIn(target, results, f'{target} not found in results')
        target = 'cash-flow'
        self.assertIn(target, results, f'{target} not found in results')
        target = 'income'
        self.assertIn(target, results, f'{target} not found in results')

    def test_0_get_function_arugments(self):
        target = "company"
        results =  self.iex.get_function_arguments(target)
        self.assertIn('symbol', results, f'Needed to find symbol in the list of arguments')

    def test_1_company(self):
        target = "company"

    def test_9_add_function_definitions(self):
        self.iex.add_function_definitions("book", ("symbol", "r", None))
        target = "test"
        results = self.iex.get_function_arguments("book")
        self.assertIn('symbol', results, f'Needed to find symbol in the list of arguments')

if __name__ == "__main__":
    unittest.main(verbosity=2)