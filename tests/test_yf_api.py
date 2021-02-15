import yf_api as yf


TICKER = 'aapl'


def test_get_quotes():
    data = yf.get_quotes(TICKER)
    assert isinstance(data, list)


def test_get_quotes_params():
    data = yf.get_quotes(TICKER, interval='1d', time_range='1m')
    assert isinstance(data, list)
