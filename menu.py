import os


def start():
    while True:
        os.system("clear")

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
        os.system("clear")

        if option == "1":
            print("Listing clients...\n")
        elif option == "2":
            print("Searching client...\n")
        elif option == "3":
            print("Adding client...\n")
        elif option == "4":
            print("Modifying client...\n")
        elif option == "5":
            print("Deleting client...\n")
        elif option == "6":
            break

        input("\nPress ENTER to continue...")
