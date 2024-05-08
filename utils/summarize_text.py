import warnings
from dotenv import find_dotenv, load_dotenv
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

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
        returns the summarized text based on pipeline method
    tokenizerMethod(self) -> str
        returns the summarized text based on tokenizer method
    """

    def __init__(self, text, max_length=130, min_length=30):
        self.task = "summarization"
        self.model = "facebook/bart-large-cnn"
        self.text = text
        self.max_length=max_length
        self.min_length=min_length
        """
        Parameters
        ---------
        text: str
            input text
        max_length: int
            max lenght of the response
        min_length: int
            min lenght of the response        
        """
    
    def summarizerMethod(self):
        pipe = pipeline(self.task, model=self.model)
        summary = print(pipe(self.text, max_length=self.max_length, min_length=self.min_length, do_sample=False)[0]['summary_text'])
        return summary
    
    def tokenizerMethod(self):
        # Tokenizer and model are results of a ML process
        tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")
        model = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large-cnn")
    
        # The tokenizer is responsible for all the preprocessing that the pre-trained model expects
        # It will produce a dictionary that you can use in subsequent code or simply pass directly to your model using the argument unpacking operator **
        tokenized_text = tokenizer(self.text)
        
        # pt = PyTorch
        tokenized_text = tokenizer(self.text, return_tensors="pt")
        
        # outputs will be a tensor
        outputs = model.generate(tokenized_text['input_ids'], max_new_tokens=self.max_length)

        # After that, the tensor will be decodified
        result = tokenizer.decode(outputs[0], skip_special_tokens=True)

        print(result)
