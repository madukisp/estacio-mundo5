import pandas as pd

df = pd.read_csv(r'C:\Users\AMANDA DUQUE\Documents\AMANDA\estacio-mundo5\Missao3\dados.csv', sep=';', engine='python')

print("Informações gerais: ")
df.info()

print("\nPrimeiras 5 linhas: ")
print(df.head(5))

print("\nUltimas 5 linhas: ")
print(df.tail(5))

df_copy = df.copy()

df_copy['Calories'] = df_copy['Calories'].fillna(0)

print("\nDados após substituir valores nulos na coluna 'Date': ")
print(df_copy[['Date']].tail(10))

df_copy['Date'] = df_copy['Date'].fillna('01/01/2020')
df_copy['Date'] = df_copy['Date'].str.replace("'", "/")
df_copy['Date'] = df_copy['Date'].apply(lambda x: f"{x[:4]}/{x[4:6]}/{x[6:]}" if x.isdigit() and len(x) == 8 else x) 

try:
    df_copy['Date'] = pd.to_datetime(df_copy['Date'], format='%Y/%m/%d', errors='coerce')
except Exception as e:
    print("\nErro ao converter a coluna 'Date': ", e)

print("\nDados corrigidos na coluna 'Date': ")
print(df_copy[['Date']].tail(10))

df_cleaned = df_copy.dropna(subset=['Date'])

print("\nDados com valores nulos removidos: ")
df_cleaned.info()

print("\nDataFrame final apos todas as transformações: ")
print(df_cleaned)