import pandas as pd
df=pd.read_csv('13_RP_Comandos_básicos_de_Linux.csv')
print(df.head())
df.to_excel('Act13.xlsx')