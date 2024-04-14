import tkinter as tk
from tkinter import ttk
from time import sleep
from threading import Thread
from queue import Queue
from enum import Enum, auto

class TicketPurpose(Enum):
    UPDATE_PROGRESS_TEXT = auto()
    UPDATE_PROGRESS_COMPLETE = auto()

class Ticket:
    def __init__(self,
                 ticket_type: TicketPurpose,
                 ticket_value: str):
        self.ticket_type = ticket_type
        self.ticket_value = ticket_value


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("640x480")
        self.create_frame_buttons().pack(expand=True)
        self.queue_message = Queue()
        self.bind("<<CheckQueue>>", self.check_queue)

    def check_queue(self, event):
        """Read The Queue"""
        msg: Ticket
        msg = self.queue_message.get()
        
        if msg.ticket_type == TicketPurpose.UPDATE_PROGRESS_TEXT:
            self.lbl_status.configure(text=msg.ticket_value)
        elif msg.ticket_type == TicketPurpose.UPDATE_PROGRESS_COMPLETE:
            self.lbl_status.configure(text=msg.ticket_value)
            self.btn_download.configure(state=tk.NORMAL)

    def create_frame_buttons(self):
        """Create and return a frame that contains buttons"""
        self.frame_buttons = ttk.Frame(self)
        self.btn_download = ttk.Button(self.frame_buttons, 
                                        text="Download",
                                        command=self.on_download_button_clicked)
        self.btn_test = ttk.Button(self.frame_buttons, text="test", command=self.on_test_button_clicked)
        self.lbl_status = ttk.Label(self.frame_buttons)

        self.btn_download.pack()
        self.btn_test.pack()
        self.lbl_status.pack()
        return self.frame_buttons
    
    def on_download_button_clicked(self):
        self.btn_download.configure(state=tk.DISABLED)
        new_thread = Thread(target=self.download,
                            args=("sky.jpg",),
                            daemon=True
        )
        new_thread.start()

    def download(self, file_name: str):
        """download in a separate thread"""
        print("starting download")
        for progress in range(1,101):
            
            ticket = Ticket(ticket_type=TicketPurpose.UPDATE_PROGRESS_TEXT,
                            ticket_value=f"Downloading {file_name}...{progress}%"
            )
            self.queue_message.put(ticket)
            self.event_generate("<<CheckQueue>>")

            sleep(0.25)
        ticket = Ticket(ticket_type=TicketPurpose.UPDATE_PROGRESS_COMPLETE,
                        ticket_value=f"Download Complete"
        )
        self.queue_message.put(ticket)
        self.event_generate("<<CheckQueue>>")
    
    def on_test_button_clicked(self):
        print("test...")

if __name__ == "__main__":
    main = MainWindow()
    main.mainloop()