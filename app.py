import fitz
import streamlit as st

from dotenv import find_dotenv, load_dotenv
from utils.summarize_text import summaryText

load_dotenv(find_dotenv())

st.title('Seja bem-vindo ao Leitor de PDF por AI!')

file = st.file_uploader("Por favor, Selecione o Arquivo", type=['pdf'])
if file:
    binary_data = file.getvalue()
    doc = fitz.open(stream=binary_data, filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()

    text_input = st.text_input(
            "Faça uma Pergunta Sobre o Texto"
        )

    if text_input and file:
        summary = summaryText(text=text, question=text_input)
        summarized_text = summary()
        st.write(summarized_text)



