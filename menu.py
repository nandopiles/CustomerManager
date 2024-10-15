import helpers
import database as db


def start():
    while True:
        helpers.clean_screen()

        print("===================================")
        print("  Welcome to the Customer Manager  ")
        print("===================================")
        print("[1] List Clients")
        print("[2] Search Client")
        print("[3] Add Client")
        print("[4] Modify Client")
        print("[5] Delete Client")
        print("[6] Close Customer Manager")
        print("===================================")

        option = input("> ")
        helpers.clean_screen()

        if option == "1":
            print("Listing clients...\n")
            for client in db.Clients.clientsList:
                print(client)

        elif option == "2":
            print("Searching client...\n")
            dni = None
            while True:
                dni = helpers.read_text(3, 3, "[-] DNI (2 int, 1 char)").upper()
                if helpers.dni_validate(dni, db.Clients.clientsList):
                    break
            client = db.Clients.search(dni)
            print(client) if client else print("[-] Client not found")

        elif option == "3":
            print("Adding client...\n")
            dni = None
            while True:
                dni = helpers.read_text(3, 3, "[-] DNI (2 int, 1 char)").upper()
                if helpers.dni_validate(dni, db.Clients.clientsList):
                    break

            name = helpers.read_text(2, 30, "[-] Name (from 2 to 30 chars)").capitalize()
            surname = helpers.read_text(
                2, 30, "[-] Surname (from 2 to 30 chars)"
            ).capitalize()
            db.Clients.add(dni, name, surname)
            print("[+] Client added correctly")

        elif option == "4":
            print("Modifying client...\n")
            dni = None
            while True:
                dni = helpers.read_text(3, 3, "[-] DNI (2 int, 1 char)").upper()
                if helpers.dni_validate(dni, db.Clients.clientsList):
                    break
            client = db.Clients.search(dni)
            if client:
                name = helpers.read_text(
                    2, 30, f"[-] Name (from 2 to 30 chars) [{client.name}]"
                ).capitalize()
                surname = helpers.read_text(
                    2, 30, f"[-] Surname (from 2 to 30 chars) [{client.surname}]"
                ).capitalize()
                db.Clients.modify(client.dni, name, surname)
                print("[+] Client modified")
            else:
                print("[-] Client not found")

        elif option == "5":
            print("Deleting client...\n")
            dni = None
            while True:
                dni = helpers.read_text(3, 3, "[-] DNI (2 int, 1 char)").upper()
                if helpers.dni_validate(dni, db.Clients.clientsList):
                    break
            (
                print("[+] Client deleted correctly")
                if db.Clients.delete(dni)
                else print("[-] Client not found")
            )

        elif option == "6":
            break

        input("\nPress ENTER to continue...")
