import pandas as pd
import numpy as np

# Convertir "List" a "Serie" de panda
numeros = [5,8,1,2,6]
print(numeros, type(numeros))
serie = pd.Series(numeros)
print(serie, type(serie))

print("---------------------------------------------------------------------------------------------------")

# Convertir "Diccionario" a "DataFrame" de panda
data = {
    "Nombre": ["Alejandro","Ana","Juan","Javier","Francisco"],
    "Edad":   [22,56,23,34,53],
    "Ciudad": ["Baza", "Granada", "Málaga", "Madrid", "Barcelona"]
}
print(data,type(data))

df = pd.DataFrame(data)
print(df,"\n",type(df))

print("---------------------------------------------------------------------------------------------------")

# Exportar dataFrame a csv
df.to_csv("data.csv")

# Importar dataFrame de csv
import_csv_df = pd.read_csv("data.csv",index_col=0)
print(import_csv_df)

print("---------------------------------------------------------------------------------------------------")

# Exportar dataFrame a excel
df.to_excel("example.xlsx",sheet_name='Hoja1')

# Importar dataFrame de excel
import_excel_df = pd.read_excel("example.xlsx",index_col=0)
print(import_excel_df)

print("---------------------------------------------------------------------------------------------------")

# Seleccionar una columna
nombres = df["Nombre"] # Un corchete === Serie
print(nombres, type(nombres))

# Seleccionar una o más columnas
nombresEdades = df[["Nombre","Edad"]] # Doble Corchete === dataFrame
print(nombresEdades,type(nombresEdades))

print("---------------------------------------------------------------------------------------------------")

# Seleccionar un registro
fila = df.loc[2] # Un corchete === Serie
print(fila, type(fila))

# Seleccionar varios registros
fila = df.loc[[0,2]] # Doble Corchete === dataFrame
print(fila,  type(fila))

print("---------------------------------------------------------------------------------------------------")

# Filtrar por: condicion (resultado: dataFrame)
mayoresDe23 = df[df["Edad"] > 54]
print(mayoresDe23, type(mayoresDe23))

filtro = (df["Edad"] > 20) & (df["Nombre"].str.startswith("A"))
filtrados = df[filtro]
print(filtrados, type(filtrados))

print("---------------------------------------------------------------------------------------------------")

# Filtrar por: query (resultado: dataFrame)
filtradoQuery = df.query("Edad > 25 & (Nombre == 'Ana')")
print(filtradoQuery, type(filtradoQuery))

print("---------------------------------------------------------------------------------------------------")

# Filtrar por: Función isin() de Serie (resultado: dataFrame)
filtradoIsIn = df[df["Nombre"].isin(["Alejandro","Javier","Pepe"])]
print(filtradoIsIn, type(filtradoIsIn))

print("---------------------------------------------------------------------------------------------------")

# Filtrar por: función personalizada booleana
def longitudNombreMayor5(nombre):
    return len(nombre) > 5

filtradoFuncion = df[df["Nombre"].apply(longitudNombreMayor5)]
print(filtradoFuncion, type(filtradoFuncion))

print("---------------------------------------------------------------------------------------------------")

# Filtrar por edades entre 20 y 35 años (inclusive)
edades25y35 = df[df["Edad"].between(20,35)]
print(edades25y35, type(filtradoFuncion))

print("---------------------------------------------------------------------------------------------------")

# Importamos "numpy" para tratamiento de datos
    # np.nan => NaN
    # None => None
data = {
    "Nombre": ["Alejandro", np.nan, "Juan", "Javier", "Francisco"],
    "Edad":   [np.nan, 56, 23, 34, 53],
    "Ciudad": ["Baza", "Granada", "Málaga", "Madrid", None]
}

df = pd.DataFrame(data)
print(df)

print("---------------------------------------------------------------------------------------------------")

# Rellenar los valores faltantes
df_fill = df.fillna(
    {
        "Nombre": "Usuario Anónimo",
        "Edad": df["Edad"].mean(),
        "Ciudad": "Desconocido"
    }
)
print(df_fill)

print("---------------------------------------------------------------------------------------------------")

# Eliminar las filas que tengan valores faltantes
df_sin_nan = df.dropna()
print(df_sin_nan)

print("---------------------------------------------------------------------------------------------------")

# Reemplazar valores especificos de alguna columna
df_reem = df.replace(
    {
        "Ciudad": {None : "Desconocido"}
    }
)
print(df_reem)
print("---------------------------------------------------------------------------------------------------")

# Interpolar valores
df_interpolado = df.copy()
df_interpolado["Edad"] = df["Edad"].interpolate(limit_direction="both")

print( df_interpolado )

print("---------------------------------------------------------------------------------------------------")

# Creación de un dataFrame con duplicados
data_duplicada = {
    "Nombre": ["Alejandro", np.nan, "Juan", "Javier", "Francisco","Antonio","Cristina","Alejandro"],
    "Edad":   [20, 56, 23, 34, 53, np.nan, 22, 20],
    "Ciudad": ["Baza", "Granada", "Málaga", "Madrid", None, "Alicante", "Estepona", "Baza"]
}

df_duplicado = pd.DataFrame(data_duplicada)
print(df_duplicado)

print("***********************************************")

# Eliminación de duplicados
df_sin_duplicados = df_duplicado.drop_duplicates()
print(df_sin_duplicados)

print("---------------------------------------------------------------------------------------------------")

# Renombrar columnas de un dataFrame
df_renombrado = df.rename(columns={"Nombre":"Name","Edad":"Age","Ciudad":"City"})
print(df_renombrado)

print("---------------------------------------------------------------------------------------------------")

# Ordenar un dataFrame
columnas_ordenadas = ["Ciudad","Edad","Nombre"]
df_ordenado = df[columnas_ordenadas]
print(df_ordenado)

print("---------------------------------------------------------------------------------------------------")

# Transformación de datos
def cuadrado(x):
    return x**2

df["Edad_Cuadrado"] = df["Edad"].apply(cuadrado)
print(df)

print("---------------------------------------------------------------------------------------------------")

# Agrupar datos
data = {
    "Nombre": ["Alejandro", "Pepe", "Juan", "Javier", "Francisco", "Antonio", "Cristina"],
    "Edad":   [20, 56, 23, 34, 53, 45, 22],
    "Ciudad": ["Baza", "Málaga", "Baza", "Baza", None, "Málaga", "Estepona"],
    "Puntuacion": [80,45,26,95,100,74,63]
}

df = pd.DataFrame(data)

# Agrupar datos por ciudad
grouped = df.groupby("Ciudad")
print(grouped.groups)

print("---------------------------------------------------------------------------------------------------")

# Agregar datos en un DataFrame

# Calculamos la suma de las edades y puntuaciones por ciudad

aggregated_data = grouped.aggregate(
    {
        "Edad": "mean",
        "Puntuacion": "sum"
    }
)

print(aggregated_data)

print("---------------------------------------------------------------------------------------------------")

# Definir una función de agregación personalizada
def rango(series):
    return series.max() - series.min()

aggregated_data_custom = grouped.aggregate(
    {
        "Edad": rango,
        "Puntuacion": rango
    }
)

print(aggregated_data_custom)

print("---------------------------------------------------------------------------------------------------")

# Agregar una columna al diccionario y convertir en DF

data["Categoria"] = ["A","B","A","B","A","B","A"]
df = pd.DataFrame(data)

print(df)

print("---------------------------------------------------------------------------------------------------")

# Agrupar datos por varias columnas

grouped_multi = df.groupby(["Ciudad","Categoria"])
print(grouped_multi.groups)

print("---------------------------------------------------------------------------------------------------")

# Calcular la suma de las edades y puntuaciones por Ciudad y por Categoria
aggregated_data_multi = grouped_multi.aggregate(
    {
        "Edad":"sum",
        "Puntuacion":"mean"
    }
)

print(aggregated_data_multi)

print("---------------------------------------------------------------------------------------------------")

# Agregar una columna a un dataFrame
data = {
    "Nombre": ["Juan","Ana","Luis","Laura"],
    "Edad": [25, 33, 30, 28]
}

df = pd.DataFrame(data)

df["Ciudad"] = ["Madrid","Barcelona","Madrid","Valencia"]

print(df)

print("---------------------------------------------------------------------------------------------------")

# Agregar una fila a un dataFrame
new_row = pd.Series({"Nombre": "Pedro", "Edad":45, "Ciudad":"Barcelona"})
df = pd.concat([df, new_row.to_frame().T], ignore_index=True)

print(df)

