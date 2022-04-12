# Move Resizing to ext operation
import random

import pandas as pd


def namegen():
    col_list = ["year", "name", "percent", "sex"]
    df = pd.read_csv("Names_Short_M.csv", usecols=col_list)
    for x in df.index:
        if df.loc[x, "year"] < 2010:
            df.drop(x, inplace=True)
    dl = df['name'].tolist()
    n = random.randint(0, len(dl))
    # print(dl[n])
    return dl[n]
