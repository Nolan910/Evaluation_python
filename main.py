import pandas as pd


cinemas= pd.read_csv("./data/cinemas.csv", sep=';')
cinemas_df = pd.DatafFrame(cinemas)

print(cinemas_df)