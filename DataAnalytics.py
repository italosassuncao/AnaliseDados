"""
Essa solução consiste em carregar os dados transacionais de um arquivo JSON baseado na estrutura de dados da
Open Finance Brasil.

Os dados serão carregados, filtrados e visualizados em um gráfico de linhas.
"""

import pandas as pd

import matplotlib.pyplot as plt

# Realiza a leitura dos dados contidos em um arquivo JSON por exemplo

data = pd.read_json('dados.json')

# Exibe as primeiras linhas do DataFrame
print(data.head())

# Obtém informações sobre as colunas e tipos de dados
print(data.info())

# Gera estatísticas descritivas
print(data.describe())

# Valores nulos são tratados
data.dropna(inplace=True)

# Converte coluna de data para o tipo datetime
data['data'] = pd.to_datetime(data['data'])

# Agrupa transações por mês e calcula o total gasto em cada mês
monthly_spending = data.groupby(data['data'].dt.to_period('M'))['valor'].sum()

# Cria um gráfico de linha para visualizar os gastos mensais ao longo do tempo
plt.figure(figsize=(10, 6))

plt.plot(monthly_spending.index.to_timestamp(), monthly_spending.values, marker='o')

plt.xlabel('Mês')

plt.ylabel('Total Gasto')

plt.title('Gastos Mensais')

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()
