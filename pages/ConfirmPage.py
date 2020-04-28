from selenium.webdriver.common.by import By

from Utilities.BaseClass import BaseClass

from TestData.ExcelLib import *

class ConfirmPage(BaseClass):

    ConfirmPageObjects=read_locators("ConfirmPage")

    def __init__(self,driver):
        self.driver=driver

    def enterDeliveryLocation(self):
        delivery_location=self.getbyType(ConfirmPage.ConfirmPageObjects['delivery_location'])
        return self.driver.find_element(*delivery_location)

    def enterCountry(self):
        country=self.getbyType(ConfirmPage.ConfirmPageObjects['country'])
        self.driver.find_element(*country).click()

    def clickcheckbox(self):
        checkbox=self.getbyType(ConfirmPage.ConfirmPageObjects['checkbox'])
        self.driver.find_element(*checkbox).click()

    def clickpurchase(self):
        purchase=self.getbyType(ConfirmPage.ConfirmPageObjects['purchase'])
        self.driver.find_element(*purchase).click()

    def getConfirmText(self):
        confirm_msg=self.getbyType(ConfirmPage.ConfirmPageObjects['confirm_msg'])
        return self.driver.find_element(*confirm_msg)