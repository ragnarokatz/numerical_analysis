import timedelta

import pandas as pd
import numpy as np


def generate_fundnav_table():
    rnds = np.random.rand(3,4)
    df = pd.DataFrame(rnds, columns=list('abcd'))
    return df


def generate_date_table():
    dr = pd.date_range('1970-01-01', periods=1000)
    for n in range(1, 10):
        ts = dr - timedelta(years=n)

    return df(dr, columns='trade_date',)


df = generate_fundnav_table()
dates = generate_date_table()
df.join(dates, 
