
from TestData.ExcelLib import *
from Utilities.UtilityFunctions import UtilityFunctions


class BookFlightPage(UtilityFunctions):

    BookFlightPageObjects=read_locators("BookFlightPage")

    def enter_firstname(self,value):
        txt_firstname=BookFlightPage.BookFlightPageObjects['txt_firstname']
        self.Enter_Value_In_Edit_Field(txt_firstname,value)

    def enter_lastname(self,value):
        txt_lastname=BookFlightPage.BookFlightPageObjects['txt_lastname']
        self.Enter_Value_In_Edit_Field(txt_lastname,value)

    def enter_creditCard(self,value):
        txt_creditcard=BookFlightPage.BookFlightPageObjects['txt_creditcard']
        self.Enter_Value_In_Edit_Field(txt_creditcard,value)

    def click_purchase(self):
        btn_purchase=BookFlightPage.BookFlightPageObjects['btn_purchase']
        self.Click_Element(btn_purchase)
