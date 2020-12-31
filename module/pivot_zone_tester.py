import yfinance as yf
from module.pivot_zone import pivot_zone_validator

histories = [
    yf.Ticker('MELI').history(start='2007-08-08', end='2007-12-08'),
    yf.Ticker('AMSC').history(start='2003-08-26', end='2003-12-27'),
    yf.Ticker('EDU').history(start='2007-01-14', end='2007-04-14'),
    yf.Ticker('NFLX').history(start='2009-07-14', end='2009-10-14')
]

for hist in histories:
    print(pivot_zone_validator(hist))
