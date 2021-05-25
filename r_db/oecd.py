from common import *

def search(casno, browser):
    url = "https://hpvchemicals.oecd.org/ui/Search.aspx"
    try:
        browser.get(url)
    except:
        print("사이트에 연결되지 않습니다.")
        return "미확인"
    
    oecd_search_xpath = "//*[@id='ctl00_ContentPlaceHolder1_CasnumTextBox']"
    result = send_casno_by_enter(casno, browser, oecd_search_xpath)
    
    if result == "미확인":
        return result

    oecd_result_xpath = "//*[@id='col_middle']/table"
    result = wait_loading(oecd_result_xpath, browser)
    
    if result == "미확인":
        return result
    elif "Records : 0" in result.text:
        return "X"
    else:
        return "O"