import pandas as pd

df = pd.read_csv("07_csv.csv", sep="|",  header=None)
df.to_excel("abc.xlsx")


