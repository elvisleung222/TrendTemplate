import yfinance as yf
import re
import xlsxwriter
import json
import sys
from datetime import datetime
from module.pivot_zone import pivot_zone_validator

try:
    home_dir = sys.argv[1]
except Exception as e:
    print("Please provide home directory as 1st input option")
try:
    stocks_file_name = sys.argv[2]
except Exception as e:
    print("Please provide stock file name as 2nd input option")

stocks_file = open(home_dir + stocks_file_name, "r")
stocks_list = json.loads(stocks_file.read())
stocks_file.close()

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


def validate(code):
    today = datetime.today().date()
    ticker = yf.Ticker(codify(code))
    history = ticker.history(period='1y')
    close = history['Close'][-1]
    week_low_52 = history['Low'].min()
    week_high_52 = history['High'].max()
    ma_50 = history['Close'][-50:].mean()
    ma_150 = history['Close'][-150:].mean()
    ma_200 = history['Close'][-200:].mean()
    ma_200_series = history['Close'].rolling(window=200).mean().dropna()[-20:]
    grade = 'C'
    if len(ma_200_series) > 1:
        ma_200_slope = (ma_200_series[-1] - ma_200_series[1]) / len(ma_200_series)
    else:
        ma_200_slope = 1

    conditions = [
        close > ma_150 and close > ma_200,
        ma_150 > ma_200,
        ma_200_slope > 0,
        ma_50 > ma_150 and ma_50 > ma_200,
        close > ma_50,
        close >= 1.3 * week_low_52,
        close >= 0.75 * week_high_52,
        abs((history.index.max().date() - today).days) <= 7  # no trading data for more than 7 days
    ]

    if all(conditions):
        info = ticker.get_info()

        # Grading (Stronger version of minimal trend template)
        if close >= 2 * week_low_52 and close >= 0.85 * week_high_52:
            grade = 'B'

        if close >= 3 * week_low_52 and close >= 0.95 * week_high_52:
            grade = 'A'

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
            'grade': grade,
            'pivot_zone': pivot_zone_validator(history),
            'as_of': str(history.index.max().date())
        }
        if info['marketCap'] is not None and info['volume'] is not None:
            result.append(output)
            return True, output
    return False, None


start = datetime.now()
data = {"data": []}
for stock in stocks_list:
    try:
        validated, output = validate(stock)
        print(str(datetime.now()) + ': ' + stock)
        if validated:
            data["data"].append(output)
    except Exception as e:
        print(e)
print('Start time\t: ' + str(start))
print('End time\t: ' + str(datetime.now()))
fo1 = open(home_dir + 'static/Trend-Template-Result-' + stocks_file_name + '.json', 'w+')
fo1.write(json.dumps(data))
fo1.close()
fo2 = open(home_dir + 'history/Trend-Template-Result-' + stocks_file_name + '-' + str(start.date()) + '.json', 'w+')
fo2.write(json.dumps(data))
fo2.close()

# Export to excel
# fields are same as output object
headers = {
    'code': 'Code',
    'name': 'Name',
    'market_capital': 'Market Cap',
    'volume': 'Volume',
    'close': 'Close Price',
    'week_low_52': '52 Weeks Low',
    'week_high_52': '52 Weeks High',
    'ma_50': '50 MA',
    'ma_150': '150 MA',
    'ma_200': '200 MA',
    'ma_200_slope': 'Slope of 200 MA',
    'grade': 'Grade',
    'pivot_zone': 'Pivot Zone',
    'as_of': 'Retrieved at',
}

create_xlsx_file(home_dir + 'history/Trend-Template-Result-' + stocks_file_name + '-' + str(start.date()) + '.xlsx',
                 headers, result)
print("finished.")
