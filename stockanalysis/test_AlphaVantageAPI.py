import unittest
import AlphaVantageAPI as api

#alpha = api.AlphaVantage(api_key="&apikey=BXCLSC7GAHP5UGGO", default_datatype="json")
#ticker = "IBM"



class AlphaVantageAPI_test(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        import json
        with open('config.json') as cfg:
            config = json.load(cfg)
        api_key=f'&apikey={config["alphaVantage"]}'
        self.alpha = api.AlphaVantage(api_key=api_key, default_datatype="json")
        self.ticker = config["ticker"]

    ### STOCKS
    #print(f'available functions: {alpha.get_available_functions()}')

    def test_TIME_SERIES_INTRADAY(self):
        #"TIME_SERIES_INTRADAY": ("symbol", "interval", "outputsize", "datatype"),
        target = 'Time Series (60min)'
        results = self.alpha.TIME_SERIES_INTRADAY(symbol=self.ticker, interval="60min")
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_TIME_SERIES_DAILY(self):
        #"TIME_SERIES_DAILY": ("symbol", "outputsize", "datatype"),
        target = 'Time Series (Daily)'
        results = self.alpha.TIME_SERIES_DAILY(symbol=self.ticker)
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_TIME_SERIES_DAILY_ADJUSTED(self):
        #"TIME_SERIES_DAILY_ADJUSTED": ("symbol", "outputsize", "datatype"),
        target = 'Time Series (Daily)'
        results = self.alpha.TIME_SERIES_DAILY_ADJUSTED(symbol=self.ticker)
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_TIME_SERIES_WEEKLY(self):
        #"TIME_SERIES_WEEKLY": ("symbol", "outputsize", "datatype"),
        target = 'Weekly Time Series'
        results = self.alpha.TIME_SERIES_WEEKLY(symbol=self.ticker)
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_TIME_SERIES_WEEKLY_ADJUSTED(self):
        #"TIME_SERIES_WEEKLY_ADJUSTED": ("symbol", "outputsize", "datatype"),
        target = 'Weekly Adjusted Time Series'
        results = self.alpha.TIME_SERIES_WEEKLY_ADJUSTED(symbol=self.ticker)
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_TIME_SERIES_MONTHLY(self):
        #"TIME_SERIES_MONTHLY": ("symbol", "outputsize", "datatype"),
        target = 'Monthly Time Series'
        results = self.alpha.TIME_SERIES_MONTHLY(symbol=self.ticker)
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_TIME_SERIES_MONTHLY_ADJUSTED(self):
        #"TIME_SERIES_MONTHLY_ADJUSTED": ("symbol", "outputsize" "datatype"),
        target = 'Monthly Adjusted Time Series'
        results = self.alpha.TIME_SERIES_MONTHLY_ADJUSTED(symbol=self.ticker)
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_GLOBAL_QUOTE(self):
        #"GLOBAL_QUOTE": ("symbol", "datatype"),
        target = 'Global Quote'
        results = self.alpha.GLOBAL_QUOTE(symbol=self.ticker)
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_SYMBOL_SEARCH(self):
        #"GLOBAL_QUOTE": ("symbol", "datatype"),
        target = 'bestMatches'
        results = self.alpha.SYMBOL_SEARCH(keywords=self.ticker)
        self.assertIn(target, results.keys(), f'{target} not in results')

    #### FOREX

    def test_FX_INTRADAY(self):
        #"FX_INTRADAY": ("from_symbol", "to_symbol", "interval", "outputsize", "datatype"),
        target = 'Time Series FX (60min)'
        results = self.alpha.FX_INTRADAY(from_symbol="EUR", to_symbol="USD", interval="60min)")
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_FX_DAILY(self):
        #"FX_DAILY": ("from_symbol", "to_symbol", "outputsize", "datatype"),
        target = 'Time Series FX (Daily)'
        results = self.alpha.FX_DAILY(from_symbol="EUR", to_symbol="USD")
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_FX_WEEKLY(self):
        #"FX_WEEKLY": ("from_symbol", "to_symbol", "outputsize", "datatype"),
        target = 'Time Series FX (Weekly)'
        results = self.alpha.FX_WEEKLY(from_symbol="EUR", to_symbol="USD")
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_FX_MONTHLY(self):
        #"FX_MONTHLY": ("from_symbol", "to_symbol", "outputsize", "datatype"),
        target = 'Time Series FX (Monthly)'
        results = self.alpha.FX_MONTHLY(from_symbol="EUR", to_symbol="USD")
        self.assertIn(target, results.keys(), f'{target} not in results')

    ### CRYPTO

    def test_CURRENCY_EXCHANGE_RTE(self):
        #"CURRENCY_EXCHANGE_RATE": ("from_currency", "to_currency"),
        target = 'Realtime Currency Exchange Rate'
        results = self.alpha.CURRENCY_EXCHANGE_RATE(from_currency="BTC", to_currency="USD")
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_DIGITAL_CURRENCY_DAILY(self):
        ##"DIGITAL_CURRENCY_DAILY": ("symbol", "market", "datatype"),
        target = 'Time Series (Digital Currency Daily)'
        results = self.alpha.DIGITAL_CURRENCY_DAILY(symbol="BTC", market="CNY")
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_DIGITAL_CURRENCY_WEEKLY(self):
        ##"DIGITAL_CURRENCY_WEEKLY": ("symbol", "market", "datatype"),
        target = 'Time Series (Digital Currency Weekly)'
        results = self.alpha.DIGITAL_CURRENCY_WEEKLY(symbol="BTC", market="CNY")
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_DIGITAL_CURRENCY_MONTHLY(self):
        ##"DIGITAL_CURRENCY_MONTHLY": ("symbol", "market", "datatype"),
        target = 'Time Series (Digital Currency Monthly)'
        results = self.alpha.DIGITAL_CURRENCY_MONTHLY(symbol="BTC", market="CNY")
        self.assertIn(target, results.keys(), f'{target} not in results')

    ##### Technical Indicators

    def test_AD(self):
        #"AD": ("symbol", "interval", "datatype"),
        target = 'Technical Analysis: Chaikin A/D'
        results = self.alpha.AD(symbol=self.ticker, interval="monthly")
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_ADOSC(self):
        #"ADOSC": ("symbol", "interval", "fastperiod", "slowperiod", "datatype"),
        target = 'Technical Analysis: ADOSC'
        results = self.alpha.ADOSC(symbol=self.ticker, interval="monthly", fastperiod=3, slowperiod=10)
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_ADX(self):
        #"ADX": ("symbol", "interval", "time_period", "datatype"),
        target = 'Technical Analysis: ADX'
        results = self.alpha.ADX(symbol=self.ticker, interval="monthly", time_period=60)
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_ADXR(self):
        #"ADXR": ("symbol", "interval", "time_period", "datatype"),
        target = 'Technical Analysis: ADXR'
        results = self.alpha.ADXR(symbol=self.ticker, interval="monthly", time_period=60)
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_APO(self):
        #"APO": ("symbol", "interval", "series_type", "fastperiod", "slowperiod", "matype", "datatype"),
        target = 'Technical Analysis: APO'
        results = self.alpha.APO(symbol=self.ticker, interval="monthly", series_type="closed")
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_AROON(self):
        #"AROON": ("symbol", "interval", "time_period", "datatype"),
        target = 'Technical Analysis: AROON'
        results = self.alpha.AROON(symbol=self.ticker, interval="monthly", time_period=60)
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_AROONOSC(self):
        #"AROONOSC": ("symbol", "interval", "time_period", "datatype"),
        target = 'Technical Analysis: AROONOSC'
        results = self.alpha.AROONOSC(symbol=self.ticker, interval="monthly", time_period=60)
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_ATR(self):
        #"ATR": ("symbol", "interval", "time_period", "datatype"),
        target = 'Technical Analysis: ATR'
        results = self.alpha.ATR(symbol=self.ticker, interval="monthly", time_period=60)
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_BBANDS(self):
        #"BBANDS": ("symbol", "interval", "time_period", "series_type", "nbdevup", "nbdevdn",  "matype", "datatype"),
        target = 'Technical Analysis: BBANDS'
        results = self.alpha.BBANDS(symbol=self.ticker, interval="monthly", time_period=60, series_type="closed", nbdevup=2, nbdevdn=2, matype=0)
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_BOP(self):
        #"BOP": ("symbol", "interval", "datatype"),
        target = 'Technical Analysis: BOP'
        results = self.alpha.BOP(symbol=self.ticker, interval="monthly")
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_CCI(self):
        #"CCI": ("symbol", "interval", "time_period", "datatype"),
        target = 'Technical Analysis: CCI'
        results = self.alpha.CCI(symbol=self.ticker, interval="monthly", time_period=60)
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_CMQ(self):
        #"CMO": ("symbol", "interval", "time_period", "series_type", "datatype"),
        target = 'Technical Analysis: CMO'
        results = self.alpha.CMO(symbol=self.ticker, interval="monthly", time_period=60, series_type="close")
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_DEMA(self):
        #"DEMA": ("symbol", "interval", "time_period", "series_type", "datatype"),
        target = 'Technical Analysis: DEMA'
        results = self.alpha.DEMA(symbol=self.ticker, interval="monthly", time_period=60, series_type="closed")
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_DX(self):
        #"DX": ("symbol", "interval", "time_period", "datatype"),
        target = 'Technical Analysis: DX'
        results = self.alpha.DX(symbol=self.ticker, interval="monthly", time_period=60)
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_EMA(self):
        #"EMA": ("symbol", "interval", "time_period", "series_type", "datatype"),
        target = 'Technical Analysis: EMA'
        results = self.alpha.EMA(symbol=self.ticker, interval="monthly", time_period=60, series_type="closed")
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_HT_DCPERIOD(self):
        #"HT_DCPERIOD": ("symbol", "interval", "series_type", "datatype"),
        target = 'Technical Analysis: HT_DCPERIOD'
        results = self.alpha.HT_DCPERIOD(symbol=self.ticker, interval="monthly", series_type="closed")
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_HT_DCPHASE(self):
        #"HT_DCPHASE": ("symbol", "interval", "series_type", "datatype"),
        target = 'Technical Analysis: HT_DCPHASE'
        results = self.alpha.HT_DCPHASE(symbol=self.ticker, interval="monthly", series_type="closed")
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_HT_PHASOR(self):
        #"HT_PHASOR": ("symbol", "interval", "series_type", "datatype"),
        target = 'Technical Analysis: HT_PHASOR'
        results = self.alpha.HT_PHASOR(symbol=self.ticker, interval="monthly", series_type="closed")
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_HT_TRENDLINE(self):
        #"HT_TRENDLINE": ("symbol", "interval", "series_type", "datatype"),
        target = 'Technical Analysis: HT_TRENDLINE'
        results = self.alpha.HT_TRENDLINE(symbol=self.ticker, interval="monthly", series_type="closed")
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_HT_TRENDMODE(self):
        #"HT_TRENDMODE": ("symbol", "interval", "series_type", "datatype"),
        target = 'Technical Analysis: HT_TRENDMODE'
        results = self.alpha.HT_TRENDMODE(symbol=self.ticker, interval="monthly", series_type="closed")
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_HT_SINE(self):
        #"HT_SINE": ("symbol", "interval", "series_type", "datatype"),
        target = 'Technical Analysis: HT_SINE'
        results = self.alpha.HT_SINE(symbol=self.ticker, interval="monthly", series_type="closed")
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_KAMA(self):
        #"KAMA": ("symbol", "interval", "time_period", "series_type", "datatype"),
        target = 'Technical Analysis: KAMA'
        results = self.alpha.KAMA(symbol=self.ticker, interval="monthly", time_period=60, series_type="closed")
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_MACD(self):
        #"MACD": ("symbol", "interval", "series_type", "fastperiod", "slowperiod", "signalperiod", "datatype"),
        target = 'Technical Analysis: MACD'
        results = self.alpha.MACD(symbol=self.ticker, interval="monthly", series_type="closed", fastperiod=12, slowperiod=26, signalperiod=9)
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_MACDEXT(self):
        #"MACDEXT": ("symbol", "interval", "series_type", "fastperiod", "slowperiod", "signalperiod", "datatype"),
        target = 'Technical Analysis: MACDEXT'
        results = self.alpha.MACDEXT(symbol=self.ticker, interval="monthly", series_type="closed", fastperiod=12, slowperiod=26, signalperiod=3)
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_MAMA(self):
        #"MAMA": ("symbol", "interval", "series_type", "fastlimit", "slowlimit", "datatype"),
        target = 'Technical Analysis: MAMA'
        results = self.alpha.MAMA(symbol=self.ticker, interval="monthly", series_type="close", fastlimit=0.01, slowlimit=0.01)
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_MFI(self):
        #"MFI": ("symbol", "interval", "time_period", "datatype"),
        target = 'Technical Analysis: MFI'
        results = self.alpha.MFI(symbol=self.ticker, interval="monthly", time_period=60)
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_MIDPOINT(self):
        #"MIDPOINT": ("symbol", "interval", "time_period", "series_type", "datatype"),
        target = 'Technical Analysis: MIDPOINT'
        results = self.alpha.MIDPOINT(symbol=self.ticker, interval="monthly", time_period=60, series_type="closed")
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_MIDPRICE(self):
        #"MIDPRICE": ("symbol", "interval", "time_period", "datatype"),
        target = 'Technical Analysis: MIDPRICE'
        results = self.alpha.MIDPRICE(symbol=self.ticker, interval="monthly", time_period=60)
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_MINUS_DI(self):
        #"MINUS_DI": ("symbol", "interval", "time_period", "datatype"),
        target = 'Technical Analysis: MINUS_DI'
        results = self.alpha.MINUS_DI(symbol=self.ticker, interval="monthly", time_period=60)
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_MINUS_DM(self):
        #"MINUS_DM": ("symbol", "interval", "time_period", "datatype"),
        target = 'Technical Analysis: MINUS_DM'
        results = self.alpha.MINUS_DM(symbol=self.ticker, interval="monthly", time_period=60)
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_MOM(self):
        #"MOM": ("symbol", "interval", "time_period", "series_type", "datatype"),
        target = 'Technical Analysis: MOM'
        results = self.alpha.MOM(symbol=self.ticker, interval="monthly", time_period=60, series_type="closed")
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_NATR(self):
        #"NATR": ("symbol", "interval", "time_period", "datatype"),
        target = 'Technical Analysis: NATR'
        results = self.alpha.NATR(symbol=self.ticker, interval="monthly", time_period=60)
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_OBV(self):
        #"OBV": ("symbol", "interval", "datatype"),
        target = 'Technical Analysis: OBV'
        results = self.alpha.OBV(symbol=self.ticker, interval="monthly")
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_PLUS_DI(self):
        #"PLUS_DI": ("symbol", "interval", "time_period", "datatype"),
        target = 'Technical Analysis: PLUS_DI'
        results = self.alpha.PLUS_DI(symbol=self.ticker, interval="monthly", time_period=60)
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_PLUS_DM(self):
        #"PLUS_DM": ("symbol", "interval", "time_period", "datatype"),
        target = 'Technical Analysis: PLUS_DM'
        results = self.alpha.PLUS_DM(symbol=self.ticker, interval="monthly", time_period=60)
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_PPO(self):
        #"PPO": ("symbol", "interval", "series_type", "fastperiod", "slowperiod", "matype", "datatype"),
        target = 'Technical Analysis: PPO'
        results = self.alpha.PPO(symbol=self.ticker, interval="monthly", series_type="closed", fastperiod=12, slowperiod=26, matype=0)
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_ROC(self):
        #"ROC": ("symbol", "interval", "time_period", "series_type", "datatype"),
        target = 'Technical Analysis: ROC'
        results = self.alpha.ROC(symbol=self.ticker, interval="monthly", time_period=60, series_type="close")
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_ROCR(self):
        #"ROCR": ("symbol", "interval", "time_period", "series_type", "datatype"),
        target = 'Technical Analysis: ROCR'
        results = self.alpha.ROCR(symbol=self.ticker, interval="monthly", time_period=60, series_type="close")
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_RSI(self):
        # "RSI": ("symbol", "interval", "time_period", "series_type", "datatype"),
        target = 'Technical Analysis: RSI'
        results = self.alpha.RSI(symbol=self.ticker, interval="monthly", time_period=60, series_type="closed")
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_SAR(self):
        #"SAR": ("symbol", "interval", "acceleration", "maximum", "datatype"),
        target = 'Technical Analysis: SAR'
        results = self.alpha.SAR(symbol=self.ticker, interval="monthly", acceleration=0.01, maximum=0.20)
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_STOCH(self):
        #"STOCH": ("symbol", "interval", "fastkperiod", "slowkperiod", "slowdperiod", "slowkmatype", "slowdmatype", "datatype"),
        target = 'Technical Analysis: STOCH'
        results = self.alpha.STOCH(symbol=self.ticker, interval="monthly", fastkperiod=5, slowkperiod=3, slowdperiod=3, slowkmatype=0)
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_STOCHF(self):
        #"STOCHF": ("symbol", "interval", "fastkperiod", "fastdperiod", "fastdmatype", "datatype"),
        target = 'Technical Analysis: STOCHF'
        results = self.alpha.STOCHF(symbol=self.ticker, interval="monthly", fastkperiod=5, fastdperiod=3, fastdmatype=0)
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_STOCHRSI(self):
        # "STOCHRSI": ("symbol", "interval", "time_period", "series_type", "fastkperiod", "fastdperiod", "fastdmatype", "datatype"),
        target = 'Technical Analysis: STOCHRSI'
        results = self.alpha.STOCHRSI(symbol=self.ticker, interval="monthly", time_period=60, series_type="close", fastkperiod=5, fastdperiod=3, fastdmatype=0)
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_SMA(self):
        #"SMA": ("symbol", "interval", "time_period", "series_type", "datatype"),
        target = 'Technical Analysis: SMA'
        results = self.alpha.SMA(symbol=self.ticker, interval="monthly", time_period=60, series_type="closed")
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_T3(self):
        #"T3": ("symbol", "interval", "time_period", "series_type", "datatype"),
        target = 'Technical Analysis: T3'
        results = self.alpha.T3(symbol=self.ticker, interval="monthly", time_period=60, series_type="close")
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_TEMA(self):
        #"TEMA": ("symbol", "interval", "time_period", "series_type", "datatype"),
        target = 'Technical Analysis: TEMA'
        results = self.alpha.TEMA(symbol=self.ticker, interval="monthly", time_period=60, series_type="closed")
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_TRANGE(self):
        #"TRANGE": ("symbol", "interval", "datatype"),
        target = 'Technical Analysis: TRANGE'
        results = self.alpha.TRANGE(symbol=self.ticker, interval="monthly")
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_TRIMA(self):
        #"TRIMA": ("symbol", "interval", "time_period", "series_type", "datatype"),
        target = 'Technical Analysis: TRIMA'
        results = self.alpha.TRIMA(symbol=self.ticker, interval="monthly", time_period=60, series_type="closed")
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_TRIX(self):
        #"TRIX": ("symbol", "interval", "time_period", "series_type", "datatype"),
        target = 'Technical Analysis: TRIX'
        results = self.alpha.TRIX(symbol=self.ticker, interval="monthly", time_period=60, series_type="close")
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_ULTOSC(self):
        #"ULTOSC": ("symbol", "interval", "timeperiod1", "timeperiod2", "timeperiod3", "datatype"),
        target = 'Technical Analysis: ULTOSC'
        results = self.alpha.ULTOSC(symbol=self.ticker, interval="monthly", timeperiod1=7, timeperiod2=14, timeperiod3=28)
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_VWAP(self):
        #"VWAP": ("symbol", "interval", "datatype"),
        target = 'Technical Analysis: VWAP'
        results = self.alpha.VWAP(symbol=self.ticker, interval="60min")
        print(f'results.keys(): {results.keys()}')
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_WILLR(self):
        # "WILLR": ("symbol", "interval", "time_period", "datatype"),
        target = 'Technical Analysis: WILLR'
        results = self.alpha.WILLR(symbol=self.ticker, interval="monthly", time_period=60)
        self.assertIn(target, results.keys(), f'{target} not in results')

    def test_WMA(self):
        #"WMA": ("symbol", "interval", "time_period", "series_type", "datatype"),
        target = 'Technical Analysis: WMA'
        results = self.alpha.WMA(symbol=self.ticker, interval="monthly", time_period=60, series_type="closed")
        self.assertIn(target, results.keys(), f'{target} not in results')


if __name__ == "__main__":
    unittest.main(verbosity=2)