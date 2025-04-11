# --- Importar as bibliotecas --- #
import numpy as np
import pandas as pd
from joblib import load

# --- Importar o módulo de abriro CSV --- #
from abrir_csv import abrir_arquivo


class Previsao:
    """Classe responsável por gerar a previsão com o modelo de IA."""
    def __init__(self):
        """Função que inicializa a classe."""
        # --- Inicializar o modelo --- #
        self.modelo = load('./modelo/decision_tree.joblib')

    def entrada_manual(self, entradas):
        """Função responsável por dar a previsão quando os dados são digitados."""
        # --- Transformar a lista em um array --- #
        dados = np.array([entradas])

        # --- Realizar a previsão --- #
        previsao = self.modelo.predict(dados)

        # --- Mostrar a resposta de um jeito que o usuário entenda --- #
        resposta = ''
        if previsao == 0:
            resposta = 'Não cancelará'
        elif previsao == 1:
            resposta = 'Cancelará'

        return resposta

    def entrada_arquivo(self, arquivo):
        """Função responsável por dar a previsão com os dados a partir de um arquivo."""
        # --- Abrir o CSV no site --- #
        abrir_arquivo(arquivo)

        # --- Carregar os dados --- #
        dados = pd.read_csv('csv_temp.csv')

        # --- Copiar os dados --- #
        dados_copia = dados.copy()

        # --- Converter os dados para números --- #
        dados_copia['sexo'].replace('Homem', 1, inplace=True)
        dados_copia['sexo'].replace('Mulher', 0, inplace=True)
        dados_copia['assinatura'].replace('Basico', 0, inplace=True)
        dados_copia['assinatura'].replace('Premium', 1, inplace=True)
        dados_copia['assinatura'].replace('Padrao', 2, inplace=True)
        dados_copia['duracao_contrato'].replace('Mensal', 1, inplace=True)
        dados_copia['duracao_contrato'].replace('Quadrienal', 2, inplace=True)
        dados_copia['duracao_contrato'].replace('Anual', 0, inplace=True)

        # --- Retirar a coluna com o ID dos clientes --- #
        dados_copia = dados_copia.drop('CustomerID', axis=1)

        # --- Realizar a previsão --- #
        previsao = pd.Series(self.modelo.predict(dados_copia)).rename('cancelamento', inplace=True)

        # --- Juntar as tabelas --- #
        resposta = pd.concat([dados, previsao], axis=1)

        # --- Converter o resultado do cancelamento em palavra --- #
        resposta['cancelamento'].replace(0, 'Não cancelará', inplace=True)
        resposta['cancelamento'].replace(1, 'Cancelará', inplace=True)

        return resposta
