import pandas as pd
import streamlit as st

from dotenv import find_dotenv, load_dotenv
from utils.summarize_text import *

load_dotenv(find_dotenv())

st.title('Seja Bem-Vindo!')

# Options list
df_format_file = pd.DataFrame({
    'Input': ['.pdf']
    })

option = st.selectbox(
    'Qual o Formato dos Dados de Entrada?',
     df_format_file['Input'])

file = st.file_uploader("Por favor, Selecione o Arquivo", type=['pdf'])

text_input = st.text_input(
        "Faça uma Pergunta Sobre o Texto"
    )

if text_input and file:
    summary = summaryText(media=file, question=text_input)
    summarized_text = summary()
    # print(summarized_text)

    if st.button('Gerar Reposta'):
        st.write(summarized_text)

