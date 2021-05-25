from common import *

def search(casno, browser):
    url = "https://ntp.niehs.nih.gov/publications/reports/index.html"
    
    try:
        browser.get(url)
    except:
        print("사이트에 연결되지 않습니다.")
        return "미확인"
    
    ntp_search_xpath = "//*[@id='datatable_filter']/label/input"

    result = send_casno_by_enter(casno, browser, ntp_search_xpath)
    
    if result == "미확인":
        return result

    ntp_result_xpath = "//*[@id='datatable_info']"
    result = wait_loading(ntp_result_xpath, browser)

    if result == "미확인":
        return result
    elif "Showing 0 to 0 of 0 entries" in result.text:
        return "X"
    else:
        return "O"
