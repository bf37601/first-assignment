import pandas as pd
#1
df = pd.read_csv("./train.tsv", delimiter = '\t')
#nalezy ustawic tabulature jako delimiter

#2
df.columns = ['Cena za m2','Liczba pokoi', 'Powierzchnia', 'Piętro','Lokalizacja','Opis']

print(df['Cena za m2'])
print(df[['Cena za m2','Powierzchnia']])
pd.set_option('max_colwidth', max(df['Opis'].str.len()))
print(df)

#3

df.info()