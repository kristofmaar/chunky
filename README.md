# chunky
Meet *chunky*, the coolest text chunking API you'll ever use.

## Overview
*chunky* is a proof-of-concept application designed to demonstrate the process of text chunking for Retrieval-Augmented Generation (RAG) models using vector search technologies. The primary objective of *chunky* is to provide a simple API endpoint that allows users to upload a PDF file, from which the application will extract, clean, and chunk the text into smaller, more optimal pieces.

## Endpoints

### Upload PDF

<details>
  <summary><code>POST</code> <code><b>/upload</b></code> <code>(Uploads a PDF file, extracts text from it, cleans the text, and chunks it into smaller pieces)</code></summary>

##### Parameters

> | name      |  type     | data type               | description                                                           |
> |-----------|-----------|-------------------------|-----------------------------------------------------------------------|
> | `file`    |  required | file                    | The PDF file to be uploaded                                           |

##### Responses

> | http code     | content-type                      | response                                                            |
> |---------------|-----------------------------------|---------------------------------------------------------------------|
> | `200`         | `application/json`                | `{"chunks": ["chunk1", "chunk2", ...]}`                             |
> | `400`         | `application/json`                | `{"detail": "Invalid file type. Please upload a PDF file."}`        |
> | `500`         | `application/json`                | `{"detail": "An error occurred: {error_message}"}`                  |

##### Example cURL

> ```bash
> curl -X POST "http://localhost:8000/upload" -H "accept: application/json" -H "Content-Type: multipart/form-data" -F "file=@path/to/your/file.pdf"
> ```

</details>

## Running the application

### On your machine
Create conda environment:
  ```bash
  conda env create --file=environment.yml
  ```

Activate conda environment:
  ```bash
  conda activate chunky
  ```

Run the FastAPI application:
  ```bash
  uvicorn app:app
  ```

### Using Docker

Build the Docker image:
```bash
docker build -t chunky:latest .
```

Run the Docker container:
```bash
docker run -d -p 8000:8000 chunky:latest
```

## Sources

### Blog posts, articles
- https://unstructured.io/blog/chunking-for-rag-best-practices
- https://www.pinecone.io/learn/chunking-strategies
- https://pub.towardsai.net/how-to-optimize-chunk-sizes-for-rag-in-production-fae9019796b6
- https://towardsdatascience.com/how-to-chunk-text-data-a-comparative-analysis-3858c4a0997a
- https://www.restack.io/p/text-chunking-answer-spacy-semantic-chunking-cat-ai
- https://www.llamaindex.ai/blog/evaluating-the-ideal-chunk-size-for-a-rag-system-using-llamaindex-6207e5d3fec5
- https://www.kaggle.com/discussions/general/503436
- https://medium.com/@datascientist_SheezaShabbir/text-cleaning-in-nlp-libraries-techniques-and-how-to-get-started-8c7c7e8ba7cf
- https://spotintelligence.com/2023/09/18/top-20-essential-text-cleaning-techniques-practical-how-to-guide-in-python/

### Forum posts
- https://www.reddit.com/r/LocalLLaMA/comments/15f0b24/open_source_options_for_better_chunking/
- https://www.reddit.com/r/LangChain/comments/16bjj6w/what_is_optimal_chunk_size/
- https://www.reddit.com/r/LangChain/comments/16m73j4/comment/k17vcki/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button

### Code examples
- https://github.com/topics/chunking
- https://github.com/Azure-Samples/azure-search-openai-demo/blob/main/app/backend/prepdocslib/textsplitter.py

### Research papers
- **[Improving Retrieval for RAG based Question Answering Models on Financial Documents](https://arxiv.org/abs/2404.07221)**  
  *Spurthi Setty, Harsh Thakkar, Alyssa Lee, Eden Chung, Natan Vidra*  
  *arXiv preprint, 2024*.  
  [arXiv:2404.07221](https://arxiv.org/abs/2404.07221)  
- **[Question-Based Retrieval using Atomic Units for Enterprise RAG](https://arxiv.org/abs/2405.12363)**  
  *Vatsal Raina and Mark Gales*  
  *arXiv preprint, 2024*.  
  [arXiv:2405.12363](https://arxiv.org/abs/2405.12363)  