import unittest
from utils import extract_text_md, extract_text_pdf, split_text
import os

class TestUtilsFunctions(unittest.TestCase):

    def test_extract_text_md_success(self):
        with open("test.md", "w") as f:
            f.write("This is a test Markdown file.")
        
        text = extract_text_md("test.md")
        self.assertEqual(text, "This is a test Markdown file.")
        
        os.remove("test.md")

    def test_extract_text_pdf_success(self):
        # Assume "test.pdf" is a small sample PDF with known content.
        with open("test.pdf", "w") as f:
            f.write("This is a test PDF file.")

        text = extract_text_pdf("test.pdf")
        self.assertTrue(isinstance(text, str))
        
        os.remove("test.pdf")

    def test_split_text(self):
        text = "This is a test sentence " * 100
        blocks = split_text(text, max_tokens=50)
        
        self.assertTrue(len(blocks) > 1)
        self.assertTrue(all(len(block) <= 200 for block in blocks))

if __name__ == '__main__':
    unittest.main()
