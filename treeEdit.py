import tkinter as tk
from tkinter import ttk
#TreevieEdit example
class TreeviewEdit(ttk.Treeview):
    def __init__(self,root, **kw):
        super().__init__(root,**kw)
        self.bind("<Double-1>", self.on_double_click)
        self.root = root

    def on_focus_out(self,event):
        event.widget.destroy()

    def on_enter_pressed(self,event):
        new_text = event.widget.get()
        selected_iid = event.widget.editing_item_iid
        column_index = event.widget.editing_column

        if column_index == -1:
            self.item(selected_iid, text=new_text)
        else:
            current_values = self.item(selected_iid).get("values")
            current_values[column_index] = new_text
            self.item(selected_iid, values=current_values)
            
        event.widget.destroy()

    def on_double_click(self,event):
        #What region was clicked?
        regionClicked = self.identify_region(event.x, event.y)
        if regionClicked not in ('tree', 'cell'):
            return

        #which item was clicked?
        column = self.identify_column(event.x)
        column_index = int(column[1:]) - 1
        selected_iid = self.focus()
        #get text and values
        selected_values = self.item(selected_iid)

        if column == "#0":
            selected_text = selected_values.get("text")
        else:
            selected_text = selected_values.get("values")[column_index]
        column_box = self.bbox(selected_iid,column)
        entry_edit = ttk.Entry(self.root,width=column_box[2])
        #remember what we are editing
        entry_edit.editing_column = column_index
        entry_edit.editing_item_iid = selected_iid
        entry_edit.place(x=column_box[0], y=column_box[1], 
                         w=column_box[2], h=column_box[3])
        entry_edit.insert(0, selected_text)
        entry_edit.select_range(0,tk.END)
        entry_edit.focus()
    
        entry_edit.bind('<FocusOut>', self.on_focus_out)
        entry_edit.bind('<Return>', self.on_enter_pressed)


if __name__ == "__main__":
    root = tk.Tk()
    column_names = ("vehicle_name", "year", "color")
    treeview_vehicles = TreeviewEdit(root, columns=column_names)
    treeview_vehicles.heading("#0", text="Vehicle Type")
    treeview_vehicles.heading("vehicle_name", text="Vehicle Name")
    treeview_vehicles.heading("year", text="Year")
    treeview_vehicles.heading("color", text="Color")

    sedan_row = treeview_vehicles.insert(parent="",
                                         index=tk.END,
                                         text="Sedan")
    treeview_vehicles.insert(parent=sedan_row,
                             index=tk.END,
                             values=("Nissan Versa", "2010", "Silver"))

    treeview_vehicles.insert(parent=sedan_row,
                             index=tk.END,
                             values=("Toyota Camera", "2012", "Blue"))

    treeview_vehicles.pack(fill=tk.BOTH, expand=True)

    root.mainloop()
