from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from PyPDF2 import PdfReader
import re

app = FastAPI()

def clean_text(text: str) -> str:
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\w\s,.!?]', '', text)
    return text.strip()

def chunk_text(text: str, chunk_size: int = 300, overlap: int = 30) -> list:
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size - overlap):
        chunk = ' '.join(words[i:i + chunk_size])
        chunks.append(chunk)
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