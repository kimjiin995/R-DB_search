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

def send_casno_by_enter(casno, browser, xpath):
    search_bar = wait_loading(xpath, browser)
    if search_bar == "미확인":
        print("search_bar를 찾을 수 없습니다")
        return "미확인"
    search_bar.send_keys(casno)
    search_bar.send_keys(Keys.ENTER)