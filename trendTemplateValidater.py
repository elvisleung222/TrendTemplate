import yfinance as yf
from datetime import datetime
import re
import xlsxwriter

stocks = [
    '4338',
    '4332',
    '4336',
    '1211',
]

result = []


def create_xlsx_file(file_path: str, headers: dict, items: list):
    with xlsxwriter.Workbook(file_path) as workbook:
        worksheet = workbook.add_worksheet()
        worksheet.write_row(row=0, col=0, data=headers.values())
        header_keys = list(headers.keys())
        for index, item in enumerate(items):
            row = map(lambda field_id: item.get(field_id, ''), header_keys)
            worksheet.write_row(row=index + 1, col=0, data=row)


def codify(number):
    def is_digits(x):
        return not (re.search(r'([0-9]*)', x).group() == '')

    if is_digits(number):
        return str(number) + '.HK'
    else:
        return number


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

    if all(conditions):
        info = ticker.get_info()

        if info['tradeable'] is not True:
            return False, None

        output = {
            'code': code,
            'name': info['longName'],
            'market_capital': info['marketCap'],
            'volume': info['volume'],
            'close': '{:.3f}'.format(close),
            'week_low_52': '{:.3f}'.format(week_low_52),
            'week_high_52': '{:.3f}'.format(week_high_52),
            'ma_50': '{:.3f}'.format(ma_50),
            'ma_150': '{:.3f}'.format(ma_150),
            'ma_200': '{:.3f}'.format(ma_200),
            'ma_200_slope': '{:.3f}'.format(ma_200_slope),
            'rsi_14': '{:.3f}'.format(rsi_14),
            'as_of': str(history.index.max().date())
        }

        result.append(output)
        return True, output
    return False, None


start = datetime.now()
fo = open('Trend-Template-Result-' + str(start.date()) + '.json', 'ab+')
for stock in stocks:
    try:
        validated, output = validate(stock)
        print(str(datetime.now()) + ': ' + stock)
        if validated:
            # fo.write(stock.encode())
            fo.write(str(output).encode())
            fo.write(',\n'.encode())
    except Exception as e:
        print(e)
print('Start time\t: ' + str(start))
print('End time\t: ' + str(datetime.now()))
fo.close()

# Export to excel
headers = {
    'code': 'Code',
    'name': 'Name',
    'market_capital': 'Market Cap',
    'volume': 'Volume',
    'close': 'Close Price',
    # 'week_low_52': '52 Weeks Low',
    # 'week_high_52': '52 Weeks High',
    # 'ma_50': '50 MA',
    # 'ma_150': '150 MA',
    # 'ma_200': '200 MA',
    'ma_200_slope': 'Slope of 200 MA',
    'rsi_14': 'RSI',
    'as_of': 'Retrieved at',
}

create_xlsx_file('Trend-Template-Result-' + str(start.date()) + '.xlsx', headers, result)
