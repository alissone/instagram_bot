import json
import pickle
from selenium import webdriver

"""
Manage driver and session
"""

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


def attach_to_session(executor_url, session_id):
    """
    https://stackoverflow.com/questions/8344776/can-selenium-interact-with-an-existing-browser-session
    """
    original_execute = WebDriver.execute
    def new_command_execute(self, command, params=None):
        if command == "newSession":
            # Mock the response
            return {'success': 0, 'value': None, 'sessionId': session_id}
        else:
            return original_execute(self, command, params)
    # Patch the function before creating the driver object
    WebDriver.execute = new_command_execute
    driver = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
    driver.session_id = session_id
    # Replace the patched function with original function
    WebDriver.execute = original_execute
    return driver


def save_session(driver, filename="instagram_session"):
    session = {}
    session["url"] = driver.command_executor._url
    session["id"] = driver.session_id

    with open(filename + ".json", "w") as session_file:
        json.dump(session, session_file, sort_keys=True, indent=4)


def load_session(filename="instagram_session"):
    with open(filename + ".json", "r") as session_file:
        session = json.load(session_file)

    print(session["url"])
    driver = attach_to_session(session["url"], session["id"])
    return driver
    # driver = build_driver(new_session=False, command_executor=session["url"])
    # driver.close()  # this prevents the dummy browser
    # driver.session_id = session["id"]
    # return driver


def build_driver(new_session=True):
    options = webdriver.ChromeOptions()
    options.binary_location = '~/Programas/chrome-linux/chrome'
    options.add_experimental_option("detach", True)
    #options.add_argument("user-data-dir=~/.config/chromium/Default") #Path to your chrome profile
    chrome_driver_binary = '~/Programas/chromedriver'

    if new_session:
        return webdriver.Chrome(chrome_driver_binary, options=options)
    else:
        return webdriver.Remote(chrome_driver_binary, options=options)

def save_cookie(driver, path):
    print("Saving cookie",str(path),"...")
    with open(path, 'wb') as filehandler:
        pickle.dump(driver.get_cookies(), filehandler)

def load_cookie(driver, path):
    print("Loading cookie",str(path),"...")
    with open(path, 'rb') as cookiesfile:
         cookies = pickle.load(cookiesfile)
         for cookie in cookies:
             driver.add_cookie(cookie)
