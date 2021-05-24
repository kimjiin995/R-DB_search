from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xml.etree.ElementTree import parse
import time
from excel_load import *
from selenium.webdriver.support.select import Select

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
    options.add_argument("start-maximized")
    options.add_argument("--disable-extensions")
    options.add_argument('disable-infobars')

    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    return browser

def wait_loading(xpath, browser):
    try:
        result = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
        return result
    except:
        print("로딩이 깁니다. 미확인 처리합니다.")
        return "미확인"

def wait_presence_loading(xpath, browser):
    try:
        result = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, xpath)))
        return result
    except:
        print("검색결과가 없다는 요소를 찾을 수 없습니다.")
        return "O"

def send_as_search_bar(casno, browser, xpath):
    search_bar = wait_loading(xpath, browser)
    search_bar.send_keys(casno)
    search_bar.send_keys(Keys.ENTER)

def search_merck(casno, browser):
    url = "https://www.rsc.org/merck-index/search"
    
    browser.get(url)

    search_bar = browser.find_element_by_id("CASRegNo")
    search_bar.send_keys(casno)
    search_bar.send_keys(Keys.ENTER)
    
    merck_result_xpath = "/html/body/div[3]/div[1]/div[5]/div[1]/div[2]/div/div[2]/div/p[1]/strong"
    result = wait_loading(merck_result_xpath, browser)

    if result == "미확인":
        return result
    elif "0 results" in result.text:
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

    crc_result_xpath = "//*[@id='resultsForm:j_idt111']"
    result = wait_loading(crc_result_xpath, browser)
    
    if result == "미확인":
        return result
    elif "No records found" in result.text:
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

    echa_search_xpath = "//*[@id='_dissactivesubstances_WAR_dissactivesubstancesportlet_disas_substance_name']"
    send_as_search_bar(casno, browser, echa_search_xpath)
   
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

def search_iarc(casno):
    file_name = "Agents Classified by the IARC Monographs, Volumes 1–129.xlsx"
    (wb, ws) = load_wb("C:\\dev\\python_workspace\\R-DB_search\\datas\\"+file_name)

    for index in range(3, ws.max_row):
        casnum_iarc = bring_casnum(ws, "A", index)
        if casno in str(casnum_iarc):
            return "O"
    return "X"

def search_ntp(casno, browser):
    url = "https://ntp.niehs.nih.gov/publications/reports/index.html"
    browser.get(url)
    
    ntp_search_xpath = "//*[@id='datatable_filter']/label/input"

    send_as_search_bar(casno, browser, ntp_search_xpath)

    ntp_result_xpath = "//*[@id='datatable_info']"
    result = wait_loading(ntp_result_xpath, browser)

    if result == "미확인":
        return result
    elif "Showing 0 to 0 of 0 entries" in result.text:
        return "X"
    else:
        return "O"

def search_red(casno, browser):
    url = "https://iaspub.epa.gov/apex/pesticides/f?p=chemicalsearch:1"
    browser.get(url)
    
    red_search_xpath = "//*[@id='P1_CODE_SEARCH']"

    send_as_search_bar(casno, browser, red_search_xpath)

    red_result_xpath = "//*[@id='main']"
    result = wait_loading(red_result_xpath, browser)
    
    if result == "미확인":
        return result
    
    elif "No data found" in result.text:
        return "X"
    else:
        return "O"

def search_nite(casno, browser):
    url = "https://www.nite.go.jp/en/chem/chrip/chrip_search/srhInput"
    browser.get(url)
    
    nite_search_xpath = "//*[@id='txNumSh']"

    send_as_search_bar(casno, browser, nite_search_xpath)

    nite_result_xpath = "//*[@id='content-area']/div[4]"
    result = wait_loading(nite_result_xpath, browser)
    
    if result == "미확인":
        return result
    elif "Hazard and Risk Assessment Reports etc. in Japan" in result.text:
        return "O"
    else:
        return "X"
    
def search_atsdr(casno, browser):
    url = "https://wwwn.cdc.gov/TSP/index.aspx"
    browser.get(url)
    
    atsdr_search_xpath = "//*[@id='ContentPlaceHolder1_txtSearch']"
    send_as_search_bar(casno, browser, atsdr_search_xpath)

    atsdr_result_xpath = "//*[@id='ContentPlaceHolder1_lblSearchCount']"
    result = wait_loading(atsdr_result_xpath, browser)
    
    if result == "미확인":
        return result
    elif "unique Substance Name(s)* meet your search criteria" in result.text:
        return "O"
    else:
        return "X"

def search_aicis(casno, browser):
    url = "https://www.industrialchemicals.gov.au/chemical-information/search-assessments"
    browser.get(url)
    
    aicis_search_xpath = "//*[@id='assessment-cass-input']"
    send_as_search_bar(casno, browser, aicis_search_xpath)

    aicis_result_xpath = "//*[@id='casitemnoresult']"
    result = wait_loading(aicis_result_xpath, browser)
    
    if result == "미확인":
        return result
    elif "No result" in result.text:
        return "X"
    else:
        return "O"

def search_oecd(casno, browser):
    url = "https://hpvchemicals.oecd.org/ui/Search.aspx"
    browser.get(url)
    
    oecd_search_xpath = "//*[@id='ctl00_ContentPlaceHolder1_CasnumTextBox']"
    send_as_search_bar(casno, browser, oecd_search_xpath)

    oecd_result_xpath = "//*[@id='col_middle']/table"
    result = wait_loading(oecd_result_xpath, browser)
    
    if result == "미확인":
        return result
    elif "Records : 0" in result.text:
        return "X"
    else:
        return "O"

def search_iris(casno):
    file_name = "excelView_IRIS.xlsx"
    (wb, ws) = load_wb("C:\\dev\\python_workspace\\R-DB_search\\datas\\"+file_name)

    for index in range(4, ws.max_row):
        casnum_iris = bring_casnum(ws, "B", index)
        if casno in str(casnum_iris):
            return "O"
    return "X"



    





