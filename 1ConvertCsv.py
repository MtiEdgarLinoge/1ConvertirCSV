#Libreria a usar; pseudomimo: pd
import pandas as pd

#Importa el archivo csv a uan variable df
df=pd.read_csv("Sistemas_Operativos_Gpo_B.csv")

#Imprime archivo df, 5 son  las primeras 5 filas
print(df.head(5))

#Imprime  la información del archivo csv
#--print(df.info())

#Se manda archivo a xls por columnas
df.to_excel('SO.xlsx', index=False)
