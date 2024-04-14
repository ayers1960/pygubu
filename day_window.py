#!/usr/bin/python3
import pathlib
import tkinter as tk
import pygubu
from datetime import datetime
from about_window import AboutWindow

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "day_window.ui"


class DayWindowApp:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        # Main widget
        self.mainwindow: tk.Toplevel = builder.get_object(
            "main_window", master)
        builder.connect_callbacks(self)

        self.lbl_day = builder.get_object("lbl_day")
        self.lbl_day.configure(text=datetime.now().strftime("%A"))
    def run(self):
        self.mainwindow.mainloop()

    def onAboutButtonClicked(self):
        about = AboutWindow(master=self.mainwindow)
        pass


if __name__ == "__main__":
    app = DayWindowApp()
    app.run()

