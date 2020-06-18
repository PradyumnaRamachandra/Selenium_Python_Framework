
from TestData.ExcelLib import *

class ConfirmationPage():

    ConfirmationPageObjects=read_locators("ConfirmationPage")

    def __init__(self,driver):
        self.driver=driver

    def getConfirmation_msg(self):
        we_confirmation=ConfirmationPage.ConfirmationPageObjects['we_confirmation']
        return self.driver.find_element(*we_confirmation)

    def getLogOut(self):
        btn_Logout=ConfirmationPage.ConfirmationPageObjects['btn_Logout']
        return self.driver.find_element(*btn_Logout)

