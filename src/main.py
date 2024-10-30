import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.ttk import Progressbar, Combobox
from translate import start_translation_thread

def browse_file():
    try:
        filename = filedialog.askopenfilename(
            title="Select a file",
            filetypes=(("Markdown Files", "*.md"), ("PDF Files", "*.pdf"), ("All Files", "*.*"))
        )
        if filename:
            file_path.set(filename)
        else:
            messagebox.showwarning("Warning", "No file was selected.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while selecting a file: {e}")

# GUI setup with error handling
try:
    root = tk.Tk()
    root.title("File Translator")

    file_path = tk.StringVar()
    language_var = tk.StringVar(value="english")
    progress_var = tk.IntVar()

    frame = tk.Frame(root, padx=10, pady=10)
    frame.pack(fill=tk.BOTH, expand=True)

    tk.Label(frame, text="Input file (.md or .pdf):").grid(row=0, column=0, sticky=tk.W)
    tk.Entry(frame, textvariable=file_path, width=50).grid(row=0, column=1, padx=5, pady=5)
    tk.Button(frame, text="Browse", command=browse_file).grid(row=0, column=2, padx=5, pady=5)

    tk.Label(frame, text="Target language:").grid(row=2, column=0, sticky=tk.W)
    languages = ["english", "spanish", "french", "german", "italian", "portuguese", "chinese", "japanese", "korean", "russian"]
    language_dropdown = Combobox(frame, values=languages, textvariable=language_var)
    language_dropdown.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

    tk.Label(frame, text="Translation progress:").grid(row=3, column=0, sticky=tk.W)
    progress_bar = Progressbar(frame, orient=tk.HORIZONTAL, length=400, mode='determinate', variable=progress_var)
    progress_bar.grid(row=3, column=1, padx=5, pady=5, columnspan=2)

    translate_button = tk.Button(frame, text="Start Translation", command=lambda: start_translation_thread(translate_button, file_path, language_var, progress_var))
    translate_button.grid(row=4, column=1, padx=5, pady=15)

    root.mainloop()
except Exception as e:
    messagebox.showerror("Error", f"An error occurred while setting up the interface: {e}")
