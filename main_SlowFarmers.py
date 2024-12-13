import random

import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utils.Field import *


class Green(unittest.TestCase):

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        s = Service()
        self.driver = webdriver.Chrome(executable_path='C:\chromedriver-win32\chromedriver.exe',
                                       chrome_options=chrome_options)
        self.driver.get(Field.homePage)
        self.driver.delete_all_cookies()
        assert self.driver.current_url == "https://zieloneimperium.pl/"
        self.Start()

    def tearDown(self):
        print("Zamykanie")
        sleep(5)
        self.driver.quit()

    def Start(self):
        """
        Method contains login and close_pop_up method
        :return:
        """
        # Uncomment and fill your credentials
        self.login(login='helloworld', password='helloworld2', server=20)
        self.close_pop_up()

    def close_pop_up(self):
        """
        Close every event pop-up window
        :return:
        """
        if self.driver.find_element(By.XPATH, Field.new_tab).is_displayed():
            self.driver.find_element(By.XPATH, Field.new_offer).click()
        close_reward_button = self.driver.find_element(By.XPATH, Field.close_reward_button)
        claim_reward = self.driver.find_element(By.XPATH, Field.claim_reward)
        self.driver.find_element(By.ID, Field.daily_symbol).click()
        if claim_reward.is_displayed():
            claim_reward.click()
            sleep(1)
            close_reward_button.click()
        else:
            close_reward_button.click()

    def login(self, login, password, server):
        """
        Login to account
        :param login:
        :param password:
        :param server:
        :return:
        """
        assert self.driver.find_element(By.ID, Field.login_user).is_displayed()
        assert self.driver.find_element(By.ID, Field.login_password).is_displayed()
        assert self.driver.find_element(By.ID, Field.login_server).is_displayed()
        assert self.driver.find_element(By.ID, Field.login_button).is_displayed()
        self.driver.find_element(By.ID, Field.login_user).send_keys(login)
        self.driver.find_element(By.ID, Field.login_password).send_keys(password)
        select = Select(self.driver.find_element(By.ID, Field.login_server))
        select.select_by_index(server - 1)
        self.driver.find_element(By.ID, Field.login_button).click()
        WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable((By.ID, Field.garden_collect)))
        self.driver.find_element(By.XPATH, Field.garden_cookies).click()

    def every_field(self):
        """
        Method used to plant and use water on every planted field
        :return:
        """
        for c in range(1, 205):
            garden_tile_cursor = 'gardenTile' + str(c) + '_cursor'
            field = self.driver.find_element(By.ID, garden_tile_cursor)
            ActionChains(self.driver).move_to_element(field).perform()
            if Field.cursor_garden_water in field.get_attribute('class') or Field.cursor_plant in field.get_attribute(
                    'class'):
                field.click()
    def collect_event(self):
        event = self.driver.find_element(By.XPATH, Field.collect_fail_event)
        event2 = self.driver.find_element(By.XPATH,Field.collect_success_exit)
        if event.is_displayed():
            event.click()
        elif event2.is_displayed():
            event2.click()
        else:
            pass
    def Collect(self):
        """
        Method used to gathering every ready plant
        :return:
        """
        for x in range(2, 8):
            assert self.driver.find_element(By.ID, Field.garden_collect).is_displayed()
            self.driver.find_element(By.ID, Field.garden_collect).click()
            z = 0
            for i in self.driver.find_elements(By.XPATH, "//div[@id='gardenDiv']/div/img[2][@alt=" + str(x) + "]"):
                self.driver.find_element(By.ID, Field.garden_collect).click()
                i.click()
                z += 1
                self.collect_event()

            print("\nFor", x, "alts. Collected", z, "plants")

    def pelana_automatyzacja(self):
        # self.alter_collect()
        # self.client_needs()
        # self.alter_moznasadzic()
        # self.random_plant()
        # self.alter_woda()
        # self.client_accept()
        self.travel_to_different_garden(2)
        self.alter_collect()
        self.client_needs()
        self.alter_moznasadzic()
        self.random_plant()
        self.alter_woda()
        self.client_accept()

    def Plant(self):
        """
        Method used to plant, if you use it only it will plant first item from your regal
        :return:
        """
        self.every_field()

    def client_needs(self):
        """
        Method used to gathering client needs, save to list. Planting items from needed list.
        :return:
        """
        clients = self.driver.find_elements(By.XPATH, Field.client)
        need_list = []
        for x in reversed(clients):
            self.driver.find_element(By.ID, x.get_attribute('id')).click()  # click on every client
            client_list = self.driver.find_elements(By.XPATH, Field.client_want)
            for z in client_list:
                if z.get_attribute('class') == 'rot':
                    need_list.append(z.text.split()[2])
        self.driver.find_element(By.ID, Field.decision_later).click()
        print("\nNeed_list:", set(need_list))
        print("We have:")
        check_regal = self.driver.find_elements(By.XPATH, Field.regal)
        d = 1 + len(check_regal)
        stan = {}
        duszka = []
        for _ in check_regal:
            d -= 1  # decrement regal item
            item = self.driver.find_element(By.XPATH, "//div[@id='regal']/div[" + str(d) + "]")  # regal
            ActionChains(self.driver, duration=0).move_to_element(
                item).click().perform()  # take information from regal
            zasiej_name = self.driver.find_element(By.XPATH, Field.zasiej_window).text  # take info from zasiej

            stan[zasiej_name] = item.get_attribute('id')  # add to dictionary product from regal

            print(zasiej_name, "id", stan[zasiej_name], "ilosc:", item.text)
            product = str(stan[zasiej_name])
            if zasiej_name in need_list:
                duszka.append(zasiej_name)
                if product == "regal_20":
                    # TODO naprawa 2 polowych sadzonek
                    print("Szparagi potrzebuja dw-och miejsc, na ten moment nie obslugujemy")
                    continue

                else:
                    print("Planted", zasiej_name.center(100, "="))
                    plant_remaning = self.driver.find_element(By.XPATH, '//div[@id="regal"]/div[@id="' +
                                                              product + '"]')
                    plant_remaning.click()
                    self.alter_moznasadzic()

        print("Klienci potrzebuja i możemy zasadzić", duszka)

    def client_accept(self):
        """
        Method check every client in queue, and accept them offerts.
        :return:
        """
        click_on_client = self.driver.find_elements(By.XPATH, Field.client)
        len(click_on_client)
        # dlugosc_kolejki = len(click_on_client)
        for x in reversed(click_on_client):
            # dlugosc_kolejki-=1
            self.driver.find_element(By.ID, x.get_attribute('id')).click()  # click on every client
            self.driver.find_element(By.ID, Field.client_accept).click()
        later_btn = self.driver.find_element(By.ID, Field.later_button)
        later_btn.click()

    def random_plant(self):
        # TODO czasem wybiera spoza listy, albo ilosc na regale wieksza niz maksymalne mozliwe
        """
        Method randomly pick plant to seed from you regal items.
        :return:
        """
        check_regal = self.driver.find_elements(By.XPATH, Field.regal)
        x = 1 + len(check_regal)
        random_number = random.randint(1, x)
        random_plant = self.driver.find_element(By.XPATH, '//div[@id="regal"]/div[' + str(random_number) + ']')
        random_plant.click()
        self.alter_moznasadzic()

    def alter_moznasadzic(self):
        #  TODO Sprawdic tak aby na sztywno nie podawac co ma sadzic, tylko ma przekazywac
        # self.driver.find_element(By.ID, "regal_6").click()
        for i in self.driver.find_elements(By.XPATH, Field.mozna_sadzic):
            i.click()

    def alter_collect(self):
        if self.driver.find_element(By.XPATH,Field.gnom_zbierajacy_plony).is_enabled():
            self.driver.find_element(By.XPATH, Field.gnom_zbierajacy_plony).click()
            sleep(2)
            self.collect_event()
        else:
            for x in range(2, 7):
                do_zebrania = self.driver.find_elements(By.XPATH,
                                                        "//div[substring(@style, string-length(@style) - string-length('_04.gif)') + 1) = '_04.gif)' and //img[@alt='" + str(
                                                            x) + "']]/..")
                for i in do_zebrania:
                    self.driver.find_element(By.ID, Field.garden_collect).click()
                    i.click()

    def alter_woda(self):
        self.driver.find_element(By.ID, Field.garden_water).click()
        for x in range(1, 4):
            do_podlania = self.driver.find_elements(By.XPATH,
                                                    "//div[substring(@style, string-length(@style) - string-length('_0" + str(
                                                        x) + ".gif)') + 1) = '_0" + str(x) + ".gif)']/..")
            for i in do_podlania:
                i.click()

    def plewienie(self):
        chwasty = [Field.chwast_2, Field.kamie_50, Field.pien_250, Field.kret_500]
        for z in chwasty:
            for x in self.driver.find_elements(By.XPATH, z):
                x.click()
                assert self.driver.find_element(By.ID, "baseDialogButton").is_displayed()
                btn_yes = self.driver.find_element(By.ID, "baseDialogButton")
                btn_yes.click()
                if self.driver.find_element(By.ID, "baseDialogButton").is_displayed():
                    btn_yes.click()
                else:
                    continue

    def travel_to_different_garden(self, garden_number):
        rower = self.driver.find_element(By.ID, Field.bike)
        rower.click()
        WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located((By.ID, Field.city_map)))
        travel_to_garden = self.driver.find_element(By.ID, Field.travel_garden + str(garden_number))
        travel_to_garden.click()
        WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located((By.ID, "gardenDiv")))
        sleep(2)

    def test_collect(self):
        self.alter_collect()

    def test_collect_2(self):
        self.travel_to_different_garden(2)
        self.alter_collect()

    def test_sadzenie(self):
        self.alter_moznasadzic()

    def test_woda(self):
        self.alter_woda()

    def test_zmiana_ogrodu(self):
        self.travel_to_different_garden(2)

    def test_sadzenie_2(self):
        self.travel_to_different_garden(2)
        self.alter_moznasadzic()

    def test_woda_2(self):
        self.travel_to_different_garden(2)
        self.alter_woda()

    def test_klikanie_klientow(self):
        self.client_needs()

    def test_klikanie_klientow_2(self):
        self.travel_to_different_garden(2)
        self.client_needs()

    def test_plewienia(self):
        self.plewienie()

    def test_plewienia_2(self):
        self.travel_to_different_garden(2)
        self.plewienie()
    def test_pelny(self):
        self.pelana_automatyzacja()