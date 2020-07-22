
from TestData.ExcelLib import *
from Utilities.UtilityFunctions import UtilityFunctions


class ConfirmationPage(UtilityFunctions):

    ConfirmationPageObjects=read_locators("ConfirmationPage")

    def get_Confirmation_msg(self):
        we_confirmation=ConfirmationPage.ConfirmationPageObjects['we_confirmation']
        return self.driver.find_element(*we_confirmation)

    def click_logOut(self):
        btn_logout=ConfirmationPage.ConfirmationPageObjects['btn_Logout']
        self.Click_Element(btn_logout)

