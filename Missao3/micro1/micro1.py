import pandas as pd

df = pd.read_csv(r'C:\Users\AMANDA DUQUE\Documents\AMANDA\estacio-mundo5\Missao4\micro1\dados.csv', sep=';', engine='python')

# print("Dados completos: ")
# print(df)

# df_subset = df[['Date', 'Pulse', 'Calories']]

# print("\nSubset de dados (Data, Pulso, Calorias): ")
# print(df_subset)

# pd.set_option('display.max_rows', 9999)

# print("\nPrimeiras 3 linhas: ")
# print(df.head(3))

# print("\nUltimas 3 linhas: ")
# print(df.tail(3))


# print("\nConjunto de dados original (exibindo todas as linhas): ")
# print(df.to_string())

# print("\Informações gerais sobre o conjunto de dados: ")
# print(df.info())

total_linhas = df.shape[0]
print("Total de linhas: ", total_linhas)

total_colunas = df.shape[1]
print("Total de colunas: ", total_colunas)

dados_nulos = df.isnull().sum().sum()
print("Total de dados nulos: ", dados_nulos)

memoria_usada = df.memory_usage(deep=True).sum()
print("Memoria usada: ", memoria_usada)