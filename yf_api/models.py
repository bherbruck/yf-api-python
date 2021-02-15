from enum import Enum


class Interval(Enum):
    MINUTE = '1m'
    MINUTE_15 = '15m'
    MINUTE_30 = '30m'
    HOUR = '1h'
    DAY = '1d'
    DAY_5 = '5d'
    WEEK = '1wk'
    MONTH = '1mo'
    YEAR = '1y'


class TimeRange(Enum):
    HOUR = '1h'
    DAY = '1d'
    DAY_5 = '5d'
    MONTH = '1mo'
    MONTH_3 = '3mo'
    MONTH_6 = '6mo'
    YEAR = '1y'
    YEAR_2 = '2y'
    YEAR_5 = '5y'
    YEAR_10 = '10y'
    YEAR_YTD = 'ytd'
    MAX = 'max'
