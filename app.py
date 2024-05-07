import warnings
from dotenv import find_dotenv, load_dotenv
from transformers import pipeline

warnings.filterwarnings("ignore")
load_dotenv(find_dotenv())

class summaryText:
    """
    this class aims to summarize a large text into a simple
    """

    def __init__(self, text):
        self.task = "summarization"
        self.model = "facebook/bart-large-cnn"
        self.text = text
        self.callfunction()
    
    def callfunction(self):
        pipe = pipeline(self.task, model=self.model)
        summary = print(pipe(self.text, max_length=130, min_length=30, do_sample=False)[0]['summary_text'])
        return summary