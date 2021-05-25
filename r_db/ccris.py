from common import *

def search(casno, browser):
    url = f"https://pubchem.ncbi.nlm.nih.gov/#query={casno}&tab=substance&sidsrcname=Chemical%20Carcinogenesis%20Research%20Information%20System%20(CCRIS)"
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

# import requests
# from bs4 import BeautifulSoup

# def search(casno):
#     headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.62"}
#     url = f"https://pubchem.ncbi.nlm.nih.gov/#query={casno}&tab=substance&sidsrcname=Chemical%20Carcinogenesis%20Research%20Information%20System%20(CCRIS)"

#     res = requests.get(url, headers=headers)
#     res.raise_for_status()
#     if res.status_code != requests.codes.ok:
#         print("사이트에 연결하지 못했습니다. [에러코드 ", res.status_code, "]")
#         return "미확인"
#     print(res.text)
#     soup = BeautifulSoup(res.text, "lxml")

#     with open("ccris.html", "w", encoding="utf8") as f:
#         f.write(res.text)

#     # result = soup.find("div", attrs={"id":"main-results"})
#     # if "0 results found" in str(result.get_text()):
#     #     return "X"
#     # else:
#     #     return "O"
    



