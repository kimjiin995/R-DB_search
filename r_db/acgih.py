def search(result_page):
    
    if result_page == "X":
        return "X"
    elif result_page == "미확인":
        return "미확인"
    elif "ACGIH" in result_page:
        return "O"
    else:
        return "X"