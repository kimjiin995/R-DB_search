from common import *

def search(casno, browser):
    url = "https://iaspub.epa.gov/apex/pesticides/f?p=chemicalsearch:123"
    try:
        browser.get(url)
    except:
        print("사이트에 연결되지 않습니다.")
        return "미확인"
    
    red_search_xpath = "//*[@id='P1_CODE_SEARCH']"

    result = send_casno_by_enter(casno, browser, red_search_xpath)

    if result == "미확인":
        return result
    
    red_result_xpath = "//*[@id='main']"
    result = wait_loading(red_result_xpath, browser)
    
    if result == "미확인":
        return result
    
    elif "No data found" in result.text:
        return "X"
    else:
        return "O"