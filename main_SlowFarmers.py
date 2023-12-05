import random
import time
import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from Rejestracja.Field import *


class Green(unittest.TestCase):

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        s = Service()

        self.driver = webdriver.Chrome(service=s, chrome_options=chrome_options)
        self.driver.get(Field.homePage)
        self.driver.delete_all_cookies()
        assert self.driver.current_url == "https://zieloneimperium.pl/"

    def login(self, login, password, server):
        self.driver.find_element(By.ID, Field.login_user).send_keys(login)
        self.driver.find_element(By.ID, Field.login_password).send_keys(password)
        select = Select(self.driver.find_element(By.ID, Field.login_server))
        select.select_by_index(server - 1)
        self.driver.find_element(By.ID, Field.login_button).click()
        sleep(1)
        self.driver.find_element(By.XPATH, Field.garden_cookies).click()

    def Collect(self):
        for x in range(2, 8):
            self.driver.find_element(By.ID, Field.garden_collect).click()
            z = 0
            for i in self.driver.find_elements(By.XPATH, "//div[@id='gardenDiv']/div/img[2][@alt=" + str(x) + "]"):
                self.driver.find_element(By.ID, Field.garden_collect).click()
                i.click()
                z += 1
                event = self.driver.find_element(By.XPATH,"//div[@id='baseDialogButton']/div[2]")
                if event.is_displayed():
                    event.click()
                else:
                    pass

            print("For", x, "alts. Collected", z, "plants")

    def Water(self):
        self.driver.find_element(By.ID, Field.garden_water).click()
        for c in range(1, 205):
            garden_tile_cursor = 'gardenTile' + str(c) + '_cursor'
            field = self.driver.find_element(By.ID, garden_tile_cursor)
            ActionChains(self.driver, duration=0).move_to_element(field).perform()
            if Field.cursor_garden_water in field.get_attribute('class'):
                field.click()

    def Plant(self):
        h = 0
        for c in range(1, 205):
            garden_tile_cursor = 'gardenTile' + str(c) + '_cursor'
            field = self.driver.find_element(By.ID, garden_tile_cursor)
            ActionChains(self.driver, duration=0).move_to_element(field).perform()
            if Field.cursor_plant in field.get_attribute('class'):
                field.click()
                h += 1
        print("\n -> " + str(h) + " <- planted")

    def client_needs(self):
        clients = self.driver.find_elements(By.XPATH, Field.client)
        need_list = []
        for x in clients:
            self.driver.find_element(By.ID, x.get_attribute('id')).click()  # click on every client
            client_list = self.driver.find_elements(By.XPATH, Field.client_want)
            for z in client_list:
                if z.get_attribute('class') == 'rot':
                    need_list.append(z.text.split()[2])
        later_button = self.driver.find_element(By.ID, Field.decision_later)
        later_button.click()
        print("Need_list:", set(need_list))
        print("We have:")
        check_regal = self.driver.find_elements(By.XPATH, Field.regal)
        d = 1 + len(check_regal)
        stan = {}
        for _ in check_regal:
            d -= 1  # decrement regal item
            item = self.driver.find_element(By.XPATH, "//div[@id='regal']/div[" + str(d) + "]")  # regal
            ActionChains(self.driver, 50).move_to_element(item).click().perform()  # take information from regal
            zasiej_name = self.driver.find_element(By.XPATH, Field.zasiej_window).text  # take info from zasiej
            stan[zasiej_name] = item.get_attribute('id')  # add to dictionary product from regal
            # print(zasiej_name, "id", stan[zasiej_name], "ilosc:", item.text)
            product = str(stan[zasiej_name])
            if zasiej_name in need_list:
                print("Planted", zasiej_name.center(100, "="))
                plant_remaming = self.driver.find_element(By.XPATH, '//div[@id="regal"]/div[@id="' +
                                                                  product + '"]')
                plant_remaming.click()
                self.Plant()

    def close_pop_up(self):
        if self.driver.find_element(By.XPATH, Field.new_tab).is_displayed():
            self.driver.find_element(By.XPATH, Field.new_offer).click()
        daily_symbol = self.driver.find_element(By.ID, Field.daily_symbol)
        close_reward_button = self.driver.find_element(By.XPATH, Field.close_reward_button)
        claim_reward = self.driver.find_element(By.XPATH, Field.claim_reward)
        daily_symbol.click()
        if claim_reward.is_displayed():
            claim_reward.click()
            sleep(1)
            close_reward_button.click()
        else:
            close_reward_button.click()

    def client_accept(self):
        click_on_client = self.driver.find_elements(By.XPATH, Field.client)
        for x in click_on_client:
            self.driver.find_element(By.ID, x.get_attribute('id')).click()  # click on every client
            self.driver.find_element(By.ID, Field.client_accept).click()

    def Start(self):
        # Uncomment and fill your credentials
        # self.login(login='', password='', server=)
        self.close_pop_up()

    def tearDown(self):
        self.driver.quit()

    def random_plant(self):
        random_number = random.randint(1, 20)
        random_plant = self.driver.find_element(By.XPATH, '//div[@id="regal"]/div[' + str(random_number) + ']')
        random_plant.click()
        self.Plant()
        self.Water()

    def test_complex_1(self):
        self.Start()
        self.Collect()
        self.client_accept()

    def test_complex_2(self):
        self.Start()
        self.client_needs()
        self.random_plant()
