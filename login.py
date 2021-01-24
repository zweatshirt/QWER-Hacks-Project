# It pains me to see so many imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from fake_useragent import UserAgent
# import datetime
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
        # self.email = "coilettebendher@gmail.com"
        self.email = "coilettebendher2@gmail.com"
        self.password = "thisisagenericpassword123"
        # self.number = "2247898554"  # number to sign in
        self.number = "3125699159"  # number to sign in
        self.wait = WebDriverWait(self.driver, 50)

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
        elif sitee == "homepage":
            self.driver.execute_script("window.open('')")
            self.driver.switch_to.window(login.driver.window_handles[2])

    def login_driver(self):
        try:
            login_btn = self.wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH,
                     "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button/span")
                )
            )
            login_btn.click()

            login_by_num = login_btn = self.wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH,
                     "//*[@id=\"modal-manager\"]/div/div/div[1]/div/div[3]/span/div[3]/button/span[2]")
                )
            )
            login_by_num.click()

            enter_num = self.wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH,
                     "/html/body/div[2]/div/div/div[1]/div[2]/div/input")
                )
            )
            enter_num.send_keys(self.number)

            continue_btn = self.wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH,
                     "/html/body/div[2]/div/div/div[1]/button/span")
                )
            )
            continue_btn.click()
        finally:
            pass

    # def parse_time(self):
    #     stringify_time = datetime.datetime.now().strftime("%I:%M %p")
    #     return stringify_time[1:] if stringify_time[0] == "0" else stringify_time

    # TODO: finish this portion
    def grab_num_driver(self):
        try:
            # click sign in button
            login_btn = self.wait.until(
                EC.element_to_be_clickable(
                    (By.LINK_TEXT, "Sign in")
                )
            )
            login_btn.click()

            # enter email
            sign_in_field = self.wait.until(
                EC.element_to_be_clickable(
                    (By.CLASS_NAME,
                     "whsOnd")
                    # (By.XPATH,
                    #  "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
                )
            )
            sign_in_field.send_keys(self.email)

            # hit next button
            next_btn = self.wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH,
                     "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]")
                )
            )
            next_btn.click()

            # enter password
            password_field = self.wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH,
                     "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
                )
            )
            password_field.send_keys(self.password)

            # hit second next button
            next_btn_two = self.wait.until(
                EC.element_to_be_clickable(
                    # (By.XPATH,
                    #  "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]")
                    (By.CLASS_NAME,
                     'VfPpkd-RLmnJb')
                )
            )
            try:
                next_btn_two.click()
            except StaleElementReferenceException:
                next_btn_two = self.driver.find_element_by_class_name('VfPpkd-RLmnJb')
                next_btn_two.click()

            # hit messages button
            msg_btn = self.wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH,
                     "/html/body/div[1]/div[2]/div[2]/gv-side-nav/div/div/gmat-nav-list/a[2]/div/div/span[2]")
                )
            )
            msg_btn.click()

            message = self.wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH,
                     "//*[@gv-test-id='text-message-content']")
                )
            )

            # attempt to click into message, needs work
            # message = self.wait.until(
            #     EC.element_to_be_clickable(
            #         (By.CLASS_NAME,
            #          "rkljfb-biJj")
            #     )
            # )
            message.click()

            messagetxt = self.wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH,
                     "//*[@gv-test-id='bubble']")
                )
            )
            text = messagetxt.text
            # my stupid text editor automatically changes lambdas to regular funcs
            def pin(x): return [str(char) for char in x.split() if char.isdigit()]
            return pin(text)

        finally:
            pass

    # last function to be called after the code sent to the number is grabbed
    def enter_tinder(self, pin):
        field1 = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH,
                    "//*[@id=\"modal-manager\"]/div/div/div[1]/div[3]/input[1]")
            )
        )
        field1.send_keys(pin[0][0])
        field2 = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH,
                    "//*[@id=\"modal-manager\"]/div/div/div[1]/div[3]/input[2]")
            )
        )
        field2.send_keys(pin[0][1])
        field3 = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH,
                    "//*[@id=\"modal-manager\"]/div/div/div[1]/div[3]/input[3]")
            )
        )
        field3.send_keys(pin[0][2])
        field4 = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH,
                    "//*[@id=\"modal-manager\"]/div/div/div[1]/div[3]/input[4]")
            )
        )
        field4.send_keys(pin[0][3])
        field5 = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH,
                    "//*[@id=\"modal-manager\"]/div/div/div[1]/div[3]/input[5]")
            )
        )
        field5.send_keys(pin[0][4])
        field6 = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH,
                    "//*[@id=\"modal-manager\"]/div/div/div[1]/div[3]/input[6]")
            )
        )
        field6.send_keys(pin[0][5])
        continue_btn = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH,
                    "//*[@id=\"modal-manager\"]/div/div/div[1]/button")
            )
        )
        continue_btn.click()

        # I don't know if this possible
        grab_num_two_driver():
            gmail_btn = self.wait.until(
                EC.element_to_be_clickable(
                    (By.CLASS_NAME,
                        "gb_g")
                )
            )


# move to main when ready:
login = Login()
login.goto_site("tinder")
login.login_driver()
login.goto_site("google_voice")
pin = login.grab_num_driver()
login.driver.switch_to.window(login.driver.window_handles[0])
login.enter_tinder(pin)
login.goto_site("homepage")
login.grab_num_two_driver()
