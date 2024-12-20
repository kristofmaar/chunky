import unittest
import requests

BASE_URL = "http://localhost:8000"

class TestChunkPDF(unittest.TestCase):

    def test_chunk_pdf_success(self):
        with open("test_documents/gdpr.pdf", "rb") as pdf_file:
            files = {"file": ("gdpr.pdf", pdf_file, "application/pdf")}
            response = requests.post(f"{BASE_URL}/chunk", files=files)

        self.assertEqual(response.status_code, 200)
        response_json = response.json()
        self.assertIn("chunks", response_json)
        self.assertEqual(len(response_json["chunks"]), 392)

    def test_chunk_pdf_invalid_file_type(self):
        files = {"file": ("test_documents/test.txt", b"Sample text", "text/plain")}
        response = requests.post(f"{BASE_URL}/chunk", files=files)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"detail": "Invalid file type. Please upload a PDF file."})

    def test_chunk_pdf_exception(self):
        with open("test_documents/invalid_pdf.pdf", "rb") as pdf_file:
            files = {"file": ("test_wrong.pdf", pdf_file, "application/pdf")}
            response = requests.post(f"{BASE_URL}/chunk", files=files)

        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json(), {"detail": "An error occurred: EOF marker not found"})

if __name__ == "__main__":
    unittest.main()
