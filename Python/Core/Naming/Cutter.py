import pandas as pd

col_list = ["yr", "sex", "FirstForename", "number", "rank", "position"]
df = pd.read_csv("Names.csv", usecols=col_list)
for x in df.index:
    if df.loc[x, "yr"] < 2010:
        df.drop(x, inplace=True)
df.to_csv(r'C:\Users\lucaf\PycharmProjects\Hello-World\Python\Core\Naming\Names_Short.csv', index=False, header=True)
