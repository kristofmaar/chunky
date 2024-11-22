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