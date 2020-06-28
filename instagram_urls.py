from instagram_utils import wait
import random

"""
URL constants and related
"""

def open_url(driver, url):
    print("Navigating to",url,"...")
    driver.get(url)
    wait(1)


def followers_url(username):
    return "https://www.instagram.com/{}/followers/".format(username)


def instagram_home():
    return "https://www.instagram.com/"

def instagram_login():
    return "'https://www.instagram.com/accounts/login/?source=auth_switcher'"


def random_famous_username():
    top_10_usernames = [
        "neymarjr",
        "beyonce",
        "leomessi",
        "kimkardashian",
        "selenagomez",
        "kyliejenner",
        "therock",
        "arianagrande",
        "cristiano",
        "instagram",
    ]
    return random.choice(top_10_usernames)
