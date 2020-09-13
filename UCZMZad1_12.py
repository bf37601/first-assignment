import pandas as pd

df = pd.read_csv("./train.tsv", delimiter='\t')
df.columns = ['Cena',
              'Liczba pokoi',
              'Powierzchnia',
              'Piętro',
              'Lokalizacja',
              'Opis'
              ]

# 1
# multiply by 1k to give a full money ammount and round to 1 zł

dfsrednia = int(round(df['Cena'].mean() * 1000))

with open('out0.csv', 'w') as out0:
    out0.write(str(dfsrednia))

# 2
df['Cena za m2'] = round((df['Cena'] * 1000 / df['Powierzchnia']), 2)

df2 = df[(df['Liczba pokoi'] >= 3) &
         (df['Cena za m2'] < df['Cena za m2'].mean())]
df2.to_csv('out1.csv', columns=['Liczba pokoi', 'Cena', 'Cena za m2'])
