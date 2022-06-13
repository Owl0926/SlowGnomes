import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from Rejestracja.Field import *


class Green(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--zoom")

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

    def collect(self):
        # self.driver.find_element(By.ID, Field.garden_collect).click()
        self.move_cursor_collect()

    def water(self):
        self.driver.find_element(By.ID, Field.garden_water).click()
        self.move_cursor_water()

    def move_cursor_collect(self):
        for c in range(1, 205):
            self.driver.find_element(By.ID, Field.garden_collect).click()
            garden_tile_cursor = 'gardenTile' + str(c) + '_cursor'
            field = self.driver.find_element(By.ID, garden_tile_cursor)
            ActionChains(self.driver, duration=5).move_to_element(field).perform()
            if str(2) in field.get_attribute('alt'):
                field.click()
            elif '3' in field.get_attribute('alt'):
                field.click()
            elif '4' in field.get_attribute('alt'):
                field.click()

    def move_cursor_water(self):
        for c in range(1, 205):
            garden_tile_cursor = 'gardenTile' + str(c) + '_cursor'
            field = self.driver.find_element(By.ID, garden_tile_cursor)
            ActionChains(self.driver, duration=0).move_to_element(field).perform()
            if Field.cursor_garden_water in field.get_attribute('class'):
                field.click()

    def move_cursor_plant(self):
        for c in range(1, 205):
            garden_tile_cursor = 'gardenTile' + str(c) + '_cursor'
            field = self.driver.find_element(By.ID, garden_tile_cursor)
            ActionChains(self.driver, duration=0).move_to_element(field).perform()
            if Field.cursor_plant in field.get_attribute('class'):
                field.click()

    def plant(self):
        kapusta = self.driver.find_element(By.ID, 'regal_6')
        # marchew = self.driver.find_element(By.ID, 'regal_6')
        # rzodkiew = self.driver.find_element(By.ID, 'regal_14')
        # pomidor = self.driver.find_element(By.ID, 'regal_5')
        # ogorek = self.driver.find_element(By.ID, 'regal_12')
        # truskawka = self.driver.find_element(By.ID, 'regal_3')
        kapusta.click()
        self.move_cursor_plant()

    def gnome_message(self):
        self.driver.find_element(By.XPATH, Field.communicate_gnome)

    # def test_collect(self):
    #     self.login()
    #     self.collect()

    def test_complex(self):
        print("login")
        self.login()
        print("colllect")
        self.collect()
        print("plant")
        self.plant()
        print("water")
        self.water()
    #
    # def test_plant(self):
    #     self.login()
    #     self.plant()
    #
    # def test_water(self):
    #     self.login()
    #     self.water()