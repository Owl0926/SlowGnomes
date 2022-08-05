import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from Rejestracja.Field import Field

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

    def test_regalcheck_and_clientcheck(self):
        self.login()
        klienci = self.driver.find_elements(By.XPATH, "//div[@id='wimpareaWimps']/img")
        need_list = []
        for x in klienci:
            self.driver.find_element(By.ID, x.get_attribute('id')).click()  # przeklikuje klientow
            list = self.driver.find_elements(By.XPATH, "//div[@id='wimpVerkaufProducts']/div")
            for z in list:
                if z.get_attribute('class') == 'rot':
                    need_list.append(z.text.split()[2])
        print("need_list:", set(need_list))
        regal = self.driver.find_elements(By.XPATH, "//div[@id='regal']/div")
        stan = {}
        d = 1 + len(regal)
        for _ in regal:  # zbiera wszystkie przedmioty z regalu i wpisuje je do tablicy
            d -= 1  # dekrementacja
            kielich = self.driver.find_element(By.XPATH, "//div[@id='regal']/div[" + str(d) + "]")  # regal
            ActionChains(self.driver, 50).move_to_element(kielich).click().perform()  # przeklikanie regalu

            zasiej_name = self.driver.find_element(By.XPATH, "//div[@id='lager_name']").text  # zebrabnie info z ZASIEJ
            stan[zasiej_name] = kielich.get_attribute('id')  # dodanie do dicta produkt z regalu oraz
        print("Stan", stan)
        clear_n = []
        for i in need_list:
            if i not in clear_n:
                clear_n.append(i)
        # print("need_list",clear_n)
        print("Mozemy zasadzic")

        for i in stan:
            if i in clear_n:
                # self.driver.find_element(By.ID,stan.get(i)).click
                print(i,"i jego id",stan.get(i))
                ba = self.driver.find_element(By.ID,stan.get(i))
                ba.click()
                sleep(5)
