import re
import os
import platform


def clean_screen():
    os.system("cls") if platform.system() == "Windows" else os.system("clear")


def read_text(length_min=0, length_max=100, message=None):
    while True:
        text = input("> ")
        if length_min <= len(text) <= length_max:
            return text
        else:
            print(message)


def dni_validate(dni):
    if not re.match("[0-9]{2}[A-Z]$", dni):
        print("[-] Incorrect DNI format")
        return False
    return True


def ultimate_dni_validate(dni, clientsList):
    basic_validation = dni_validate(dni)
    if basic_validation:
        for client in clientsList:
            if client.dni == dni:
                print("[-] This DNI is already in use")
                return False
        return True
    else:
        return False
