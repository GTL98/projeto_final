# --- Importar o streamlit --- #
import streamlit as st

# --- Importar o módulo da criação da tabela --- #
from tabelas import tabela

# --- Configurações da página --- #
st.set_page_config(page_title='Tabelas', layout='wide')


# --- Título da página --- #
st.title('Tabelas')

# --- Informações da página --- #
st.write('---')
st.subheader('Nesta página você terá acesso à tabela com informações estatísticas dos dados.')
st.write('---')

# --- Colocar o campo para adicionar o arquivo CSV --- #
upload = st.file_uploader(
    label='Escolha um arquivo CSV:',
    type='csv'
)

# --- Verificar se o arquivo foi adicionado ao site --- #
if upload:
    st.write(tabela(upload))
