from search import *
from r_db import *

# 브라우저 생성
# browser = create_browser()
browser = create_browser_view()


# casno = "24261-13-0"
# casno = "814-94-8"
# casno = "3586-55-8"
# casno = "12001-28-4"
# casno = "75-91-2"
# casno = "117-81-7" # ntp 확인
# casno = "79-41-4" # nite 확인
# casno = "7778-74-7" # atsdr 확인
# casno = "83-32-9" # iris 확인
casno = "129-00-0" # hsdb 확인
# casno = "50-00-0" # acgih 확인

# print("merck\t : " + merck.search(casno, browser))
# print("crc\t : " + crc.search(casno, browser))
# print("eu_rar\t : " + eu_rar.search(casno))
# print("echa_bio : " + echa_bio.search(casno, browser))
# print("iarc\t : " + iarc.search(casno))
# print("ntp\t : " + ntp.search(casno, browser))
# print("red\t : " + red.search(casno, browser))
# print("nite\t : " + nite.search(casno, browser))
# print("atsdr\t : " + atsdr.search(casno, browser))
# print("aicis\t : " + aicis.search(casno, browser))
# print("oecd\t : " + oecd.search(casno, browser))
# print("iris\t : " + iris.search(casno))

#pubchem검색
# result_page = pubchem.search(casno, browser)

# print("hsdb\t : " + hsdb.search(result_page))
# print("ipcs\t : " + ipcs.search(casno, browser))
# print("chem_id_plus: " + chem_id_plus.search(casno, browser))
# print("us_dashboard: " + us_dashboard.search(casno, browser))
# print("acgih\t : " + acgih.search(result_page))
# print("acgih\t : " + acgih.search(result_page))
# print("ccris\t : " + ccris.search(casno, browser))
# print("ccris\t : " + ccris.search(casno))
# ccris.search(casno)
print("genotox\t : " + genetox.search(casno, browser))