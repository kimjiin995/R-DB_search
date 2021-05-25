from excel_load import *

def search(casno):
    file_name = "Agents Classified by the IARC Monographs, Volumes 1–129.xlsx"
    (wb, ws) = load_wb("C:\\dev\\python_workspace\\R-DB_search\\datas\\"+file_name)

    for index in range(3, ws.max_row):
        casnum_iarc = bring_casnum(ws, "A", index)
        if casno in str(casnum_iarc):
            return "O"
    return "X"