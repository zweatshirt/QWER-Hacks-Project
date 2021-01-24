# Imports for the project #
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login import Login
from behaviorFlow import behaviorFlow
import time

# Note: We can separate the different parts into different files
# then just add everything here.


class TinderDriver:

    def __init__(self, driver):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.name = None

    def login():
        pass

    def create_bio():
        pass

    def swipe(self, direction):
        self.return_home()
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
        # if(not message_button.aria-selected):
        message_button.click()
    
    def open_match_tab(self):
        match_button = self.driver.find_element_by_id("match-tab")
        # if(not match_button.aria-selected):
        match_button.click()
    
    def get_random_message(self):
        # return on a random message in the message tab
        return None

    def check_for_new_matches(self):
        # return first element that links to messages with a new match
        return None

    def find_last_response(self):
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

    def message():
        # check for matches we have not messaged
        self.open_match_tab()
        new_match = self.check_for_new_matches()

        # if one exists message then pick it, else pick a random one
        if(new_match != None):
            new_match.click()
        else:
            self.open_message_tab()
            old_match = self.get_random_message()
            
            if(old_match == None): 
                print("no matches found, back to swiping")
                return

            old_match.click()

        # find last message send by other person
        last_message = self.find_last_response()

        response = self.get_response(last_message)

        # find input_box
        # input_box = self.driver.find_
        # input_box.send_keys(response + Keys.ENTER)
        
        

login = Login()
print(login.parse_time())
login.goto_site("tinder")
login.login_driver()
login.goto_site("google_voice")
pin = login.grab_num_driver()
login.driver.switch_to.window(login.driver.window_handles[0])
login.enter_tinder(pin)

td = TinderDriver(login.driver)
# td.return_home()
# print(td.get_response("whats up dude"))

# driver = 0
coilette = behaviorFlow()
coilette.chooseBehavior(td)
