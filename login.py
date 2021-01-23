from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent

user_agent = UserAgent()
rand_user = user_agent.random

# needed to bypass captcha
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'user-agent={rand_user}')


class Login:

    def __init__(self):
        # init driver
        self.driver = webdriver.Chrome(ChromeDriverManager().install(),
                                       chrome_options=chrome_options)
        self.tinder = "https://tinder.com"
        self.google_voice = "https://voice.google.com/about"
        self.email = "coilettebendher@gmail.com"
        self.number = "2247898554"  # number to sign in

    def goto_site(self, site):
        if site == "tinder":
            self.driver.get(self.tinder)
        elif site == "google_voice":
            self.driver.get(self.google_voice)

    def login_driver(self):
        try:
            login_btn = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(
                    (By.XPATH,
                     "//*[@id=\"content\"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button")
                )
            )
            login_btn.click()

            login_by_num = login_btn = WebDriverWait(self.driver, 20).until(
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

        # TODO: finish this portion
        def grab_num_driver():
            try:
                login_btn = WebDriverWait(self.driver, 20).until(
                    EC.element_to_be_clickable(
                        (By.XPATH,
                         "/html/body/div[1]/div[2]/a[2]")
                    )
                )
                login_btn.click()

                sign_in_field = WebDriverWait(self.driver, 20).until(
                    EC.element_to_be_clickable(
                        (By.XPATH,
                         "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
                    )
                )
                sign_in_field.send_keys(self.email)

            finally:
                pass


login = Login()
login.goto_site("tinder")
login.login_driver()
# login.goto_site("google_voice")
# login.grab_num_driver()
