# --- Importar o streamlit --- #
import streamlit as st

# --- Importar o módulo da previsão --- #
from previsoes import Previsao

# --- Configurações da página --- #
st.set_page_config(page_title='Previsão', layout='wide')

# --- Título da página --- #
st.title('Previsão')

# --- Informar o que ocorre na página --- #
st.write('---')
st.subheader('Nesta página é possível prever se um cliente cancelará ou não o contrato.')
st.subheader('Você pode enviar os dados ao modelo por uma arquivo CSV ou escrito.')
st.write('---')

# --- Carregar o modelo --- #
modelo = Previsao()

# --- Colocar o botão de seleção do tipo de entrada --- #
entrada = st.radio(
    label='Escolha um dos tipos de entrada:',
    options=(
        'Manual',
        'CSV'
    ),
    horizontal=True
)

# --- verificar qual tipo de entrada foi escolhido --- #
if entrada == 'Manual':
    # --- Colocar o campo da idade --- #
    idade = st.text_input(
        label='Idade:',
        placeholder='Digite a idade do cliente'
    )

    # --- Esolher do sexo do cliente --- #
    sexo = st.radio(
        label='Sexo:',
        options=(
            'Homem',
            'Mulher'
        ),
        horizontal=True
    )
    # --- Converter para número --- #
    sexo_numero = ''
    if sexo == 'Homem':
        sexo_numero = 1
    else:
        sexo_numero = 0

    # --- Tempo como cliente --- #
    tempo_cliente = st.text_input(
        label='Tempo como cliente:',
        placeholder='Tempo como cliente em meses'
    )

    # --- Frequência de uso dos serviços --- #
    frequencia_uso = st.text_input(
        label='Frequência de uso:',
        placeholder='Frequência de uso dos serviços'
    )

    # --- Ligações para o callcenter --- #
    ligacoes = st.text_input(
        label='Ligações ao callcenter',
        placeholder='Quantidade de ligações ao callcenter'
    )

    # --- Dias de atraso --- #
    atraso = st.text_input(
        label='Dias de atraso',
        placeholder='Dias de atraso da conta'
    )

    # --- Tipo de assinatura --- #
    assinatura = st.radio(
        label='Tipo de assinatura:',
        options=(
            'Padrão',
            'Premium',
            'Básico'
        ),
        horizontal=True
    )
    # --- Converter para números --- #
    assinatura_numero = ''
    if assinatura == 'Básico':
        assinatura_numero = 0
    elif assinatura == 'Premium':
        assinatura_numero = 1
    else:
        assinatura_numero = 2

    # --- Tipo de contrato --- #
    contrato = st.radio(
        label='Tipo de contrato:',
        options=(
            'Mensal',
            'Quadrienal',
            'Anual'
        ),
        horizontal=True
    )
    # --- Converter para números --- #
    contrato_numero = ''
    if contrato == 'Mensal':
        contrato_numero = 1
    elif contrato == 'Quadrienal':
        contrato_numero = 2
    else:
        contrato_numero = 0

    # --- Total gasto --- #
    total_gasto = st.text_input(
        label='Total gasto:',
        placeholder='Total gasto do cliente'
    )

    # --- Última interação --- #
    ultima_interacao = st.text_input(
        label='Última interação:',
        placeholder='Última interação do cliente com a empresa em dias'
    )

    # --- Criar as colunas --- #
    colunas = st.columns(5)

    # --- Criar o botão para enviar os dados ao modelo --- #
    with colunas[2]:
        enviar = st.button(
            label='Enviar',
            use_container_width=True
        )

    if enviar:
        # --- Criar uma lista com os dados --- #
        dados = [int(idade), sexo_numero, int(tempo_cliente), int(frequencia_uso), int(ligacoes),
                 int(atraso), assinatura_numero, contrato_numero, float(total_gasto), int(ultima_interacao)]

        # --- Enviar os dados ao modelo --- #
        resposta = modelo.entrada_manual(dados)

        # --- Escrever a resposta --- #
        st.subheader(resposta)

else:
    # --- Colocar o campo de envio do arquivo CSV --- #
    upload = st.file_uploader(
        label='Escolha um arquivo CSV:',
        type='csv'
    )

    # --- Criar as colunas par centralizar o botão --- #
    colunas = st.columns(5)

    # --- Criar o botão ---
    with colunas[2]:
        enviar = st.button(
            label='Enviar',
            use_container_width=True
        )

    # --- Mostrar a previsão ao pressionar o botão --- #
    if enviar and upload:
        resposta = modelo.entrada_arquivo(upload)
        st.write(resposta)

        # --- Obter a tabela com a porcentagem de cancelamento --- #
        tabela_por = resposta['cancelamento'].value_counts(normalize=True)

        # --- Escrever a porcentagem de quam cancelou e não cancelou --- #
        cancelara = tabela_por.loc['Cancelará'] * 100
        nao_cancelara = tabela_por.loc['Não cancelará'] * 100
        st.subheader(f'Cancelará: {cancelara:.1f}%')
        st.subheader(f'Não cancelará: {nao_cancelara:.1f}%')
