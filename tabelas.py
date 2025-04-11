# --- Importar o módulo de abrir o CSV --- #
from unittest.mock import inplace

import pandas as pd
from abrir_csv import abrir_arquivo


def tabela(arquivo):
    """Função responsável por reetornar a tabela com as informações estatísticas."""
    # --- Abrir o CSV --- #
    abrir_arquivo(arquivo)

    # --- Obter os dados  --- #
    dados = pd.read_csv('csv_temp.csv')

    # --- Criar a tabela com as informações estatísticas --- #
    info_estatisticas = dados.describe().T

    # --- Excluir a linha do ID do cliente --- #
    info_estatisticas.drop('CustomerID', axis=0, inplace=True)

    # --- Renomear as colunas --- #
    info_estatisticas.rename(
        columns={
            'count': 'Quantidade de clientes',
            'mean': 'Média',
            'std': 'Desvio padrão',
            'min': 'Mínimo',
            'max': 'Máximo'
        },
        inplace=True
    )

    return info_estatisticas
