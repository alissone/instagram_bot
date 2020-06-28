from instagram_utils import wait, progress_bar

followers_xpaths = {
    "modal_link": "/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span",
    "scrollarea": "/html/body/div[4]/div/div/div[2]",
    "username"  : "/html/body/div[4]/div/div/div[2]/ul/div/li[$$$]/div/div[1]/div[2]/div[1]/a",
    "name"      : "/html/body/div[4]/div/div/div[2]/ul/div/li[$$$]/div/div[1]/div[2]/div[2]",
    "image"     : "/html/body/div[4]/div/div/div[2]/ul/div/li[$$$]/div/div[1]/div[1]/a/img",
    "button"    : "/html/body/div[4]/div/div/div[2]/ul/div/li[$$$]/div/div[2]/button",
}

following_xpaths = {
    "modal_link" : "/html/body/div[1]/section/main/div/header/section/ul/li[3]/a",
    "scrollarea" : "/html/body/div[4]/div/div/div[2]",
    "username"   : "/html/body/div[4]/div/div/div[2]/ul/div/li[$$$]/div/div[2]/div[1]/div/div/a",
    "name"       : "/html/body/div[4]/div/div/div[2]/ul/div/li[$$$]/div/div[2]/div[2]/div",
    "image"      : "/html/body/div[4]/div/div/div[2]/ul/div/li[$$$]/div/div[1]/div/a/img",
    "button"     : "/html/body/div[4]/div/div/div[2]/ul/div/li[$$$]/div/div[3]/button",
}

likes_xpaths = {
    "modal_link" : "/html/body/div[4]/div[2]/div/article/div[2]/section[2]/div/div[2]/button",
    "scrollarea" : "/html/body/div[5]/div/div/div[2]/div",
    "username"   : "/html/body/div[5]/div/div/div[2]/div/div/div[3]/div[2]/div[1]/div/a/div/div/div",
    "name"       : "/html/body/div[5]/div/div/div[2]/div/div/div[3]/div[2]/div[2]/div",
    "image"      : "/html/body/div[5]/div/div/div[2]/div/div/div[3]/div[1]/div/a/img",
    "button"     : "/html/body/div[5]/div/div/div[2]/div/div/div[3]/div[3]/button",
}

def get_text_from_xpath(driver, xpath, index=None):
    if index:
        xpath = xpath.replace("$$$",str(index))
    return driver.find_element_by_xpath(xpath).text


def open_modal(driver, xpaths: dict) -> bool:
    print("Trying to open modal...")

    try:
        button_xpath = xpaths.get("modal_link")
        button = driver.find_element_by_xpath(button_xpath)
        button.click()
        return True

    except Exception as e:
        print("Couldn't open modal because of",e)
        return False

def scroll_to_bottom_of_modal(driver, scrollarea_xpath, clicks):
    """Utility to scroll down in Likes, Following and Followers modal

    Args:
        scrollarea_xpath (str): xpath of modal div
        clicks ([type]): number of steps to scroll down
    """

    print("Scrolling modal...")
    scrollarea = driver.find_element_by_xpath(scrollarea_xpath)
    for _ in range(clicks):
        driver.execute_script(
            "arguments[0].scrollTop = arguments[0].scrollHeight", scrollarea)
        wait(0.8)

def get_users_from_modal(driver, xpaths: dict, number_of_users: int) -> bool:
    print("Trying to get users from modal...")
    users = []
    for user_index in range(number_of_users):
        user_id     = get_text_from_xpath(driver, xpaths.get("username"), user_index + 1)
        user_name   = get_text_from_xpath(driver, xpaths.get("name"), user_index + 1)
        user_button = get_text_from_xpath(driver, xpaths.get("button"), user_index + 1)

        try:
            user = User(username=user_id, name=user_name)
            user.set_status(user_button)
            users.append(user)
            del user
        except:
            print("Skipped user {}".format(user_index))

        progress_bar(user_index, number_of_users)
    return users

