# It pains me to see so many imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent
import datetime
from waiting import wait
import random

user_agent = UserAgent()
rand_user = user_agent.random

# needed to bypass captcha
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'user-agent={rand_user}')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_argument('window-size={},{}'.format(random.randint(1000, 1920),
                                                       random.randint(720, 1080)))


class Login:
    def __init__(self):
        # init driver
        self.driver = webdriver.Chrome(ChromeDriverManager().install(),
                                       chrome_options=chrome_options)
        self.email = "coilettebendher@gmail.com"
        self.password = "thisisagenericpassword123"
        self.number = "2247898554"  # number to sign in

    def goto_site(self, site):
        # Used JS scripts to ensure that new windows could be opened
        # regardless of OS
        # Also this is hardcoded so not ideal
        if site == "tinder":
            self.driver.get("https://tinder.com")
        elif site == "google_voice":
            self.driver.execute_script("window.open('')")
            self.driver.switch_to.window(login.driver.window_handles[1])
            self.driver.get("https://voice.google.com/about")

    def login_driver(self):
        try:
            login_btn = WebDriverWait(self.driver, 50).until(
                EC.element_to_be_clickable(
                    (By.XPATH,
                     "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button/span")
                )
            )
            login_btn.click()

            login_by_num = login_btn = WebDriverWait(self.driver, 50).until(
                EC.element_to_be_clickable(
                    (By.XPATH,
                     "//*[@id=\"modal-manager\"]/div/div/div[1]/div/div[3]/span/div[3]/button/span[2]")
                )
            )
            login_by_num.click()

            enter_num = login_by_num = login_btn = WebDriverWait(self.driver, 50).until(
                EC.element_to_be_clickable(
                    (By.XPATH,
                     "/html/body/div[2]/div/div/div[1]/div[2]/div/input")
                )
            )
            enter_num.send_keys(self.number)

            continue_btn = login_by_num = login_btn = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(
                    (By.XPATH,
                     "/html/body/div[2]/div/div/div[1]/button/span")
                )
            )
            continue_btn.click()
        finally:
            pass

    def parse_time(self):
        stringify_time = datetime.datetime.now().strftime("%I:%M %p")
        return stringify_time[1:] if stringify_time[0] == "0" else stringify_time

    # TODO: finish this portion
    def grab_num_driver(self):
        try:
            login_btn = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(
                    (By.LINK_TEXT, "Sign in")
                )
            )
            login_btn.click()

            sign_in_field = WebDriverWait(self.driver, 35).until(
                EC.element_to_be_clickable(
                    (By.XPATH,
                     "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
                )
            )
            sign_in_field.send_keys(self.email)

            next_btn = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(
                    (By.XPATH,
                     "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]")
                )
            )
            next_btn.click()

            password_field = WebDriverWait(self.driver, 35).until(
                EC.element_to_be_clickable(
                    (By.XPATH,
                     "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
                )
            )
            password_field.send_keys(self.password)

            next_btn_two = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(
                    (By.XPATH,
                     "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]")
                )
            )
            next_btn_two.click()

            msg_btn = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(
                    (By.XPATH,
                     "/html/body/div[1]/div[2]/div[2]/gv-side-nav/div/div/gmat-nav-list/a[2]/div/div/span[2]")
                )
            )
            msg_btn.click()

            message = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(
                    (By.PARTIAL_LINK_TEXT,
                     "Your Tinder code is")
                )
            )
            message.click()
        finally:
            pass

    # last function to be called after the code sent to the number is grabbed
    def enter_tinder():
        pass


login = Login()
print(login.parse_time())
login.goto_site("tinder")
login.login_driver()
login.goto_site("google_voice")
login.grab_num_driver()
login.driver.switch_to.window(login.driver.window_handles[0])
# add login.enter_tinder here
