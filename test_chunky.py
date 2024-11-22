import unittest
from chunky import Chunky
from PyPDF2 import PdfReader

class TestChunky(unittest.TestCase):
    
    def setUp(self):
        self.chunky = Chunky()

    def test_clean_text(self):
        text = "This  is   a \t test\nstring with  \n  irregular \t whitespace."
        expected = "This is a test string with irregular whitespace."
        self.assertEqual(self.chunky.clean_text(text), expected)

        text = "This is a test string with non-printable characters: \x00\x01\x02."
        expected = "This is a test string with non-printable characters: ."
        self.assertEqual(self.chunky.clean_text(text), expected)

    def test_chunk_text(self):
        text = "This is a test string that will be chunked into smaller pieces."
        chunks = self.chunky.chunk_text(text)
        self.assertIsInstance(chunks, list)
        self.assertGreater(len(chunks), 0)

    def test_chunk_pdf_text(self):
        reader = PdfReader("test_files/gdpr.pdf")
        text = ""
        for page in reader.pages:
            text += page.extract_text()

        cleaned_text = self.chunky.clean_text(text)
        chunks = self.chunky.chunk_text(cleaned_text)
        self.assertEqual(len(chunks), 392)

if __name__ == '__main__':
    unittest.main()