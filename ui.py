import helpers
import database as db
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askokcancel, WARNING


class CenterWidgetMixin:
    def centerWindow(self):
        if isinstance(self, (Tk, Toplevel)):
            self.update_idletasks()
            w = self.winfo_width()
            h = self.winfo_height()
            ws = self.winfo_screenwidth()
            hs = self.winfo_screenheight()
            x = int((ws - w) / 2)
            y = int((hs - h) / 2)
            self.geometry(f"{w}x{h}+{x}+{y}")  # width x height + offset_x + offset_y


class CreateClientWindow(Toplevel, CenterWidgetMixin):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Create client")
        self.build()
        self.centerWindow()
        self.transient(parent)
        self.grab_set()

    def build(self):
        frame = Frame(self)
        frame.pack(padx=20, pady=10)

        Label(frame, text="DNI (2 ints 1 upper char)").grid(row=0, column=0)
        Label(frame, text="Name (from 2 to 30 chars)").grid(row=0, column=1)
        Label(frame, text="DNI (from 2 to 30 chars)").grid(row=0, column=2)

        dni = Entry(frame)
        dni.grid(row=1, column=0)
        dni.bind("<KeyRelease>", lambda event: self.validate(event, 0))
        name = Entry(frame)
        name.grid(row=1, column=1)
        name.bind("<KeyRelease>", lambda event: self.validate(event, 1))
        surname = Entry(frame)
        surname.grid(row=1, column=2)
        surname.bind("<KeyRelease>", lambda event: self.validate(event, 2))

        frame = Frame(self)
        frame.pack(pady=10)

        addButton = Button(frame, text="Add", command=self.add_client)
        addButton.configure(state=DISABLED)
        addButton.grid(row=0, column=0)
        Button(frame, text="Cancel", command=self.close).grid(row=0, column=1)

        self.validations = [0, 0, 0]  # all "False"
        self.addButton = addButton
        self.dni = dni
        self.name = name
        self.surname = surname

    def add_client(self):
        self.master.treeView.insert(
            parent="",
            index="end",
            iid=self.dni.get(),
            values=(self.dni.get(), self.name.get(), self.surname.get()),
        )
        db.Clients.add(self.dni.get(), self.name.get(), self.surname.get())
        self.close()

    def close(self):
        self.destroy()
        self.update()

    def validate(self, event, index):
        value = event.widget.get()
        validation = (
            helpers.ultimate_dni_validate(value, db.Clients.clientsList)
            if index == 0
            else (value.isalpha() and 2 <= len(value) <= 30)
        )
        event.widget.configure({"bg": "Green" if validation else "Red"})
        # change button's status looking the validations
        self.validations[index] = validation
        self.addButton.config(
            state=NORMAL if self.validations == [1, 1, 1] else DISABLED
        )


class ModifyClientWindow(Toplevel, CenterWidgetMixin):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Modify client")
        self.build()
        self.centerWindow()
        self.transient(parent)
        self.grab_set()

    def build(self):
        frame = Frame(self)
        frame.pack(padx=20, pady=10)

        Label(frame, text="DNI (not editable)").grid(row=0, column=0)
        Label(frame, text="Name (from 2 to 30 chars)").grid(row=0, column=1)
        Label(frame, text="DNI (from 2 to 30 chars)").grid(row=0, column=2)

        dni = Entry(frame)
        dni.grid(row=1, column=0)
        name = Entry(frame)
        name.grid(row=1, column=1)
        name.bind("<KeyRelease>", lambda event: self.validate(event, 0))
        surname = Entry(frame)
        surname.grid(row=1, column=2)
        surname.bind("<KeyRelease>", lambda event: self.validate(event, 1))

        client = self.master.treeView.focus()
        fields = self.master.treeView.item(client, "values")
        dni.insert(0, fields[0])
        dni.config(state=DISABLED)
        name.insert(0, fields[1])
        surname.insert(0, fields[2])

        frame = Frame(self)
        frame.pack(pady=10)

        modifyButton = Button(frame, text="Modify", command=self.modify_client)
        modifyButton.grid(row=0, column=0)
        Button(frame, text="Cancel", command=self.close).grid(row=0, column=1)

        self.validations = [1, 1]  # all "True"
        self.modifyButton = modifyButton
        self.dni = dni
        self.name = name
        self.surname = surname

    def modify_client(self):
        client = self.master.treeView.focus()
        self.master.treeView.item(
            client, values=(self.dni.get(), self.name.get(), self.surname.get())
        )
        db.Clients.modify(self.dni.get(), self.name.get(), self.surname.get())
        self.close()

    def close(self):
        self.destroy()
        self.update()

    def validate(self, event, index):
        value = event.widget.get()
        validation = value.isalpha() and 2 <= len(value) <= 30
        event.widget.configure({"bg": "Green" if validation else "Red"})
        # change button's status looking the validations
        self.validations[index] = validation
        self.modifyButton.config(
            state=NORMAL if self.validations == [1, 1] else DISABLED
        )


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

        Button(frame, text="Add", command=self.create).grid(row=0, column=0)
        Button(frame, text="Modify", command=self.modify).grid(row=0, column=1)
        Button(frame, text="Delete", command=self.delete).grid(row=0, column=2)

        self.treeView = treeView  # export as an instance attribute

    def delete(self):
        client = self.treeView.focus()
        if client:
            fields = self.treeView.item(client, "values")
            confirmation = askokcancel(
                title="Confirmation Message",
                message=f"Are you sure to delete {fields[1]} {fields[2]}?",
                icon=WARNING,
            )
            if confirmation:
                self.treeView.delete(client)
                db.Clients.delete(fields[0])

    def create(self):
        CreateClientWindow(self)

    def modify(self):
        if self.treeView.focus():
            ModifyClientWindow(self)


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
