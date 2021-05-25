from selenium.webdriver.common.keys import Keys
from common import *

def search(casno, browser):
    url = "https://www.rsc.org/merck-index/search"
    
    try:
        browser.get(url)
    except:
        print("사이트에 연결되지 않습니다.")
        return "미확인"

    try:
        search_bar = browser.find_element_by_id("CASRegNo")
    except:
        print("search_bar를 찾을 수 없습니다")
        return "미확인"
    
    search_bar.send_keys(casno)
    search_bar.send_keys(Keys.ENTER)
    
    merck_result_xpath = "/html/body/div[3]/div[1]/div[5]/div[1]/div[2]/div/div[2]/div/p[1]/strong"
    result = wait_loading(merck_result_xpath, browser)

    if result == "미확인":
        return result
    elif "0 results" in result.text:
        return "X"
    else:
        return "O"