import os
import platform


def clean_screen():
    os.system("cls") if platform.system() == "Windows" else os.system("clear")


def read_text(length_min=0, length_max=100, message=None):
    print(message) if message else None

    while True:
        text = input("> ")
        if len(text) >= length_min and len(text) <= length_max:
            return text
