from common import *

def search(casno, browser):
    url = "https://www.nite.go.jp/chem/jcheck/search.action?request_locale=en"
    try:
        browser.get(url)
    except:
        print("사이트에 연결되지 않습니다.")
        return "미확인"
    
    search_xpath = "//*[@id='search_action_cas_no']"
    result = send_casno_by_enter(casno, browser, search_xpath)
    
    if result == "미확인":
        return result

    result_xpath = "//*[@id='main']"
    result = wait_loading(result_xpath, browser)
    
    if result == "미확인":
        return result
    elif "No Results matched" in result.text:
        return "X"
    else:
        return "O"