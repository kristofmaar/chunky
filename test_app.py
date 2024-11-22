import unittest
import requests

BASE_URL = "http://localhost:8000"

class TestUploadPDF(unittest.TestCase):

    def test_upload_pdf_success(self):
        with open("test_files/gdpr.pdf", "rb") as pdf_file:
            files = {"file": ("gdpr.pdf", pdf_file, "application/pdf")}
            response = requests.post(f"{BASE_URL}/upload", files=files)

        self.assertEqual(response.status_code, 200)
        response_json = response.json()
        self.assertIn("chunks", response_json)
        self.assertEqual(len(response_json["chunks"]), 392)

    def test_upload_pdf_invalid_file_type(self):
        files = {"file": ("test_files/test.txt", b"Sample text", "text/plain")}
        response = requests.post(f"{BASE_URL}/upload", files=files)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"detail": "Invalid file type. Please upload a PDF file."})

    def test_upload_pdf_exception(self):
        with open("test_files/test_wrong.pdf", "rb") as pdf_file:
            files = {"file": ("test_wrong.pdf", pdf_file, "application/pdf")}
            response = requests.post(f"{BASE_URL}/upload", files=files)

        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json(), {"detail": "An error occurred: EOF marker not found"})

if __name__ == "__main__":
    unittest.main()
