import os
import time
import threading
import requests
from tkinter import messagebox
from fpdf import FPDF
from utils import split_text, extract_text_md, extract_text_pdf

def translate_text(text_blocks, target_language, base_url, progress_var):
    translated_blocks = []
    headers = {
        "Content-Type": "application/json"
    }
    url = base_url + "/chat/completions"
    total_blocks = len(text_blocks)

    for idx, block in enumerate(text_blocks):
        success = False
        retries = 3
        while not success and retries > 0:
            try:
                messages = [
                    {
                        "role": "system",
                        "content": (
                            "Translate the provided markdown text into the specified target language, "
                            "retaining the original formatting (headings, lists, code blocks, etc.), "
                            "and return only the translated text without any extra explanations."
                        )
                    },
                    {
                        "role": "user",
                        "content": f"Please translate the following markdown content to {target_language}:\n\n{block}"
                    }
                ]

                data = {
                    "model": "gpt-3.5-turbo",
                    "messages": messages
                }
                response = requests.post(url, headers=headers, json=data)
                response.raise_for_status()
                
                response_data = response.json()
                translated_text = response_data['choices'][0]['message']['content']
                translated_blocks.append(translated_text)
                success = True
            except requests.exceptions.RequestException as e:
                retries -= 1
                time.sleep(1)
                print(f"Request error: {e}. Retries left: {retries}")
            except KeyError:
                messagebox.showerror("Error", "Invalid response format received from translation API.")
                sys.exit(1)
            except Exception as e:
                retries -= 1
                print(f"Unexpected error: {e}. Retries left: {retries}")

        if not success:
            messagebox.showerror("Error", "Unable to translate text after multiple attempts.")
            sys.exit(1)
        progress = int(((idx + 1) / total_blocks) * 100)
        progress_var.set(progress)
    return translated_blocks

def start_translation_thread(button, file_path, language_var, progress_var):
    button.config(state=tk.DISABLED)
    translation_thread = threading.Thread(target=lambda: start_translation(button, file_path, language_var, progress_var))
    translation_thread.start()

def start_translation(button, file_path, language_var, progress_var):
    input_file = file_path.get()
    target_language = language_var.get()
    base_url = "http://127.0.0.1:1234/v1"

    if not input_file:
        messagebox.showwarning("Warning", "Please select an input file.")
        button.config(state=tk.NORMAL)
        return

    if not os.path.isfile(input_file):
        messagebox.showerror("Error", "Specified file does not exist.")
        button.config(state=tk.NORMAL)
        return

    file_extension = os.path.splitext(input_file)[1].lower()
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'translations')
    os.makedirs(output_dir, exist_ok=True)

    try:
        if file_extension == '.md':
            text = extract_text_md(input_file)
        elif file_extension == '.pdf':
            text = extract_text_pdf(input_file)
        else:
            messagebox.showerror("Error", "Unsupported file type. Only .md and .pdf files are accepted.")
            return
        
        text_blocks = split_text(text)
        progress_var.set(0)
        translated_blocks = translate_text(text_blocks, target_language, base_url, progress_var)
        translated_text = ''.join(translated_blocks)
        
        output_file_name = os.path.splitext(os.path.basename(input_file))[0] + '_translated' + file_extension
        output_file = os.path.join(output_dir, output_file_name)
        
        if file_extension == '.md':
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(translated_text)
        elif file_extension == '.pdf':
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, translated_text)
            pdf.output(output_file)

        messagebox.showinfo("Success", f"Translation completed. Output file: {output_file}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during translation: {e}")
    finally:
        progress_var.set(100)
        button.config(state=tk.NORMAL)
