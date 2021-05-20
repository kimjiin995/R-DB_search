from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xml.etree.ElementTree import parse
import time
from excel_load import *

def create_browser():
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument("window-size=1920x1080")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.62")

    browser = webdriver.Chrome(options=options)
    return browser

def create_browser_view():
    options = webdriver.ChromeOptions()
    options.add_argument("window-size=1920x1080")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.62")

    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    return browser

def wait_loading(xpath, browser):
    try:
        result = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
        return result
    except:
        print("로딩이 깁니다. 브라우저를 끕니다.")
        browser.quit()

def search_merck(casno, browser):
    url = "https://www.rsc.org/merck-index/search"
    
    browser.get(url)

    search_bar = browser.find_element_by_id("CASRegNo")
    search_bar.send_keys(casno)
    search_bar.send_keys(Keys.ENTER)
    
    xpath_merck = "/html/body/div[3]/div[1]/div[5]/div[1]/div[2]/div/div[2]/div/p[1]/strong"
    result = wait_loading(xpath_merck, browser)

    if "0 results" in result.text:
        return "X"
    else:
        return "O"

def search_crc(casno, browser):
    url ="https://hbcp.chemnetbase.com/faces/contents/ContentsSearch.xhtml"
    
    browser.get(url)

    search_bar = browser.find_element_by_id("searchForm:searchTerm1")
    search_bar.send_keys(casno)
    search_button = browser.find_element_by_id("searchForm:j_idt135")
    search_button.click()

    xpath_crc = "//*[@id='resultsForm:j_idt111']"
    result = wait_loading(xpath_crc, browser)
    
    if "No records found" in result.text:
        return "X"
    else:
        return "O"

def search_eurar(casno):
    tree = parse("C:\\dev\\python_workspace\\R-DB_search\\datas\\eurar.xml")
    root = tree.getroot()
    substances = root.findall("Substance")
    
    for substance in substances:
        casnum_eurar = substance.find("Substance_CAS_Numbers").find("CAS_number").text
        if casno in casnum_eurar:
            return "O"
    return "X" 

def search_echa_bio(casno, browser):
    url = "https://echa.europa.eu/information-on-chemicals/biocidal-active-substances"
    
    browser.get(url)
    accept_btn = browser.find_element_by_id("_viewsubstances_WAR_echarevsubstanceportlet_acceptDisclaimerButton")
    accept_btn.click()

    xpath_search_echa = "//*[@id='_dissactivesubstances_WAR_dissactivesubstancesportlet_disas_substance_name']"

    search_bar = wait_loading(xpath_search_echa, browser)
    search_bar.send_keys(casno)
    search_bar.send_keys(Keys.ENTER)
   
    # 페이지 맨아래로 스크롤
    time.sleep(2)
    browser.execute_script("window.scrollTo(0, 1080)")
    time.sleep(2)
    xpath_echa_bio = "//*[@id='p_p_id_dissactivesubstances_WAR_dissactivesubstancesportlet_']/div/div/div[3]"
    result = wait_loading(xpath_echa_bio, browser)

    if "No results were found" in result.text:
        return "X"
    else:
        return "O"

def search_IARC(casno):
    file_name = "Agents Classified by the IARC Monographs, Volumes 1–129.xlsx"
    (wb, ws) = load_wb("C:\\dev\\python_workspace\\R-DB_search\\datas\\"+file_name)

    for index in range(3, ws.max_row):
        casnum_IARC = bring_casnum_IARC(ws, index)
        if casno in str(casnum_IARC):
            return "O"
    return "X"
    
    
    





