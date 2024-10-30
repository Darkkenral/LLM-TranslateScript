import fitz
import sys
from tkinter import messagebox

def extract_text_md(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
        return text
    except Exception as e:
        messagebox.showerror("Error", f"Error reading .md file: {e}")
        sys.exit(1)

def extract_text_pdf(file_path):
    try:
        text = ""
        with fitz.open(file_path) as doc:
            for page in doc:
                text += page.get_text()
        return text
    except Exception as e:
        messagebox.showerror("Error", f"Error reading .pdf file: {e}")
        sys.exit(1)

def split_text(text, max_tokens=500):
    max_chars = max_tokens * 4
    blocks = []
    try:
        while len(text) > max_chars:
            split_point = text[:max_chars].rfind('\n')
            if split_point == -1:
                split_point = text[:max_chars].rfind(' ')
            if split_point == -1:
                split_point = max_chars
            blocks.append(text[:split_point])
            text = text[split_point + 1:]
        if text.strip():
            blocks.append(text)
    except Exception as e:
        messagebox.showerror("Error", f"Error splitting text: {e}")
        sys.exit(1)
    return blocks

