import gspread
from oauth2client.service_account import ServiceAccountCredentials

#GooleSheet
scope = ["https://spreadsheets.google.com/feeds" ,'https://www.googleapis.com/auth/spreadsheets'
         ,"https://www.googleapis.com/auth/drive.file" ,"https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("<ServiceAccountsKeyJson>", scope)

clientSheet = gspread.authorize(creds)


class UploadGoogleSheet:
    def __init__(self, sheetName,sheetIndex,csvName):
        self.sheetName = sheetName
        self.sheetIndex = sheetIndex
        self.csvName = csvName

    def uploadcsv(self):
        #open via sheet's name
        spreadsheet = clientSheet.open(self.sheetName)
        #select worksheetID
        sheet = spreadsheet.get_worksheet(self.sheetIndex)
        #clear sheet for overwrite
        sheet.clear()
        with open(self.csvName, 'r') as file_obj:
            content = file_obj.read().encode('utf-8')
            clientSheet.import_csv(spreadsheet.id, data=content)

