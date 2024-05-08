import PyPDF2
import warnings

warnings.filterwarnings('ignore')

class readPDF:
    def __init__(self, file: str):
        self.file = file
        self.pdf_list = self.__pdfReader()
    
    def __pdfReader(self) -> list:
        # Loading PDF file as a binary
        pdf_file = open(self.file, 'rb')

        # Reading pdf_file
        pdf_obj = PyPDF2.PdfReader(pdf_file)

        # Getting the number of the pages
        total_pages = len(pdf_obj.pages)

        pdf_list = []
        for page_num in range(0, total_pages):
            # Setting each page
            page = pdf_obj.pages[page_num]

            # Getting the content for each page
            page_content = page.extract_text()

            pdf_list.append(page_content)

        pdf_file.close()

        return pdf_list
    
    def __call__(self):
        return self.pdf_list