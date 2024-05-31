import os
import warnings
import PIL.Image

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

    def __init__(self, media, question):
        self.google_api = os.environ['GOOGLE_API_KEY']
        self.file_name = os.environ['file_name']
        self.model = genai.GenerativeModel('gemini-1.5-flash')
        self.media = media
        self.question = question
        """
        Parameters
        ---------
        media: str
            name and path of the file      
        """
    
    def summarizerMethod(self):
        document = pymupdf.open(self.media)
        pdf_list = []

        for page in document.pages():
            pageText = page.get_text(option='text')
            pdf_list.append((pageText))

        concatenated_text = " ".join(pdf_list)
        response = self.model.generate_content([self.question, concatenated_text])
        return response.text
    
    def __imageReading(self, image):
        img = PIL.Image.open(image)
        response = self.model.generate_content(["Descreva a imagem em poucas palavras em português do Brasil", img])
        return response.text
      
    def __call__(self):
        return self.summarizerMethod()
