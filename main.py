from search import *

# 브라우저 생성
# browser = create_browser()
browser = create_browser_view()

# casno = "24261-13-0"
# casno = "814-94-8"
casno = "3586-55-8"
# casno = "12001-28-4"
# casno = "75-91-2"
# print(search_merck(casno, browser))
# print(search_crc(casno, browser))
# print(search_eurar(casno))
print(search_echa_bio(casno, browser))
# print(search_IARC(casno))