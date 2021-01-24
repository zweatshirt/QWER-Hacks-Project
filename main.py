# Imports for the project #
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Note: We can separate the different parts into different files
# then just add everything here.


class TinderDriver:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.name = None

    def login():
        pass

    def create_bio():
        pass

    def swipe(direction):
        element = self.driver.find_elements_by_class_name("recsPage")[0]
        if(direction == 'left'):
            element.send_keys(Keys.LEFT)
        elif(direction == 'right'):
            element.send_keys(Keys.RIGHT)

    def return_home(self):
        url = "https://tinder.com/app/recs"
        self.driver.get(url)

    def open_message_tab(self):
        message_button = self.driver.find_element_by_id("messages-tab")
        if(not message_button.aria-selected):
            message_button.click()
    
    def open_message(self):
        pass

    def get_response(self, message):
        # open tab
        self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
        
        self.driver.execute_script('''window.open("https://www.cleverbot.com/","_blank");''')
        self.driver.switch_to.window(self.driver.window_handles[-1])

        # wait for new tab to pass confirmation
        element = self.wait.until(
            EC.presence_of_element_located((By.ID, "wrapper"))
        )
        # time.sleep(2)

        self.driver.execute_script("noteok()")
        
        # type message into textbox
        input_box = self.driver.find_element_by_name("stimulus")
        input_box.send_keys(message + Keys.ENTER)

        # wait for response and plug it in i know its ugly but i dont care
        time.sleep(5)
        response = self.driver.find_elements_by_class_name('bot')[4].get_attribute("innerText")

        # close tab
        self.driver.close()

        return response

td = TinderDriver()
td.return_home()
print(td.get_response("whats up dude"))