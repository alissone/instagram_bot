from selenium import webdriver
from secret_instagram import username, password
import pickle

from instagram_utils import wait, progress_bar
from instagram_meta_srollable import scroll_to_bottom_of_modal
from instagram_urls import open_url, followers_url
from instagram_user import User
from instagram_session import load_session
from followers_routine import followers_routine


# # TODO: Replace dict with proper class!
# def get_followers_dict(number_of_followers):
#     print("Getting followers...")
#     followers = []
#     for follower_index in range(number_of_followers):
#         follower_id_xpath = "/html/body/div[4]/div/div/div[2]/ul/div/li[{}]/div/div[1]/div[2]/div[1]/a".format(
#             follower_index + 1)
#         follower_id = driver.find_element_by_xpath(follower_id_xpath).text

#         follower_name_xpath = "/html/body/div[4]/div/div/div[2]/ul/div/li[{}]/div/div[1]/div[2]/div[2]".format(
#             follower_index + 1)
#         follower_name = driver.find_element_by_xpath(follower_name_xpath).text

#         follower_button_xpath = "/html/body/div[4]/div/div/div[2]/ul/div/li[{}]/div/div[2]/button".format(
#             follower_index + 1)
#         follower_button = driver.find_element_by_xpath(
#             follower_button_xpath).text

#         try:
#             user = User(username=follower_id, name=follower_name)
#             user.set_status(follower_button)
#             followers.append(user)
#             del user
#         except:
#             print("skipped follower {}".format(follower_index))

#         progress_bar(follower_index, number_of_followers)
#     return followers


# TODO: When loading this list, the full-size profile pictures are used!
# Save each profile picture as {username}.jpg

# TODO: Get a list of people that liked a photo

# TODO: Get a list of people tagged in other posts

# TODO: We need to store those people as a graph too

driver = load_session()

# scrollarea_xpath = "/html/body/div[4]/div/div/div[2]"

# number_of_followers = 25

# clicks = number_of_followers // 7

# open_url(driver, followers_url("umadi.jerusalem"))
# open_followers_modal(driver)
# wait(2)
# scroll_to_bottom_of_modal(driver, scrollarea_xpath, clicks)
# followers = get_followers_dict(number_of_followers)
# print(followers)

followers = followers_routine(driver)