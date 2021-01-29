
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

#GooleSheet
scope = ["https://spreadsheets.google.com/feeds" ,'https://www.googleapis.com/auth/spreadsheets'
         ,"https://www.googleapis.com/auth/drive.file" ,"https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("<ServiceAccountsKeyJson>", scope)

clientSheet = gspread.authorize(creds)



class ExportGoogleSheet:
    def __init__(self, sheetName, sheetIndex):
        self.sheetName = sheetName
        self.sheetIndex = sheetIndex

    def GoogleSheetExport(self):
        try:
            # open via sheet's name
            sheet = clientSheet.open(self.sheetName).get_worksheet(self.sheetIndex)
            #export data
            data = sheet.get_all_records()

            dataFrame = pd.DataFrame(data)
            return dataFrame
        except Exception as e:
            return  str(e)
