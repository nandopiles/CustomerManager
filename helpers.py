import os
import platform


def clean_screen():
    os.system("cls") if platform.system() == "Windows" else os.system("clear")
