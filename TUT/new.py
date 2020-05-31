import pandas as pd

df = pd.read_csv("file.csv")

print(df.loc[df['Type 1'] == 'Fire'])
