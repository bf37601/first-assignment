import pandas as pd

df = pd.read_csv("./train.tsv", delimiter='\t')
df.columns = ['Cena',
              'Liczba pokoi',
              'Powierzchnia',
              'Piętro',
              'Lokalizacja',
              'Opis'
              ]
# 3
description = pd.read_csv("./description.csv")

df1 = df.merge(description, how='left', left_on='Piętro', right_on='liczba')

# delete added column 'liczba' (is unnecessary) from description dataframe
# and fill NaN as empty string
df1.drop(['liczba'], axis=1, inplace=True)
df1.fillna('', inplace=True)
df1.to_csv('out2.csv', index = False)
