import pandas as pd
import numpy as np


DATA_SIZE = 4000


def generate_date_series():
    return pd.date_range('1970-01-01', periods=DATA_SIZE)


def generate_date_table():
    end_dates = generate_date_series().to_series()
    start_dates = [end_dates - pd.DateOffset(years=n, days=1) for n in range(1, 11)]
    df = pd.concat(start_dates, axis=1)
    df = df.rename({n: f'{n+1}_year' for n in range(0, 10)}, axis=1)
    return df


def generate_fundnav_table():
    rnds = np.random.rand(DATA_SIZE, 4) + 1
    df = pd.DataFrame(rnds, columns=['total_nav', 'navps', 'div_rate', 'reinv_price'])
    df['trade_date'] = generate_date_series()
    return df


dates = generate_date_table()
# print (dates.head(10))
# dates.to_csv('dates.csv')

df = generate_fundnav_table()
df = df.sort_values('trade_date', axis=0)

df['prev_reinv_price'] = df['reinv_price'].shift(1)
df['daily_return'] = df['navps'] / df['prev_reinv_price']
df['log'] = np.log(df['daily_return'])
df['log_cum'] = df['log'].cumsum()

# print (df.head(10))
# df.to_csv('df.csv')

merged = df.join(dates, on='trade_date', how='left')
joinee = df[['trade_date', 'log_cum']].set_index('trade_date')

for n in range(1, 11):
    merged = merged.join(joinee, on=f'{n}_year', how='left', rsuffix=f'_{n}_year')

for n in range(1, 11):
    merged[f'return_{n}_year'] = np.exp(merged['log_cum'] - merged[f'log_cum_{n}_year']) ** (1 / n) - 1

merged.to_csv('merged.csv')

