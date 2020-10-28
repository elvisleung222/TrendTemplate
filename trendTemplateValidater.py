import yfinance as yf
from datetime import datetime

stocks = [
    '9998'
]


def codify(number):
    return str(number) + '.HK'


def rsi(stock, column="Close", period=14):
    # Wilder's RSI
    close = stock[column]
    delta = close.diff()
    up, down = delta.copy(), delta.copy()

    up[up < 0] = 0
    down[down > 0] = 0

    # Calculate the exponential moving averages (EWMA)
    roll_up = up.ewm(com=period - 1, adjust=False).mean()
    roll_down = down.ewm(com=period - 1, adjust=False).mean().abs()

    # Calculate RS based on exponential moving average (EWMA)
    rs = roll_up / roll_down  # relative strength =  average gain/average loss

    rsi = 100 - (100 / (1 + rs))

    return rsi


def validate(code):
    ticker = yf.Ticker(codify(code))
    history = ticker.history(period='1y')
    close = history['Close'][-1]
    week_low_52 = history['Low'].min()
    week_high_52 = history['High'].max()
    ma_50 = history['Close'][-50:].mean()
    ma_150 = history['Close'][-150:].mean()
    ma_200 = history['Close'][-200:].mean()
    ma_200_series = history['Close'].rolling(window=200).mean().dropna()[-20:]
    if len(ma_200_series) > 1:
        ma_200_slope = (ma_200_series[-1] - ma_200_series[1]) / len(ma_200_series)
    else:
        ma_200_slope = 1
    rsi_14 = rsi(history)[-1]

    conditions = [
        close > ma_150 and close > ma_200,
        ma_150 > ma_200,
        ma_200_slope > 0,
        ma_50 > ma_150 and ma_50 > ma_200,
        close > ma_50,
        close >= 1.3 * week_low_52,
        close * 1.25 >= week_high_52,
        rsi_14 > 70
    ]

    return all(conditions)


fo = open('out.txt', 'ab+')
start = datetime.now()
for stock in stocks:
    try:
        print(str(datetime.now()) + ': ' + stock)
        if validate(stock):
            fo.write(stock.encode())
            fo.write('\n'.encode())
    except Exception as e:
        print(e)
print('Start time\t: ' + str(start))
print('End time\t: ' + str(datetime.now()))
fo.close()
