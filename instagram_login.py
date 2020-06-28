from selenium import webdriver
from secret_instagram import username, password
from instagram_urls import open_url, followers_url, instagram_home, random_famous_username, instagram_login
from instagram_session import build_driver, save_session, load_session
from instagram_utils import wait
from selenium.webdriver.common.keys import Keys

driver = build_driver(new_session=True)

def verify_if_logged_in(driver) -> bool:
    """Verify if user is already logged in.
    We should definetly use something else than followers button,
    as it won't work on homepage

    Args:
        driver (webdriver): selenium webriver

    Returns:
        bool: True if the user has already logged in
    """
    try:
        open_url(driver, followers_url(random_famous_username()))
        followers_button_xpath = '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a'
        followers_button = driver.find_element_by_xpath(followers_button_xpath)
        return followers_button is not None
    except:
        return False


def login(driver, username: str, password: str) -> bool:
    """Attempts to login on Instagram

    Args:
        driver (webdriver): selenium webdriver
        username (str): username
        password (str): password

    Returns:
        bool: True if the login was successfull
    """

    print("Logging in...")

    try:
        open_url(driver, instagram_login())
        wait(7)
        driver.find_element_by_name("username").send_keys(username)
        driver.find_element_by_name("password").send_keys(password)
        driver.find_element_by_name("password").send_keys(u'\ue007')
        wait(2)
        print("Logged in sucessfully...")

        return True

    except Exception as e:
        print("Could not login because of", e)

        return False

if __name__ == "__main__":

    open_url(driver, instagram_home())
    
    logged_in = verify_if_logged_in(driver)

    if not logged_in:
        login(driver, username(), password())

    save_session(driver)