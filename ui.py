import database as db
from tkinter import *
from tkinter import ttk


class CenterWidgetMixin:
    def centerWindow(self):
        self.update()
        w = self.winfo_width()
        h = self.winfo_height()
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x = int(ws / 2 - w / 2)
        y = int(hs / 2 - h / 2)
        self.geometry(f"{w}x{h}+{x}+{y}")  # width x height + offset_x + offset_y


class MainWindow(Tk, CenterWidgetMixin):
    def __init__(self):
        super().__init__()
        self.title("Customer Manager")
        self.build()
        self.centerWindow()

    def build(self):
        frame = Frame(self)
        frame.pack()

        treeView = ttk.Treeview(frame)
        treeView["columns"] = ("DNI", "Name", "Surname")

        treeView.column("#0", width=0, stretch=NO)
        treeView.column("DNI", anchor=CENTER)
        treeView.column("Name", anchor=CENTER)
        treeView.column("Surname", anchor=CENTER)

        treeView.heading("DNI", text="DNI", anchor=CENTER)
        treeView.heading("Name", text="Name", anchor=CENTER)
        treeView.heading("Surname", text="Surname", anchor=CENTER)

        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill=Y)

        treeView.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=treeView.yview)

        for client in db.Clients.clientsList:
            treeView.insert(
                parent="",
                index="end",
                iid=client.dni,
                values=(client.dni, client.name, client.surname),
            )

        treeView.pack()

        frame = Frame(self)
        frame.pack(pady=20)

        Button(frame, text="Add", command=None).grid(row=0, column=0)
        Button(frame, text="Modify", command=None).grid(row=0, column=1)
        Button(frame, text="Delete", command=None).grid(row=0, column=2)

        self.treeView = treeView  # export as an instance attribute


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
