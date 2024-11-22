import re
from langchain.text_splitter import RecursiveCharacterTextSplitter

class Chunky:
    def __init__(self, chunk_size: int = 1024, overlap: int = 100):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def clean_text(self, text: str) -> str:
        text = re.sub(r'\s+', ' ', text)  # remove extra whitespace
        text = re.sub(r'[^\x20-\x7E]', '', text)  # remove non-printable characters
        text = re.sub(r' +', ' ', text)  # remove multiple spaces
        return text

    def chunk_text(self, text: str) -> list:
        splitter = RecursiveCharacterTextSplitter(chunk_size=self.chunk_size, chunk_overlap=self.overlap)
        chunks = splitter.split_text(text)
        return chunks