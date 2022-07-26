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
        # After disable cookies automate loggout
        # chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.cookies": 2})

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
        self.move_cursor_collect()

    def water(self):
        self.driver.find_element(By.ID, Field.garden_water).click()
        self.move_cursor_water()

    def faster_collect(self):
        self.driver.find_element(By.ID, Field.garden_collect).click()
        sleep(1)
        for i in self.driver.find_elements(By.XPATH, Field.alt2):
            i.click()
            self.kropelka_check()
        for i in self.driver.find_elements(By.XPATH, Field.alt3):
            i.click()
            self.kropelka_check()
        for i in self.driver.find_elements(By.XPATH, Field.alt4):
            i.click()
            self.kropelka_check()
        for i in self.driver.find_elements(By.XPATH, Field.alt5):
            i.click()
            self.kropelka_check()
        for i in self.driver.find_elements(By.XPATH, Field.alt6):
            i.click()
            self.kropelka_check()

    def kropelka_check(self):
        basedialog = self.driver.find_element(By.ID, "baseDialogBgTL")
        button_basedialog = self.driver.find_element(By.ID, "baseDialogButton")
        if basedialog.is_displayed():
            sleep(2)
            button_basedialog.click()
            print("kkk")
            
    def move_cursor_collect(self):
        for c in range(1, 205):
            self.driver.find_element(By.ID, Field.garden_collect).click()
            garden_tile_cursor = 'gardenTile' + str(c) + '_cursor'
            field = self.driver.find_element(By.ID, garden_tile_cursor)
            ActionChains(self.driver, duration=0).move_to_element(field).perform()
            if str(2) in field.get_attribute('alt'):
                field.click()
            elif '3' in field.get_attribute('alt'):
                field.click()
            elif '4' in field.get_attribute('alt'):
                field.click()
            elif '5' in field.get_attribute('alt'):
                field.click()
            elif '6' in field.get_attribute('alt'):
                field.click()
            elif '7' in field.get_attribute('alt'):
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
        collect_number = self.driver.find_element(By.ID, 'regal_49')
        collect_number.click()
        self.move_cursor_plant()

        # NEW ============================================================================================
    def daily_login_bonus(self):
        daily_symbol = self.driver.find_element(By.ID, "dailyloginbonus_symbol")
        close_reward_button = self.driver.find_element(By.XPATH, "//div[@onclick='dailyloginbonus.close()']")
        claim_reward = self.driver.find_element(By.XPATH, "//div[@id='dailyloginbonus_button']//div[2]")
        sleep(1)
        daily_symbol.click()
        if claim_reward.is_displayed():
            claim_reward.click()
            print("Reward claimed")
            close_reward_button.click()
        else:
            close_reward_button.click()
            print("Reward not claimed")

    def special_offer(self):
        close_offer_button = self.driver.find_element(By.XPATH, "//div[@onclick='specialoffer.close()']")
        special_offer = self.driver.find_element(By.ID, "specialoffer")
        if special_offer.is_displayed():
            close_offer_button.click()
            print("Special offer closed")

    def test_complex(self):
        self.login()
        self.special_offer()
        self.daily_login_bonus()
        self.faster_collect()
        self.plant()
        self.water()
