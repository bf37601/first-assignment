import pandas as pd

# 1
df = pd.read_csv("./train.tsv", delimiter='\t')
# set tab as delimiter

# 2
df.columns = ['Cena',
              'Liczba pokoi',
              'Powierzchnia',
              'Piętro',
              'Lokalizacja',
              'Opis'
              ]

print(df['Cena'])
print(df[['Cena', 'Powierzchnia']])
pd.set_option('max_colwidth',
              max(df['Opis'].str.len()))

print(df)

# 3

df.info()
