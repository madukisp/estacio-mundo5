import pandas as pd

# Função para ler o conteúdo do arquivo CSV
def ler_csv(caminho_arquivo):
    return pd.read_csv(caminho_arquivo, sep=';', engine='python')

# Função para exibir informações gerais sobre o DataFrame
def exibir_informacoes(df):
    print("Informações gerais:")
    df.info()
    print("\nPrimeiras 5 linhas:")
    print(df.head(5))
    print("\nÚltimas 5 linhas:")
    print(df.tail(5))

# Função para substituir valores nulos na coluna 'Calories'
def substituir_calorias_nulas(df):
    df['Calories'] = df['Calories'].fillna(0)
    return df

# Função para substituir valores nulos na coluna 'Date'
def substituir_datas_nulas(df):
    df['Date'] = df['Date'].fillna('01/01/2020')
    return df

# Função para limpar as datas no formato 'YYYYMMDD' e 'YYYY/MM/DD'
def limpar_datas(df):
    def clean_date(date_str):
        date_str = date_str.replace("'", "")  # Remove aspas simples se houver
        if date_str.isdigit() and len(date_str) == 8:  # Corrige datas no formato YYYYMMDD
            return f"{date_str[:4]}/{date_str[4:6]}/{date_str[6:]}"
        return date_str

    df['Date'] = df['Date'].apply(clean_date)
    return df

# Função para converter a coluna 'Date' para o formato datetime
def converter_para_datetime(df):
    try:
        df['Date'] = pd.to_datetime(df['Date'], format='%Y/%m/%d', errors='coerce')
    except Exception as e:
        print("\nErro ao converter a coluna 'Date':", e)
    return df

# Função para remover registros com valores nulos na coluna 'Date'
def remover_datas_nulas(df):
    df_cleaned = df.dropna(subset=['Date'])
    return df_cleaned

# Função para corrigir a duração incorreta
def corrigir_duracao(df):
    df.loc[df['Duration'] == 450, 'Duration'] = 45
    return df

# Função para corrigir o ID incorreto na linha 21
def corrigir_id(df):
    df.loc[(df['ID'] == 1) & (df['Date'] == pd.Timestamp('2020-12-21')), 'ID'] = 21
    return df

# Função para corrigir o valor incorreto na linha 20
def corrigir_calorias_linha_20(df):
    df.loc[df['ID'] == 20, 'Calories'] = df.loc[df['ID'] == 20, 'Calories'].replace('2430 2', '2430')
    return df

# Função principal que organiza o fluxo do processamento de dados
def processar_dados(caminho_arquivo):
    df = ler_csv(caminho_arquivo)
    exibir_informacoes(df)
    df_copy = df.copy()
    df_copy = substituir_calorias_nulas(df_copy)
    df_copy = substituir_datas_nulas(df_copy)
    df_copy = limpar_datas(df_copy)
    df_copy = corrigir_duracao(df_copy)
    df_copy = corrigir_id(df_copy)
    df_copy = corrigir_calorias_linha_20(df_copy)
    df_copy = converter_para_datetime(df_copy)
    
    print("\nDados corrigidos na coluna 'Date':")
    print(df_copy[['Date']].tail(10))
    
    df_cleaned = remover_datas_nulas(df_copy)
    
    print("\nDados com valores nulos removidos:")
    df_cleaned.info()
    
    print("\nDataFrame final após todas as transformações:")
    print(df_cleaned)

# Chamada da função principal com o caminho do arquivo CSV
caminho_arquivo = r'C:\Users\AMANDA DUQUE\Documents\AMANDA\estacio-mundo5\Missao3\dados.csv'
processar_dados(caminho_arquivo)
