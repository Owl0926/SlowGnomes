class Field:
    # Garden
    garden_collect = 'ernten'
    garden_water = 'giessen'
    cursor_garden_water = 'cursor-giessen'
    cursor_plant = 'cursor-pflanzen-v'
    auto_collect_gnome = "//div[@class='link harvest']"
    can_plant = "//div[contains(@style, 'background:url(https://wurzelimperium.wavecdn.net/pics/produkte/0.gif)')]/.."
    collect = "//div[substring(@style, string-length(@style) - string-length('_04.gif)') + 1) = '_04.gif)']/.."
    collect_fail_event = "//div[@id='baseDialogButton']/div[2]"
    collect_success_exit = "//div[@id='ernte_log']/img"
    # Other gardens
    travel_garden = "citymap_location_garden"
    city_map = "citymap"
    garden_1 = "//div[@id='citymap_location_garden1']"
    garden_2 = "//div[@id='citymap_location_garden2']"
    bike = "wimpareaCar"
    # to weed

    weed = "//div[contains(@style, 'background:url(https://wurzelimperium.wavecdn.net/pics/produkte/unkraut_04.gif)')]/.."
    rock = "//div[contains(@style, 'background:url(https://wurzelimperium.wavecdn.net/pics/produkte/steine_04.gif)')]/.."
    stump = "//div[contains(@style, 'background:url(https://wurzelimperium.wavecdn.net/pics/produkte/baumstumpf_04.gif)')]/.."
    mole = "//div[contains(@style, 'background:url(https://wurzelimperium.wavecdn.net/pics/produkte/maulwurf_04.gif)')]/.."

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
    logged_logout = "logout"
    back_to_homePage = "//input[@value='Powrót do strony startowej']"

    # Login
    homePage = "https://zieloneimperium.pl"
    login_user = 'login_user'
    login_password = 'login_pass'
    login_user2 = 'zdADUugwD'
    login_password2 = 'Z,;`S'
    login_button = 'submitlogin'
    login_server = 'login_server'

    # Client
    red_plants = "//div[@id='wimpVerkaufProducts']/div[@class='rot']"
    blue_plants = "//div[@id='wimpVerkaufProducts']/div[@class='blau']"
    client_accept = "wimpVerkaufYes"
    client = "//div[@id='wimpareaWimps']/img"
    client_want = "//div[@id='wimpVerkaufProducts']/div"
    decision_later = "wimpVerkaufLater"
    later_button = "wimpVerkaufLater"

    # Regal
    regal = "//div[@id='regal']/div"
    to_sow = "//div[@id='lager_name']"

    # Close tabs
    garden_cookies = "//div/a[@class='cookiemon-btn cookiemon-btn-accept']"
    daily_symbol = "dailyloginbonus_symbol"
    close_reward_button = "//div[@onclick='dailyloginbonus.close()']"
    claim_reward = "//div[@id='dailyloginbonus_button']//div[2]"
    new_offer = "//div[@id='newszwergLayer']/img"
    new_tab = "//div[@id='newszwergLayerAdNaviRight']"
