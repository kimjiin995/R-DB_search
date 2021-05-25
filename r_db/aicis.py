from common import *

def search(casno, browser):
    url = "https://www.industrialchemicals.gov.au/chemical-information/search-assessments"
    try:
        browser.get(url)
    except:
        print("사이트에 연결되지 않습니다.")
        return "미확인"
    
    aicis_search_xpath = "//*[@id='assessment-cass-input']"
    result = send_casno_by_enter(casno, browser, aicis_search_xpath)
    
    if result == "미확인":
        return result

    aicis_result_xpath = "//*[@id='casitemnoresult']"
    # aicis_result_xpath = "//*[@id='casitemnoresult']/div/p"
    result = wait_loading(aicis_result_xpath, browser)
    
    if result == "미확인":
        return result
    elif "No result" in result.text:
        return "X"
    else:
        return "O"