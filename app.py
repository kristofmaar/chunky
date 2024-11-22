from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from PyPDF2 import PdfReader
from chunky import Chunky

app = FastAPI()

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a PDF file.")

    try:
        pdf_reader = PdfReader(file.file)
        extracted_text = ""
        for page in pdf_reader.pages:
            extracted_text += page.extract_text()
        
        chunky = Chunky()
        cleaned_text = chunky.clean_text(extracted_text)
        chunks = chunky.chunk_text(cleaned_text)
        
        return JSONResponse(content={"chunks": chunks})

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")