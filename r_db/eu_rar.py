from xml.etree.ElementTree import parse
from excel_load import *

def search(casno):
    tree = parse("C:\\dev\\python_workspace\\R-DB_search\\datas\\eurar.xml")
    root = tree.getroot()
    substances = root.findall("Substance")
    
    for substance in substances:
        casnum_eurar = substance.find("Substance_CAS_Numbers").find("CAS_number").text
        if casno in casnum_eurar:
            return "O"
    return "X" 