class Client:
    def __init__(self, dni, name, surname):
        self.dni = dni
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"({self.dni}) {self.name} {self.surname}"


class Clients:
    clientsList = []

    @staticmethod
    def search(dni):
        for client in Clients.clientsList:
            if client.dni == dni:
                return client

    @staticmethod
    def add(dni, name, surname):
        client = Client(dni, name, surname)
        Clients.clientsList.append(client)

        return client

    @staticmethod
    def modify(dni, name, surname):
        for index, client in enumerate(Clients.clientsList):
            if client.dni == dni:
                Clients.clientsList[index].name = name
                Clients.clientsList[index].surname = surname

                return Clients.clientsList[index]

    @staticmethod
    def delete(dni):
        for index, client in enumerate(Clients.clientsList):
            if client.dni == dni:
                return Clients.clientsList.pop(index)
