# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 22:49:39 2023

@author: Pr. Sagou
"""
import os
import sys
from dotenv import load_dotenv
from print_sagou import print_info, print_error, print_success

import undetected_chromedriver_modified_sagou as ucg
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import chromedriver_autoinstaller



load_dotenv()  # loading the environment variables from the .env file


from class_fichier import C_Fichier


class Massar_Sagou:
    def __init__(self, driver = ""):
        self.driver=driver
        return

    def get_driver(self):
        opt = webdriver.FirefoxOptions()
        opt.add_argument("--start-maximized")
        # chromedriver_autoinstaller.install()
        # self.driver = webdriver.Firefox(options=opt)
        self.driver = ucg.Chrome()
        self.driver.maximize_window()
        print_success("DRIVER CONNECTED")
        return

    def get_site(self):
        try:
            self.driver.get(os.getenv("OFFICIAL_SITE"))
        except:
            print_error("WE CAN OPEN THE BROWSER")
            self.exit_program()
        else:
            print_info("SITE OPENED")
            return True


    def fill_username(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (
                        By.ID,"UserName",
                    )
                )
            )
        finally:
            username = self.driver.find_element(By.ID, "UserName")
            username.send_keys(os.getenv("EMAIL"))
            print_info("USERNAME FIELD DONE")
        return

    def fill_password(self):
        password = self.driver.find_element(By.ID, "Password")
        password.send_keys(os.getenv("PASSWORD"))
        print_info("PASSWORD FIELD DONE")
        return

    def submit_form(self):
        # submit the form
        sumbit_button = self.driver.find_element(By.ID, "btnSubmit")
        sumbit_button.click()
        print_info("BUTTON CLICKED")

        # checking if we've getting any error while submiting the form
        if not self.check_error_login():
            try:
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        (
                            By.ID, "sidebar-menu",
                        )
                    )
                )
            except:
                print_error("PLEASE CHECK YOUR LOGIN INFORMATION AND TRY AGAIN.")
                self.exit_program()
            else:
                print_success("WE HAVE SUCCESSFULLY LOGGED INTO YOUR ACCOUNT")
            return
        else:
            print_error("ERROR: PLEASE CHECK YOUR LOGIN INFORMATION AND TRY AGAIN.")
            self.exit_program()


    def check_error_login(self):
        try:
            WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located(
                    (
                        By.ID, "MsgError",
                    )
                )
            )
        except:
            return False
        else:
            return True


    def export_data(self):
        return

    def close_tab(self):
        self.driver.quit()
        return

    def exit_program(self):
        print_info("EXITING THE PROGRAM -- GOODBYE TEACHER --")
        self.driver.close()
        self.driver.quit()
        sys.exit()

    def main_interaction(self):
        self.get_driver()
        self.get_site()
        self.fill_username()
        self.fill_password()
        self.submit_form()
        #_____________________________
# end of Massar_Sagou class
