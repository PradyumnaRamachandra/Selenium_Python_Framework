from selenium.webdriver.common.by import By

from Utilities.BaseClass import BaseClass
from pages.ConfirmPage import ConfirmPage
from TestData.ExcelLib import *

class CheckoutPage(BaseClass):

    checkoutpageobjects=read_locators("CheckoutPage")

    def __init__(self,driver):
        self.driver=driver

    # cardtitle=(By.XPATH,"//h4[@class='card-title']/a")

    def getcardtitles(self):
        cardtitle=self.getbyType(CheckoutPage.checkoutpageobjects['cardtitle'])
        return self.driver.find_elements(*cardtitle)

    def clickAddButton(self):
        addbutton=self.getbyType(CheckoutPage.checkoutpageobjects['addbutton'])
        return self.driver.find_elements(*addbutton)

    def clickcartcheckout(self):
        cartcheckout=self.getbyType(CheckoutPage.checkoutpageobjects['cartcheckout'])
        self.driver.find_element(*cartcheckout).click()


    def clickcheckout(self):
        checkout=self.getbyType(CheckoutPage.checkoutpageobjects['checkout'])
        self.driver.find_element(*checkout).click()
        confirmpage=ConfirmPage(self.driver)
        return confirmpage
