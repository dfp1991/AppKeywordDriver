from config import ActionKeywords
from utility import ExcelUtils


def executeActions():
    method = dir(ActionKeywords)
    for i in range(len(method)):
        if method[i] == sActionKeyword:
            func = getattr(ActionKeywords, method[i])
            func()
            break

if __name__ == '__main__':
    excel_path = ""
    sheet_name = ""
    ExcelUtils.getExcelFile(excel_path, sheet_name)
    for iRow in range(1, 6):
        sActionKeyword = ExcelUtils.getCellData(excel_path, sheet_name, iRow, 3)
        executeActions()





