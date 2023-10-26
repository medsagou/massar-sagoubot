import time

from selenium.webdriver.common.by import By
from print_sagou import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

    def get_classes_from_classes_page(self):
        return

    def list_of_each_class(self):
        searchBtn = self.driver.find_element(By.ID, "btnSearch")

        TypeEnseignement = self.driver.find_element(By.ID, "TypeEnseignement")
        TypeEnseignement_all_options = TypeEnseignement.find_elements(By.TAG_NAME, "option")
        TypeEnseignement_Select = Select(TypeEnseignement)

        for TypeEnseignement_option in TypeEnseignement_all_options:
            TypeEnseignement_Select.select_by_value(TypeEnseignement_option.get_attribute("value"))

            Cycle = self.driver.find_element(By.ID, "Cycle")
            Cycle_all_options = Cycle.find_elements(By.TAG_NAME, "option")

            Cycle_Select = Select(Cycle)

            for Cycle_option in Cycle_all_options:
                Cycle_Select.select_by_value(Cycle_option.get_attribute("value"))

                Niveau = self.driver.find_element(By.ID, "Niveau")
                Niveau_all_options = Niveau.find_elements(By.TAG_NAME, "option")
                Niveau_Select = Select(Niveau)

                for Niveau_option in Niveau_all_options:
                    Niveau_Select.select_by_value(Niveau_option.get_attribute("value"))

                    Classe = self.driver.find_element(By.ID, "Classe")
                    Classe_all_options = Classe.find_elements(By.TAG_NAME, "option")
                    Classe_Select = Select(Classe)

                    for Classe_option in Classe_all_options:
                        Classe_Select.select_by_value(Classe_option.get_attribute("value"))
                        searchBtn.click()
                        try:
                            WebDriverWait(self.driver, 3).until(
                                EC.invisibility_of_element_located(
                                    (
                                        By.ID, "loadingDiv",
                                    )
                                )
                            )
                        except:
                            continue
        return

    def get_class_list(self):
        main_xpath = '/html/body/div/div[1]/div[2]/div[2]/section[2]/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/table'
        try:
            table = self.driver.find_elements(By.XPATH, main_xpath)
        except:
            print_error("WE COULD NOT FIND YOUR CLASS List")
            return False
        else:
            # to continue here

                #export to les_class-ed_num.txt
                class_etd_File = C_File(file_name="db/les_class_etd_num.txt")
                class_etd_File.dict_to_file(D)

                #export to menu.txt
                ch = "001"
                for c, v in D.items():
                    ch = str(ch) + ";" + str(c) + "+" + str(v)

                class_etd_to_menu = C_File(file_name="db/menu.txt")
                class_etd_to_menu.str_to_fichier(ch)

                return D

    def main_list_reader(self):
        self.get_list_page()
        self.list_of_each_class()
        return

