from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException 
import pyperclip
import time

def sendmsg(usr, msg, path='error', attach='error'):
    
    CHROME_PROFILE_PATH = "user-data-dir=C:\\Users\\HP\\AppData\\Local\\Google\\Chrome\\User Data\\Login"
    users = "error"
    mssg = "error"

    try:
        if usr:
            with open(usr, 'r', encoding='utf8') as file:
                users = [user.strip() for user in file.readlines()]
    except IndexError:
        print("Please Provide Users as 1st Argument")

    try:
        if msg:
            with open(msg, 'r', encoding='utf8') as file:
                mssg = file.read()
    except IndexError:
        print("Please Provide The Message File as 2st Argument")

    options = webdriver.ChromeOptions()
    options.add_argument(CHROME_PROFILE_PATH)

    def run():

        browser = webdriver.Chrome(path, options=options)
        browser.maximize_window()
        browser.get('https://web.whatsapp.com/')

        for user in users:
            # Search Bar Section
            search_xpath = '//div[@title="Search input textbox"][@role="textbox"]'
            search_box = WebDriverWait(browser, 500).until(
                EC.presence_of_element_located((By.XPATH, search_xpath))
            )
            search_box.clear()
            time.sleep(1)
            pyperclip.copy(user)
            search_box.send_keys(Keys.CONTROL + "v")
            time.sleep(2)

            # User found or not

            try:
                browser.find_element("xpath",f'//span[@title="{user}"]')
                print("======== USER FOUND", user)
                # User Section
                #//span[@title="Mohammed Musthafa A"]
                user_title = browser.find_element("xpath",f'//span[@title="{user}"]')
                user_title.click()
                time.sleep(1)


                if attach != 'error':
                    attachment_box = browser.find_element("xpath", '//span[@data-testid="clip"][@data-icon="clip"]')
                    attachment_box.click()
                    time.sleep(1)

                    image_box = browser.find_element("xpath", '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
                    image_box.send_keys(attach)
                    time.sleep(1)

                    text_box = browser.find_element("xpath", '//div[@data-testid="pluggable-input-body"][@role="textbox"]')
                    pyperclip.copy(mssg)
                    text_box.send_keys(Keys.SHIFT, Keys.INSERT)
                    text_box.send_keys(Keys.ENTER)
                    time.sleep(1)
                else:
                    msgbox_xpath = '//div[@title="Type a message"][@role="textbox"]'
                    msgbox = browser.find_element('xpath', msgbox_xpath)
                    pyperclip.copy(mssg)
                    msgbox.send_keys(Keys.SHIFT, Keys.INSERT)
                    time.sleep(2)
                    msgbox.send_keys(Keys.ENTER)
                    time.sleep(1)


            except NoSuchElementException:
                print("======== USER NOT FOUND", user)

    if users == 'error':
        pass
    elif mssg == 'error':
        pass
    elif path == 'error':
        print('Please Provide Driver Path')
    else:
        run()