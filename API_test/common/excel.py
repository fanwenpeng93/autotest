import xlrd,json,os
from common.config import allpath
path=allpath+"/API_test/testcasedir/test.xlsx"
class Xl:
    def __init__(self,sheetname):
        self.workbook = xlrd.open_workbook(path, on_demand=True)
        self.sheet=self.workbook.sheet_by_name(sheet_name=sheetname)
    def get_rows(self):
        return self.sheet.nrows
    def get_rows_values(self,row):
        self.list_values=self.sheet.row_values(row,1,8)
        return self.list_values
if __name__=="__main__":
    pass





