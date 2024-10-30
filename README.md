# File Translator

This project provides a tool to translate `.md` and `.pdf` files using a GUI built with Tkinter. Files are divided into manageable blocks for translation, and the translated output is saved in a new file within the `translations/` folder.

## Features

- Translates `.md` and `.pdf` files.
- Supports multiple languages (English, Spanish, French, German, Italian, Portuguese, Chinese, Japanese, Korean, and Russian).
- User-friendly GUI with a progress bar.
- Uses an OpenAI GPT-3.5-turbo-based translation API.

## Requirements

- Python 3.8+
- Python libraries specified in `requirements.txt`

### Install Dependencies

Install the necessary dependencies by running:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the main file to start the GUI:
   
   ```bash
   python src/main.py
   ```

2. Select the `.md` or `.pdf` file you wish to translate.

3. Choose the target language.

4. Click the "Start Translation" button to begin. The translated file will be saved in the `translations/` folder.

## Translation API Setup

This project uses the OpenAI API. To configure it:

1. Install and run the OpenAI API server or use your API key directly.
2. Ensure `src/main.py` is configured with the correct API URL in the `base_url` variable.

## Project Structure

```
/project-root
├── src/
│   ├── main.py               # Main source code
│   ├── translate.py          # Translation functions
│   ├── utils.py              # Helper functions
├── docs/                     # Documentation
├── tests/                    # Automated tests
├── translations/             # Translated files
├── README.md                 # This file
└── requirements.txt          # Project dependencies
```

## Testing

To run tests:

```bash
python -m unittest discover tests/
```

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or inquiries, contact the developer at [your-email@example.com].
