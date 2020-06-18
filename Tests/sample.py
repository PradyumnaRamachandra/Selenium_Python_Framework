from selenium import webdriver
from TestData.ExcelLib import *

# import openpyxl
#
# workbook=openpyxl.load_workbook("C:\\Users\\pr57\\Desktop\\Selenium_Python\\TestObjects1.xlsx")
# worksheet=workbook["HomePage"]
# dict={}
# rows=worksheet.max_row
# cols=worksheet.max_column
# for row in range(1,rows+1):
#     for col in range(1,cols+1):
#         # print(worksheet.cell(row=row,column=col).value)
#         dict.update({worksheet.cell(row=row,column=1).value:(worksheet.cell(row=row,column=2).value,worksheet.cell(row=row,column=3).value)})
#
# print(dict)
# class sample():
#     FormPageObjects = read_locators("FormPage")
#
#
#     def method(self):
#         print(sample.FormPageObjects['txt_name'])
#
# a=sample()
# print(a.method())

# for index,i in enumerate(range(0,5)):
# #     print(index,i)
#
# def binary_search(alist, key):
#     """Search key in alist[start... end - 1]."""
#     start = 0
#     end = len(alist)
#     while start < end:
#         mid = (start + end)//2
#         if alist[mid] > key:
#             end = mid
#         elif alist[mid] < key:
#             start = mid + 1
#         else:
#             return mid
#     return -1
#
# index=binary_search([2,4,3,5,6],5)
# print(index)

# a=[2,3,4,5,6,7,8]
#
# def search(sortedlist,key):
#     for index,i in enumerate(sortedlist):
#         if key==i:
#             return index
#
#
# b=search(a,6)
# print(b)