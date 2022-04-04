#  Copyright (c) 2022. luz5020
#  Approved for use in Open Source Projects

# Move Resizing to ext operation
import random

import pandas as pd


def namegen():
    col_list = ["yr", "sex", "FirstForename", "number", "rank", "position"]
    df = pd.read_csv("../NameGen(m)/Names_Short_M.csv", usecols=col_list)
    for x in df.index:
        if df.loc[x, "yr"] < 2010:
            df.drop(x, inplace=True)
    dl = df['FirstForename'].tolist()
    n = random.randint(0, len(dl))
    # print(dl[n])
    return dl[n]
