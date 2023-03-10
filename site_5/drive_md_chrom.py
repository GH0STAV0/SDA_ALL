from selenium import webdriver
from selenium_stealth import stealth
import time
import cnf_bvb
import emoji
import extt
import devices_gen

# extt.fuckk.extend((str(sz)))

# print(extt.fuckk)
# input('')




def build_driver(sizee):
        # whi=
        # options.add_argument("--headless")
        # options.add_argument("--start-maximized")
        # options.add_argument("--start-maximized")
        # options.add_argument( "--user-data-dir=profile")
        # options.add_argument("--lang=fr")
        # options.add_argument(cnf.user_agent)

        options = webdriver.ChromeOptions()

        options.add_argument("window-size="+sizee)

        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument("--incognito")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        prefs = {"credentials_enable_service": False,"profile.password_manager_enabled": False}
        options.add_experimental_option("prefs", prefs)

        driver = webdriver.Chrome(options=options, executable_path="/usr/bin/chromedriver")
        ua=cnf_bvb.user_agent
        vendor,randerer,platfom=devices_gen.mokking(ua)

        stealth(driver,
                user_agent=ua,
                # languages=["en-US", "en"],
                vendor="Google Inc.",
                platform=platfom,
                webgl_vendor=vendor,
                renderer=randerer,
                fix_hairline=True,
                )
        # driver.set_window_size(1024, 600)
        # driver.maximize_window()
        # driver.manage().window().maximize()
        extt.fuckk.extend((sizee,ua,platfom,vendor,randerer))
        # print(extt.fuckk)
        # input('')
        print(emoji.emojize("Ok [ "+sizee+" ] [ "+vendor+randerer+platfom+"]"' :check_mark_button: :alien:'))
        return driver
        # url = "https://bot.sannysoft.com/"
        # driver.get(url)

        # input("")
        # url='https://accounts.google.com/servicelogin'

        # driver.get(url)
        # time.sleep(5)
        # input("")
        # driver.quit()