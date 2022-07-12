import unittest
from time import sleep
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import wait
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from Field import *
from Generator import *


class Register(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-extensions")

        s = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=s, chrome_options=chrome_options)
        self.driver.get(Field.homePage)

    def register(self, login, password, garden_name, email):
        self.driver.find_element(By.XPATH, Field.homePage_Register).click()
        select_server = Select(self.driver.find_element(By.ID, Field.register_Server))
        select_server.select_by_value('server21')
        self.driver.find_element(By.XPATH, Field.register_Login).send_keys(login)
        self.driver.find_element(By.XPATH, Field.register_Password).send_keys(password)
        self.driver.find_element(By.XPATH, Field.register_GardenName).send_keys(garden_name)
        self.driver.find_element(By.XPATH, Field.register_Email).send_keys(email)
        self.driver.find_element(By.XPATH, Field.register_CheckBox).click()
        self.driver.find_element(By.XPATH, Field.register_Button).click()

    def login(self, user, password):
        self.driver.find_element(By.ID, Field.login_user).send_keys(user)
        self.driver.find_element(By.ID, Field.login_password).send_keys(password)
        select = Select(self.driver.find_element(By.ID, Field.login_server))
        select.select_by_index(20)
        self.driver.find_element(By.ID, Field.login_button).click()
        sleep(2)
    def How_much_account(self, x):
        def write_json(new_data, filename='json_data.json'):
            with open(filename, 'r+') as file:
                file_data = json.load(file)
                file_data["user_details"].append(new_data)
                file.seek(0)
                json.dump(file_data, file, ensure_ascii=False, indent=4)

        for y in range(0, x):
            sgen_login = get_random_string(9)
            sgen_password = get_random_password(5)
            sgen_garden_name = get_random_string(11)
            sgen_email = get_random_string(7) + "@gmailx.com"
            self.register(sgen_login, sgen_password, sgen_garden_name, sgen_email)
            data = {
                'login': sgen_login,
                'password': sgen_password,
                'gardenName': sgen_garden_name,
                'email': sgen_email
            }
            write_json(data)
            self.driver.find_element(By.ID, Field.logged_logout).click()
            self.driver.find_element(By.XPATH, Field.back_to_homePage).click()

    def test_fail_register(self):
        self.register('helloworld36', 'helloworld369', 'helloworld369', 'helloworld@369.pl')
        self.driver.find_element(By.XPATH, Field.register_Error)
        sleep(1)

    def test_register_single_generated(self):
        self.register(gen_login, gen_password, gen_gardenName, gen_email)
        print("Created account login :", gen_login, "\n password: ", gen_password)
        sleep(1)

    def test_multiple_register(self):
        self.How_much_account(2)

    def test_login_json(self):
        f = open('json_data.json')
        data = json.load(f)
        for i in data['user_details']:
            print(i['login'], i['password'])
            self.login(i['login'], i['password'])
            # wait.WebDriverWait((self.driver.find_element(By.ID,Field.logged_logout)), 50)
            self.driver.find_element(By.ID, Field.logged_logout).click()
            self.driver.find_element(By.XPATH, Field.back_to_homePage).click()
        f.close()
