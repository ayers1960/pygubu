import tkinter as tk
from tkinter import filedialog
from pathlib import Path

class FileHandler:
    def __init__(self, text_widget: tk.Text):
        self.text_widget: tk.Text = text_widget

    def open(self):
        """
        Clear the contents of the text wiget and open a text file.
        Put the contents of the text file into the text widget.
        """
        selected_file = filedialog.askopenfilename()

        if not selected_file:
            return
        selected_file = Path(selected_file)
        file_contents = selected_file.read_text()

        #clear the text widget
        self.text_widget.delete("1.0", tk.END)

        #put contents of file into the widget
        self.text_widget.insert("1.0", file_contents)

