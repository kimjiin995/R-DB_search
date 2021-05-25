from common import *

def search(casno, browser):
    url = "https://wwwn.cdc.gov/TSP/index.aspx"
    try:
        browser.get(url)
    except:
        print("사이트에 연결되지 않습니다.")
        return "미확인"
    
    atsdr_search_xpath = "//*[@id='ContentPlaceHolder1_txtSearch']"
    result = send_casno_by_enter(casno, browser, atsdr_search_xpath)

    if result == "미확인":
        return result

    atsdr_result_xpath = "//*[@id='ContentPlaceHolder1_lblSearchCount']"
    result = wait_loading(atsdr_result_xpath, browser)
    
    if result == "미확인":
        return result
    elif "unique Substance Name(s)* meet your search criteria" in result.text:
        return "O"
    else:
        return "X"