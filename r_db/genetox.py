from common import *

def search(casno, browser):
    url = f"https://pubchem.ncbi.nlm.nih.gov/#query={casno}&tab=substance&sidsrcname=Genetic%20Toxicology%20Data%20Bank%20(GENE-TOX)"
    try:
        browser.get(url)
    except:
        print("사이트에 연결되지 않습니다.")
        return "미확인"

    result_xpath = "//*[@id='main-results']/div[3]"
    result = wait_loading(result_xpath, browser)
    
    if result == "미확인":
        return result
    elif "0 results found" in result.text:
        return "X"
    else:
        return "O"


