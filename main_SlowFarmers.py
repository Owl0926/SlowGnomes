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
        # After disable cookies automate logout
        # chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.cookies": 2})

        s = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=s, chrome_options=chrome_options)
        self.driver.get(Field.homePage)
        self.driver.delete_all_cookies()

    def login(self, login, password, server):
        self.driver.find_element(By.ID, Field.login_user).send_keys(login)
        self.driver.find_element(By.ID, Field.login_password).send_keys(password)
        select = Select(self.driver.find_element(By.ID, Field.login_server))
        select.select_by_index(server-1)
        self.driver.find_element(By.ID, Field.login_button).click()
        sleep(2)
        self.driver.find_element(By.XPATH, Field.garden_cookies).click()

    def faster_collect(self):
        self.driver.find_element(By.ID, Field.garden_collect).click()
        for x in range(2, 8):
            for i in self.driver.find_elements(By.XPATH, "//div[@id='gardenDiv']/div/img[2][@alt="+str(x)+"]"):
                i.click()
        # for i in self.driver.find_elements(By.XPATH, Field.alt2):
        #     i.click()
        # for i in self.driver.find_elements(By.XPATH, Field.alt3):
        #     i.click()
        # for i in self.driver.find_elements(By.XPATH, Field.alt4):
        #     i.click()
        # for i in self.driver.find_elements(By.XPATH, Field.alt5):
        #     i.click()
        # for i in self.driver.find_elements(By.XPATH, Field.alt6):
        #     i.click()

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

    def water(self):
        self.driver.find_element(By.ID, Field.garden_water).click()
        for c in range(1, 205):
            garden_tile_cursor = 'gardenTile' + str(c) + '_cursor'
            field = self.driver.find_element(By.ID, garden_tile_cursor)
            ActionChains(self.driver, duration=0).move_to_element(field).perform()
            if Field.cursor_garden_water in field.get_attribute('class'):
                field.click()

    def plant(self):
        for c in range(1, 205):
            garden_tile_cursor = 'gardenTile' + str(c) + '_cursor'
            field = self.driver.find_element(By.ID, garden_tile_cursor)
            ActionChains(self.driver, duration=0).move_to_element(field).perform()
            if Field.cursor_plant in field.get_attribute('class'):
                field.click()

    def regal_check_and_client_check(self):
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
        #  Koniec obslugiwania klientow
        print("need_list:", set(need_list))
        regal = self.driver.find_elements(By.XPATH, Field.regal)
        stan = {}
        d = 1 + len(regal)
        for _ in regal:  # collect all items from regal and add to list
            d -= 1  # decrement regal item
            item = self.driver.find_element(By.XPATH, "//div[@id='regal']/div[" + str(d) + "]")  # regal
            ActionChains(self.driver, 50).move_to_element(item).click().perform()  # take information from regal
            zasiej_name = self.driver.find_element(By.XPATH, Field.zasiej_window).text  # take info from zasiej
            stan[zasiej_name] = item.get_attribute('id')  # add to dictionary product from regal

        print("Stan", stan)
        normal_garden = self.driver.find_element(By.XPATH,"//div[@id='stockSwitches']/div[@class='normal active']")
        normal_garden.click()
        clear_n = []
        for i in need_list:  # compare regal and client wants
            if i not in clear_n:
                clear_n.append(i)
        print("We can plant:")
        for i in stan:
            if i in clear_n:
                print(i, "and his ID", stan.get(i))
                ba = self.driver.find_element(By.ID, stan.get(i))
                ba.click()
                self.plant()
                sleep(1)
                print("after plant")
        else:
            print("Brak : ",clear_n, "na stanie")

    def close_tabs(self):
        new_offer = self.driver.find_element(By.XPATH, Field.new_offer)
        sleep(1)
        if new_offer.is_displayed():
            new_offer.click()
        close_offer_button = self.driver.find_element(By.XPATH, Field.close_offer)
        special_offer = self.driver.find_element(By.ID, Field.special_offer)
        if special_offer.is_displayed():
            close_offer_button.click()
            print("Special offer closed")
        #  Daily
        daily_symbol = self.driver.find_element(By.ID, Field.daily_symbol)
        close_reward_button = self.driver.find_element(By.XPATH, Field.close_reward_button)
        claim_reward = self.driver.find_element(By.XPATH, Field.claim_reward)
        daily_symbol.click()
        if claim_reward.is_displayed():
            claim_reward.click()
            print("Reward claimed")
            sleep(1)
            close_reward_button.click()
        else:
            close_reward_button.click()
            print("Reward not claimed")

    def test_complex(self):
        self.login(login='helloworld', password='helloworld2', server=20)
        # self.close_tabs()
        self.faster_collect()
        self.regal_check_and_client_check()
        self.driver.find_element(By.ID, "regal_32").click()
        self.plant()
        self.water()
