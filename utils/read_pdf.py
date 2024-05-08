import PyPDF2
import warnings

warnings.filterwarnings('ignore')

class readPDF:
    def __init__(self, file):
        self.file = file
        self.__readPDF()
    
    def __readPDF(self):
        # Loading PDF file as a binary
        pdf_file = open(self.file, 'rb')

        # Reading pdf_file
        pdf_obj = PyPDF2.PdfReader(pdf_file)

        return pdf_obj