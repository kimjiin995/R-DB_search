from common import *

def search(casno, browser):
    url = "https://chem.nlm.nih.gov/chemidplus/rn/startswith/"
    try:
        browser.get(url+casno)
    except:
        print("사이트에 연결되지 않습니다.")
        return "미확인"

    result_xpath = "//*[@id='main']"
    result = wait_loading(result_xpath, browser)
    
    if result == "미확인":
        return result
    elif "No results for Registry Number starts with" in result.text:
        return "X"
    else:
        return "O"