import os
from dotenv import find_dotenv, load_dotenv
from utils.read_pdf import readPDF
from utils.summarize_text import *

load_dotenv(find_dotenv())

file_name = os.environ.get('file_name')

reader = readPDF(file='JaneEyre.pdf')
reader = reader()

for page in reader:
    summarizer = summaryText(text=page)
    summarizer.tokenizerMethod()