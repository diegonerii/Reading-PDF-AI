# Reading-PDF-AI

## Resumo

Este é um projeto simples que consiste em dois arquivos Python e um arquivo de aplicativo.

## Arquivos

1. **read_pdf.py:**
   Este arquivo contém uma classe `readPDF` que é capaz de ler um arquivo PDF e extrair o texto de suas páginas. Ele usa a biblioteca `PyPDF2` para processar os arquivos PDF.

2. **summarize_text.py:**
    Este arquivo contém uma classe `summaryText` que é capaz de sumarizar um texto longo em uma versão mais concisa. Ele utiliza o modelo `facebook/bart-large-cnn` do `Hugging Face Transformers`.

3. **app.py:**
    Este arquivo é um exemplo de como usar as classes `readPDF` e `summaryText` para ler um PDF e sumarizar o texto de suas páginas.

## Utilização
Para usar este projeto, você precisa instalar as dependências listadas no arquivo requirements.txt. Você pode fazer isso executando o seguinte comando:

    pip install -r requirements.txt

Depois de instalar as dependências, você pode executar o arquivo `app.py` para ler um PDF e sumarizar seu conteúdo.