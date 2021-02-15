from datetime import datetime
from enum import Enum
from typing import Dict, List, Union
from urllib.parse import urljoin
from requests import get
from .models import Interval, TimeRange


API_URL = 'https://query1.finance.yahoo.com/v8/finance/chart/'


def get_quotes(symbol: str,
               interval: Union[Interval, str] = Interval.DAY,
               time_range: Union[TimeRange, str] = TimeRange.MONTH,
               include_after_market: bool = True) -> List[Dict]:
    url = urljoin(API_URL, symbol)
    response = get(url, params={'interval': enum_str(interval),
                                'range': enum_str(time_range),
                                'includePrePost': include_after_market}).json()
    error = response['chart']['error']
    if error is not None:
        raise Exception(error['description'])
    data = parse_response(response)
    return data


def enum_str(value: Union[Enum, str]):
    return value.value if isinstance(value, Enum) else value


def parse_response(response) -> List[Dict]:
    timestamps = response['chart']['result'][0]['timestamp']
    quotes = response['chart']['result'][0]['indicators']['quote'][0]
    return [{'timestamp': timestamp,
             'date': datetime.fromtimestamp(timestamp).isoformat(),
             **{name: quotes[index] for name, quotes in quotes.items()}}
            for index, timestamp in enumerate(timestamps)]
