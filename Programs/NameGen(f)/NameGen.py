#  Copyright (c) 2022. luz5020
#  Approved for use in Open Source Projects

# Move Resizing to ext operation
import random

import pandas as pd


def namegen():
    col_list = ["year", "name", "percent", "sex"]
    df = pd.read_csv("Names_Short_F.csv", usecols=col_list)
    # for x in df.index:
        # if df.loc[x, "yr"] < 2010:
        #     df.drop(x, inplace=True)
    dl = df['name'].tolist()
    n = random.randint(0, len(dl))
    # print(dl[n])
    return dl[n]
