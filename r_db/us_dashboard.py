from common import *

def search(casno, browser):
    url = "https://comptox.epa.gov/dashboard/dsstoxdb/results?search="
    try:
        browser.get(url+casno)
    except:
        print("사이트에 연결되지 않습니다.")
        return "미확인"

    result_xpath = "/html/body/div[1]/div[2]/div[1]"
    result = wait_loading(result_xpath, browser)
    
    if result == "미확인":
        return result
    elif "No Chemicals found" in result.text:
        return "X"
    else:
        return "O"
