import time
from common import *

def search(casno, browser):
    url = "https://echa.europa.eu/information-on-chemicals/biocidal-active-substances"
    
    try:
        browser.get(url)
    except:
        print("사이트에 연결되지 않습니다.")
        return "미확인"

    try:
        accept_btn = browser.find_element_by_id("_viewsubstances_WAR_echarevsubstanceportlet_acceptDisclaimerButton")
        accept_btn.click()
    except:
        print("accept btn을 찾을 수 없습니다.")
        
    echa_search_xpath = "//*[@id='_dissactivesubstances_WAR_dissactivesubstancesportlet_disas_substance_name']"
    result = send_casno_by_enter(casno, browser, echa_search_xpath)
    
    if result == "미확인":
        return result
   
    # 페이지 맨아래로 스크롤
    time.sleep(2)
    browser.execute_script("window.scrollTo(0, 1080)")
    time.sleep(2)
    echa_bio_result_xpath = "//*[@id='p_p_id_dissactivesubstances_WAR_dissactivesubstancesportlet_']/div/div/div[3]"
    result = wait_loading(echa_bio_result_xpath, browser)
    
    if result == "미확인":
        return result
    elif "No results were found" in result.text:
        return "X"
    else:
        return "O"
