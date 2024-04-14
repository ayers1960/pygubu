#!/usr/bin/python3
import pathlib
import tkinter as tk
import pygubu
from FileHandler import FileHandler

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "TextEditorDemo.ui"


class TexteditordemoApp:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        # Main widget
        self.mainwindow: tk.Toplevel = builder.get_object("toplevel1", master)
        # Main menu
        _main_menu = builder.get_object("menu1", self.mainwindow)
        self.mainwindow.configure(menu=_main_menu)
        builder.connect_callbacks(self)

        self.text1 = builder.get_object("text1")
        self.file_handler = FileHandler(text_widget=self.text1)

    def onMnuOpenClicked(self):
        self.file_handler.open()

    def onMnuExitClicked(self):
        self.mainwindow.destroy()

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    app = TexteditordemoApp()
    app.run()

