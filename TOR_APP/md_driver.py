import md_devices_gen

from selenium import webdriver
from selenium_stealth import stealth
import time
import cnf_bvb
import emoji







def build_driver(sizee):
        # whi=
        # options.add_argument("--headless")

        options = webdriver.ChromeOptions()
        # options.add_argument("--start-maximized")
        # options.add_argument("--start-maximized")
        options.add_argument("window-size="+sizee)
        # chrome_options.add_argument('--proxy-server=%s' % hostname + ":" + port)
        options.add_argument("--proxy-server=socks5://127.0.0.1:9050")

        # options.add_argument( "--user-data-dir=profile")
        options.add_argument('--disable-blink-features=AutomationControlled')
        # options.add_argument("--lang=fr")
        # options.add_argument(cnf.user_agent)
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        driver = webdriver.Chrome(options=options, executable_path="/usr/bin/chromedriver")
        ua=cnf_bvb.user_agent
        vendor,randerer,platfom=md_devices_gen.mokking(ua)

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