# chunky
Meet *chunky*, the coolest text chunking API you'll ever use.

## Overview
TODO

## Endpoints

### Upload PDF

#### URL
`POST /upload`

#### Description
Uploads a PDF file, extracts text from it, cleans the text, and chunks it into smaller pieces.

#### Request
- **Content-Type**: `multipart/form-data`
- **Parameters**:
  - `file` (required): The PDF file to be uploaded.

#### Responses

- **200 OK**
  - **Content-Type**: `application/json`
  - **Body**:
    ```json
    {
      "chunks": [
        "chunk1",
        "chunk2",
        ...
      ]
    }
    ```

- **400 Bad Request**
  - **Content-Type**: `application/json`
  - **Body**:
    ```json
    {
      "detail": "Invalid file type. Please upload a PDF file."
    }
    ```

- **500 Internal Server Error**
  - **Content-Type**: `application/json`
  - **Body**:
    ```json
    {
      "detail": "An error occurred: {error_message}"
    }
    ```

## Example

### Request
```bash
curl -X POST "http://localhost:8000/upload" -H "accept: application/json" -H "Content-Type: multipart/form-data" -F "file=@path/to/your/file.pdf"
```

## Sources
- https://unstructured.io/blog/chunking-for-rag-best-practices
- https://www.pinecone.io/learn/chunking-strategies
- https://www.reddit.com/r/LangChain/comments/16bjj6w/what_is_optimal_chunk_size/
- https://www.reddit.com/r/LangChain/comments/16m73j4/comment/k17vcki/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
- https://pub.towardsai.net/how-to-optimize-chunk-sizes-for-rag-in-production-fae9019796b6
- https://github.com/Azure-Samples/azure-search-openai-demo/blob/main/app/backend/prepdocs.py
- https://www.restack.io/p/text-chunking-answer-spacy-semantic-chunking-cat-ai
- **[Improving Retrieval for RAG based Question Answering Models on Financial Documents](https://arxiv.org/abs/2404.07221)**  
  *Spurthi Setty, Harsh Thakkar, Alyssa Lee, Eden Chung, Natan Vidra*  
  *arXiv preprint, 2024*.  
  [arXiv:2404.07221](https://arxiv.org/abs/2404.07221)  
  **Abstract**: This paper discusses advanced chunking techniques, query expansion, and metadata integration to enhance retrieval quality for question-answering models in RAG systems.
- **[Question-Based Retrieval using Atomic Units for Enterprise RAG](https://arxiv.org/abs/2405.12363)**  
  *Vatsal Raina and Mark Gales*  
  *arXiv preprint, 2024*.  
  [arXiv:2405.12363](https://arxiv.org/abs/2405.12363)  
  **Abstract**: This paper introduces a method that decomposes text into atomic statements and generates synthetic questions to improve chunk retrieval accuracy in enterprise RAG applications.