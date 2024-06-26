import os
import warnings
import PIL.Image
import streamlit as st

import fitz as pymupdf
import google.generativeai as genai

from dotenv import find_dotenv, load_dotenv

warnings.filterwarnings("ignore")
load_dotenv(find_dotenv())

class summaryText:
    """
    this class aims to summarize a large text into a simple
    ...
    ...

    Methods
    -------
    summarizerMethod(self) -> str
        returns the summarized text based on a phrase using prompt engineer
    __imageReading(self) -> str
        developing: reading a image e return what it means
    """

    def __init__(self, text, question):
        self.google_api = st.secrets['GOOGLE_API_KEY']
        # self.google_api = os.environ.get('GOOGLE_API_KEY')
        self.model = genai.GenerativeModel('gemini-1.5-flash')
        self.text = text
        self.question = question
        """
        Parameters
        ---------
        media: str
            name and path of the file      
        """
    
    def summarizerMethod(self):
        response = self.model.generate_content([self.question, self.text])
        return response.text
    
    def __imageReading(self, image):
        img = PIL.Image.open(image)
        response = self.model.generate_content(["Descreva a imagem em poucas palavras em português do Brasil", img])
        return response.text
      
    def __call__(self):
        return self.summarizerMethod()
