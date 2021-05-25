from common import *

def search(casno, browser):
    url ="https://hbcp.chemnetbase.com/faces/contents/ContentsSearch.xhtml"
    
    try:
        browser.get(url)
    except:
        print("사이트에 연결되지 않습니다.")
        return "미확인"
    try:
        search_bar = browser.find_element_by_id("searchForm:searchTerm1")
    except:
        print("search_bar를 찾을 수 없습니다.")
        return "미확인"
    search_bar.send_keys(casno)
    search_button = browser.find_element_by_id("searchForm:j_idt135")
    search_button.click()

    crc_result_xpath = "//*[@id='resultsForm:j_idt111']"
    result = wait_loading(crc_result_xpath, browser)
    
    if result == "미확인":
        return result
    elif "No records found" in result.text:
        return "X"
    else:
        return "O"