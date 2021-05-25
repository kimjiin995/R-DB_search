from common import *
import time

def search(casno, browser):
    url = "https://pubchem.ncbi.nlm.nih.gov/#query="
    try:
        browser.get(url+casno)
    except:
        print("사이트에 연결되지 않습니다.")
        return "미확인"

    try:
        elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='featured-results']/div/div[2]/div/div[1]/div[2]/div[1]")))
        elem.click()
    except:
        print("match되는 compound가 없습니다. X 처리합니다.")
        return "X"
    
    # 페이지 맨아래로 스크롤
    prev_height= browser.execute_script("return document.body.scrollHeight")

    while True:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(2)
        curr_height = browser.execute_script("return document.body.scrollHeight")

        if prev_height == curr_height:
            break    
    
        prev_height = curr_height

    print("스크롤 완료")   
    
    result_page = browser.page_source

    return result_page