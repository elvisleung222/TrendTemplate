"""
Features to identify Pivot Zone for a buy signal

- abs(high-low) < 5%
- abs(open-close) < 3%
- volume = min(volumes in 5d)
- mean(volumes in 5d) < mean(volumes in 50d)
- (max(highs in 5d) - min(lows in 5d)) < 5%
- mean(high-low in 5d) < 3%
- ((sum(delta(close_T - close_T-1)) in 5d) / 5) < 1%
"""

# Params
length = 3
zone_height_hard = 4 / 100
zone_height_soft = 6 / 100
line_height = 1.5 / 100
price_delta = 1.5 / 100


def pivot_zone_validator(history):
    open = history['Open'][-1]
    high = history['High'][-1]
    low = history['Low'][-1]
    close = history['Close'][-1]
    volume = history['Volume'][-1]
    mean_vol_50 = history['Volume'][-50:].mean()
    mean_vol_5 = history['Volume'][-length:].mean()
    min_vol_5 = history['Volume'][-length:].min()
    max_high_5 = history['High'][-length:].max()
    min_low_5 = history['Low'][-length:].min()
    mean_high_low_5 = (sum(
        [x - y for x, y in zip(history['High'][-length:], history['Low'][-length:])]) / length) / close
    mean_delta_close_5 = (history['Close'][-length:].rolling(window=2)
                          .apply(lambda x: abs(x.iloc[1] - x.iloc[0])).dropna().mean()) / close
    delta_close_open_5 = [abs(x - y) for x, y in zip(history['Close'][-length:], history['Open'][-length:])]
    delta_high_low_5 = [abs(x - y) for x, y in zip(history['High'][-length:], history['Low'][-length:])]

    conditions = [
        (high - low) / close <= zone_height_hard,
        abs((close - open) / close) <= line_height,
        mean_vol_5 <= mean_vol_50,
        (max_high_5 - min_low_5) / close <= zone_height_soft,
        mean_high_low_5 <= zone_height_hard,
        mean_delta_close_5 <= price_delta,
        any([
            volume == min_vol_5,
            abs(close - open) == min(delta_close_open_5),
            abs(high - low) == min(delta_high_low_5)
        ])
    ]

    return all(conditions)
