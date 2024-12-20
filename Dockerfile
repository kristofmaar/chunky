FROM python:3.9-slim
WORKDIR /app
COPY environment.yml .
RUN pip install --no-cache-dir fastapi uvicorn PyPDF2 langchain nltk python-multipart 
COPY . .
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]