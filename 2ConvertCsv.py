#Libreria a usar para hacer la conversion de CSV a Excel por columnas
import pandas as pd

#Importa el archivo csv a una variable:df (abreviatura de dataframe)
df=pd.read_csv('Gestión_Desarrollo_Soft.csv')

#Imprime informacion del data frame o archivo csv
print(df.info())

#Imprime las primeras 6 filas del df
#print(df.head(6))

#Con esta instruccion se convierte a archivo excel (xlxs)
df.to_excel('GestDesSof.xlsx',index=False)