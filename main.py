import export
import upload


if __name__ == '__main__':

    #export data
    objectExport = export.ExportGoogleSheet("<sheetName>", <sheetIndex>)
    dataFrame = objectExport.GoogleSheetExport()
    print(dataFrame)

    #upload data
    objectUpload = upload.UploadGoogleSheet("<sheetName>", <sheetIndex>,"<csvName>")
    Status = objectUpload.uploadcsv()
    print(Status)


