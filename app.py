from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from PyPDF2 import PdfReader
import re
from langchain.text_splitter import RecursiveCharacterTextSplitter

app = FastAPI()

def clean_text(text: str) -> str:
    text = re.sub(r'\s+', ' ', text)  # remove extra whitespace
    text = re.sub(r'[^\x20-\x7E]', '', text)  # remove non-printable characters
    text = re.sub(r' +', ' ', text)  # remove multiple spaces
    return text

def chunk_text(text: str, chunk_size: int = 1024, overlap: int = 100) -> list:
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=overlap)
    chunks = splitter.split_text(text)
    return chunks

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a PDF file.")

    try:
        pdf_reader = PdfReader(file.file)
        extracted_text = ""
        for page in pdf_reader.pages:
            extracted_text += page.extract_text()
        
        cleaned_text = clean_text(extracted_text)
        chunks = chunk_text(cleaned_text)
        
        return JSONResponse(content={"chunks": chunks})

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")