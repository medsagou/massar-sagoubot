from print_sagou import *
from Menu import  Menu


class User_Interface:
    def main_page(self, Class_Dict):
        print("Votre Classes :")
        print("{:<12} {:<12}".format("Class", "Nombre des etudiants"))
        print_dict(Class_Dict)
        return

    def main_menu(self):
        start_menu = Menu(menu_index = 0)
        return start_menu.print_menu()


