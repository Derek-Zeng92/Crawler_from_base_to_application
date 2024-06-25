import pandas as pd

df = pd.read_csv("03_csv.csv", sep="|",  header=None)
df.to_excel("abc.xlsx")


