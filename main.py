import pandas as pd
import numpy as np


def generate_date_series():
    return pd.date_range('1970-01-01', periods=1000)


def generate_fundnav_table():
    rnds = np.random.rand(1000,4)
    df = pd.DataFrame(rnds, columns=list('abcd'))
    df['trade_date'] = generate_date_series()
    return df


def generate_date_table():
    end_dates = generate_date_series().to_series()
    start_dates = [end_dates - pd.DateOffset(years=n) for n in range(0, 10)]
    df = pd.concat(start_dates, axis=1)
    df = df.rename({n: f'{n}_year' for n in range(0, 10)}, axis=1)
    return df


fundnavs = generate_fundnav_table()
dates = generate_date_table()

print(fundnavs)
print(dates)
# import pdb; pdb.set_trace()

