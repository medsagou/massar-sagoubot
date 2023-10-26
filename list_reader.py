
from selenium.webdriver.common.by import By
from print_sagou import print_info, print_error, print_success

class List_Reader():

    def __int__(self, driver=""):
        self.driver = driver


    def get_list_page(self):
        try:
            self.driver.get("https://massar.men.gov.ma/Evaluation/EspaceEnseignant/ListeEleves")
        except:
            print_error("We Can't find the list page! Close the program and try again.")
        else:
            print_info("GETTING TO THE LIST PAGE")

    def find_classes(self):
        return

    def list_of_each_class(self):
        return

    def main_list_reader(self):
        self.get_list_page()
        return

