from common import *

def search(casno, browser):
    url = "https://www.nite.go.jp/en/chem/chrip/chrip_search/srhInput"
    try:
        browser.get(url)
    except:
        print("사이트에 연결되지 않습니다.")
        return "미확인"
    
    nite_search_xpath = "//*[@id='txNumSh']"

    result = send_casno_by_enter(casno, browser, nite_search_xpath)
    
    if result == "미확인":
        return result

    nite_result_xpath = "//*[@id='content-area']/div[4]"
    result = wait_loading(nite_result_xpath, browser)
    
    if result == "미확인":
        return result
    elif "Hazard and Risk Assessment Reports etc. in Japan" in result.text:
        return "O"
    else:
        return "X"