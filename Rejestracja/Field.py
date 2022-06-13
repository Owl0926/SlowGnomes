
class Field:
    homePage = "https://zieloneimperium.pl"
    # Register
    homePage_Register = "//a[@class='register link']"
    register_Server = "reg_selectserver"
    register_Login = "//tr/td/input[@name='login'][@tabindex=51]"
    register_Password = "//tr/td/input[@tabindex=52]"
    register_GardenName = "//tr/td/input[@tabindex=53]"
    register_Email = "//tr/td/input[@tabindex=54]"
    register_CheckBox = "//tr/td/input[@tabindex=55]"
    register_Button = "//tr/td/input[@tabindex=56]"
    register_Error = "//div[@id='infolayer_text']/div[1]"
    # Login
    login_user = 'login_user'
    login_password = 'login_pass'
    login_button = 'submitlogin'
    username_main_20 = 'helloworld'
    password_main_20 = 'helloworld2'
    login_server = 'login_server'

    back_to_homePage = "//input[@value='Powrót do strony startowej']"

    # Garden
    garden_cookies = "//div/a[@class='cookiemon-btn cookiemon-btn-accept']"
    garden_collect = 'ernten'
    garden_water = 'giessen'
    cursor_garden_water = 'cursor-giessen'
    communicate_gnome = "//*[@id='sprcontent']/div/span[4]"
    cursor_plant = 'cursor-pflanzen-v'
    logged_logout = "logout"
    wyrywanie_chwasta = "//div[normalize-space()='Koszt: 2,50 kt']"

    # Klient
    red_plants = "//div[@id='wimpVerkauf']/div[4]/div[@class='rot']"
    client = "//div[@id='wimpareaWimps']/div[@id='blasei5']"
    client_by_img = "//img[@id='i5']"
    client_accept = "wimpVerkaufYes"
    client_count = "//div[@id='wimpareaWimps']/img"