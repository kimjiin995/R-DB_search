from excel_load import *

def search(casno):
    file_name = "excelView_IRIS.xlsx"
    (wb, ws) = load_wb("C:\\dev\\python_workspace\\R-DB_search\\datas\\"+file_name)

    for index in range(4, ws.max_row):
        casnum_iris = bring_casnum(ws, "B", index)
        if casno in str(casnum_iris):
            return "O"
    return "X"