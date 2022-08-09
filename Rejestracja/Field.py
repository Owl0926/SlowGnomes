
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
    login_user2 = 'zdADUugwD'
    login_password2 = 'Z,;`S'
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

    # Collect by alt

    alt2 = "//div[@id='gardenDiv']/div/img[2][@alt=2]"
    alt3 = "//div[@id='gardenDiv']/div/img[2][@alt=3]"
    alt4 = "//div[@id='gardenDiv']/div/img[2][@alt=4]"
    alt5 = "//div[@id='gardenDiv']/div/img[2][@alt=5]"
    alt6 = "//div[@id='gardenDiv']/div/img[2][@alt=6]"

    # Client
    red_plants = "//div[@id='wimpVerkaufProducts']/div[@class='rot']"
    blue_plants = "//div[@id='wimpVerkaufProducts']/div[@class='blau']"
    client_accept = "wimpVerkaufYes"
    client = "//div[@id='wimpareaWimps']/img"
    client_want = "//div[@id='wimpVerkaufProducts']/div"
    decision_later = "wimpVerkaufLater"

    # Regal
    regal = "//div[@id='regal']/div"
    zasiej_window = "//div[@id='lager_name']"

    # Close tabs
    daily_symbol = "dailyloginbonus_symbol"
    close_reward_button = "//div[@onclick='dailyloginbonus.close()']"
    claim_reward = "//div[@id='dailyloginbonus_button']//div[2]"
    close_offer = "//div[@onclick='specialoffer.close()']"
    special_offer = "specialoffer"
    new_offer = "//div[@id='newszwergLayer']/img"

