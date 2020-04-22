
import openpyxl

def getTestData(sheetname,testcase_name):

    workbook = openpyxl.load_workbook("../TestData/TestData.xlsx")
    worksheet = workbook[sheetname]
    data = []
    rows = worksheet.max_row
    cols = worksheet.max_column
    for row in range(1, rows + 1):
        # To pick only if Execute is "Yes"
        if worksheet.cell(row=row, column=1).value == testcase_name and worksheet.cell(row=row,column=cols).value == "Yes":
            temp = {}
            for col in range(2, cols):  # To Eliminate Execute Column
                temp[worksheet.cell(row=1, column=col).value] = worksheet.cell(row=row, column=col).value
            data.append(temp)

    return data