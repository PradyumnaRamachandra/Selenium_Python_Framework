
from TestData.ExcelLib import *

class BookFlightPage():

    BookFlightPageObjects=read_locators("BookFlightPage")

    def __init__(self,driver):
        self.driver=driver

    def getFirstname(self):
        txt_firstname=BookFlightPage.BookFlightPageObjects['txt_firstname']
        return self.driver.find_element(*txt_firstname)

    def getLastname(self):
        txt_lastname=BookFlightPage.BookFlightPageObjects['txt_lastname']
        return self.driver.find_element(*txt_lastname)

    def getCreditCard(self):
        txt_creditcard=BookFlightPage.BookFlightPageObjects['txt_creditcard']
        return self.driver.find_element(*txt_creditcard)

    def getPurchase(self):
        btn_purchase=BookFlightPage.BookFlightPageObjects['btn_purchase']
        return self.driver.find_element(*btn_purchase)
