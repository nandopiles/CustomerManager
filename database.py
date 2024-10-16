import csv


class Client:
    def __init__(self, dni, name, surname):
        self.dni = dni
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"({self.dni}) {self.name} {self.surname}"


class Clients:
    clientsList = []
    with open("clients.csv", newline="\n") as file:
        reader = csv.reader(file, delimiter=";")
        for dni, name, surname in reader:
            client = Client(dni, name, surname)
            clientsList.append(client)

    @staticmethod
    def search(dni):
        for client in Clients.clientsList:
            if client.dni == dni:
                return client

    @staticmethod
    def add(dni, name, surname):
        client = Client(dni, name, surname)
        Clients.clientsList.append(client)
        Clients.save()
        return client

    @staticmethod
    def modify(dni, name, surname):
        for index, client in enumerate(Clients.clientsList):
            if client.dni == dni:
                Clients.clientsList[index].name = name
                Clients.clientsList[index].surname = surname
                Clients.save()
                return Clients.clientsList[index]

    @staticmethod
    def delete(dni):
        for index, client in enumerate(Clients.clientsList):
            if client.dni == dni:
                client = Clients.clientsList.pop(index)
                Clients.save()
                return client

    @staticmethod
    def save():
        with open("clients.csv", "w", newline="\n") as file:
            writer = csv.writer(file, delimiter=";")
            for client in Clients.clientsList:
                writer.writerow((client.dni, client.name, client.surname))
