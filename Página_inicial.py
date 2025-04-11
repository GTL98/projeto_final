# --- Importar o streamlit --- #
import streamlit as st

# --- Configurações da página --- #
st.set_page_config(page_title='Página Inicial', layout='wide')

# --- Colocar um título no topo da página --- #
st.title('Aula Projeto Final')

# --- Coloar algumas informações na página inicial --- #
st.write('---')
st.header('O que você encontrará em cada página:')
st.subheader('- Gráficos: Página que apresenta os gráficos do conjunto de dados.')
st.subheader('- Tabelas: Página que apresenta em uma tabela as informações estatísticas do conjunto de dados.')
st.subheader('- Previsão: Página que é possível realizar a previsão com um modelo de IA.')
