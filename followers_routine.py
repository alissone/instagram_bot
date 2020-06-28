from instagram_meta_srollable import followers_xpaths, open_modal, scroll_to_bottom_of_modal, get_users_from_modal
from instagram_urls import open_url, followers_url
from instagram_utils import wait

def followers_routine(driver):
    # TODO: Calcular o número de seguidores a partir da página
    number_of_users = 20

    open_url(driver, followers_url("umadi.jerusalem"))
    open_modal(driver, followers_xpaths)
    wait(2)
    scroll_to_bottom_of_modal(driver, followers_xpaths["modal_link"], number_of_users)
 
    followers = get_users_from_modal(driver, followers_xpaths, number_of_users=number_of_users)
    print(followers)
    return followers

if __name__ == "__main__":
    from instagram_session import load_session
    driver = load_session()
    scroll_to_bottom_of_modal(driver, followers_xpaths["scrollarea"], 30)