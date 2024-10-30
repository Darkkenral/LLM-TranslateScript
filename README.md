# 🌐 LLM File Translator

**LLM File Translator** is a tool designed to translate `.md` and `.pdf` files using powerful language models (LLMs) through a user-friendly graphical interface. Built with **Tkinter** for an intuitive GUI and powered by **LLM Studio** as the core LLM engine, this project enables easy switching between language models for translation flexibility. Tested with **LLaMA 3** and **LLaMA 2**, LLM File Translator aims to deliver reliable and accurate file translations.

---

## 🚀 Features

- **📄 Translate .md and .pdf Files**: Supports translation of both Markdown and PDF formats while preserving structure.
- **🌍 Multilingual Support**: Translate content into multiple languages: English, Spanish, French, German, Italian, Portuguese, Chinese, Japanese, Korean, and Russian.
- **🖥️ Interactive GUI**: Built with Tkinter, featuring a progress bar to track translation status.
- **🧠 LLM Studio Integration**: Easily switch between LLM models to use the best one for your needs.
- **🔧 Customizable**: Tested with LLaMA models, but any compatible model can be configured for translation tasks.

---

## 📋 Requirements

- **Python 3.8+**
- **Dependencies**: Specified in `requirements.txt` (installation instructions below)
- **LLM Studio**: The LLM Studio server must be running with a model loaded and active for API requests to function.

---

## 🔧 Installation

1. Clone the repository:
   
   ```bash
   git clone https://github.com/your-username/LLM-File-Translator.git
   cd LLM-File-Translator
   ```

2. Install dependencies:
   
   ```bash
   pip install -r requirements.txt
   ```

---

## 🛠️ Configuration

### LLM Studio Setup

This project uses **LLM Studio** as the translation backend. **Make sure to have LLM Studio running with a loaded model and the server activated** to handle translation requests.

To set up:

1. **Load a Model** in LLM Studio according to your translation requirements.
2. **Activate the API Server** within LLM Studio to make it accessible for translation requests.
3. In `src/main.py`, ensure `base_url` points to the correct LLM Studio endpoint.

For LLM model switching, refer to the LLM Studio documentation to add or change models as needed.

---

## 📖 Usage

1. **Run the main script to start the GUI:**
   
   ```bash
   python src/main.py
   ```

2. **In the GUI**:
   
   - **Select** the `.md` or `.pdf` file you want to translate.
   - **Choose** the target language.
   - **Click** "Start Translation" to begin. The translated file will be saved to the `translations/` folder.

---

## 🧪 Testing

Run automated tests to ensure all components function correctly:

```bash
python -m unittest discover tests/
```

---

## 📂 Project Structure

```plaintext
/project-root
├── src/
│   ├── main.py               # Main source code (GUI)
│   ├── translate.py          # Translation functions
│   └── utils.py              # Helper functions
├── docs/                     # Documentation
├── tests/                    # Automated tests
├── translations/             # Translated files output
├── README.md                 # Project overview
└── requirements.txt          # Python dependencies
```

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. **Fork** the repository.
2. **Create** a new branch:
   
   ```bash
   git checkout -b feature/your-feature
   ```
3. **Commit** your changes:
   
   ```bash
   git commit -m "Add a new feature"
   ```
4. **Push** to your branch:
   
   ```bash
   git push origin feature/your-feature
   ```
5. **Open** a Pull Request.

---

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.
