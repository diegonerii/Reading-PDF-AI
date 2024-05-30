from dotenv import find_dotenv, load_dotenv
from utils.summarize_text import *

load_dotenv(find_dotenv())

summary = summaryText(media="file.pdf")
summarized_text = summary()
print(summarized_text)