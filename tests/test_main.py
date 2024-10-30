import unittest
from unittest.mock import patch, MagicMock
import tkinter as tk
import main

class TestMainInterface(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.frame = tk.Frame(self.root, padx=10, pady=10)
        self.file_path = tk.StringVar()
        self.language_var = tk.StringVar(value="english")
        self.progress_var = tk.IntVar()

    def tearDown(self):
        self.root.destroy()

    def test_browse_file(self):
        with patch("main.filedialog.askopenfilename", return_value="test.md"):
            main.browse_file()
            self.assertEqual(main.file_path.get(), "test.md")

    def test_translation_button_disabled(self):
        translate_button = tk.Button(self.frame, text="Start Translation")
        main.start_translation_thread(translate_button)
        self.assertEqual(translate_button["state"], tk.DISABLED)

if __name__ == '__main__':
    unittest.main()
