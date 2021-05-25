from common import *

def search(casno, browser):
    url = "http://inchemsearch.ccohs.ca/inchem/jsp/search/search.jsp?serverSpec=&inchemcasreg=0&SubColl=EHC&QueryText="
    try:
        browser.get(url+casno)
    except:
        print("사이트에 연결되지 않습니다.")
        return "미확인"

    result_xpath = "/html/body/center/table/tbody/tr/td/font"
    result = wait_loading(result_xpath, browser)
    
    if result == "미확인":
        return result
    elif "matched 0 documents" in result.text:
        return "X"
    else:
        return "O"