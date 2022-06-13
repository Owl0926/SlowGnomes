import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from Rejestracja.Field import *


class Register(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-extensions")

        s = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=s, chrome_options=chrome_options)
        self.driver.get(Field.homePage)

    def login(self):
        self.driver.find_element(By.ID, Field.login_user).send_keys(Field.username_main_20)
        self.driver.find_element(By.ID, Field.login_password).send_keys(Field.password_main_20)
        select = Select(self.driver.find_element(By.ID, Field.login_server))
        select.select_by_index(19)
        self.driver.find_element(By.ID, Field.login_button).click()
        sleep(2)
        self.driver.find_element(By.XPATH, Field.garden_cookies).click()

    def test_client(self):
        self.login()
        clients = self.driver.find_element(By.XPATH, Field.client_count)
        for x in range(0, 9):  # fix it to get automate
            client_cursor = 'i'+str(x)
            self.driver.find_element(By.ID, client_cursor).click()
            self.driver.find_element(By.ID, Field.client_accept).click()
            need_to_plant = self.driver.find_element(By.XPATH, Field.red_plants).text
            print(need_to_plant.split()[2])

    def test_regal(self):
        self.login()
        for x in range(1, 8):
            print(str(x))
            print(self.driver.find_element(By.XPATH, "//div[@id='regal']/div["+str(x)+"]").id)
            self.driver.find_element(By.XPATH, "//div[@id='regal']/div["+str(x)+"]").click()
            # print(self.driver.find_element(By.XPATH, "//div[@id='regal']/div["+str(x)+"]"))
            sleep(1)
