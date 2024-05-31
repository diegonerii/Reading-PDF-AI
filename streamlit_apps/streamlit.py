import time
import pandas as pd
import numpy as np
import streamlit as st

st.title('Seja Bem-Vindo!')

##################################################

# Options list
df_format_file = pd.DataFrame({
    'Input': ['.pdf']
    })

option = st.selectbox(
    'Qual o Formato dos Dados de Entrada?',
     df_format_file['Input'])

# # bootom click
# left_column = st.columns(1)
# if st.button('ok'):
#     'Você selecionou: ', option

##################################################

text_input = st.text_input(
        "Faça uma Pergunta Sobre o Texto"
    )

if text_input:
    st.write("Inserir a função Python aqui")

if st.button('Gerar Reposta'):
    st.write("Reposta")

##################################################

# DATE_COLUMN = 'date/time'
# DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
#          'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

# @st.cache_data
# def load_data(nrows):
#     data = pd.read_csv(DATA_URL, nrows=nrows)
#     lowercase = lambda x: str(x).lower()
#     data.rename(lowercase, axis='columns', inplace=True)
#     data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
#     return data

# df = pd.DataFrame({
#   'first column': [1, 2, 3, 4],
#   'second column': [10, 20, 30, 40]
# })

# # Create a text element and let the reader know the data is loading.
# data_load_state = st.text('Reading the pdf')

# # Load 10,000 rows of data into the dataframe.
# data = load_data(10000)
# st.subheader('Raw data')
# # st.write(data)

# # Notify the reader that the data was successfully loaded.
# data_load_state.text("Done! Reading was a successful!")



##################################################

# # Add a selectbox to the sidebar:
# add_selectbox = st.sidebar.selectbox(
#     'How would you like to be contacted?',
#     ('Email', 'Home phone', 'Mobile phone')
# )

# # Add a slider to the sidebar:
# add_slider = st.sidebar.slider(
#     'Select a range of values',
#     0.0, 100.0, (25.0, 75.0)
# )

##################################################

# # bootom click
# left_column, right_column = st.columns(2)
# # You can use a column just like st.sidebar:
# left_column.button('Ok2')

# # Or even better, call Streamlit functions inside a "with" block:
# with right_column:
#     chosen = st.radio(
#         'Formato dos Dados de Entrada',
#         ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
#     st.write(f"You are in {chosen} house!")

##################################################

# 'Starting a long computation...'

# # Add a placeholder
# latest_iteration = st.empty()
# bar = st.progress(0)

# for i in range(100):
#   # Update the progress bar with each iteration.
#   latest_iteration.text(f'Iteration {i+1}')
#   bar.progress(i + 1)
#   time.sleep(0.1)

# '...and now we\'re done!'