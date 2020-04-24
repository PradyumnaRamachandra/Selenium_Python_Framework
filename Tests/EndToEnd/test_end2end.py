import time
from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Utilities.BaseClass import BaseClass
from pages.CheckoutPage import CheckoutPage
from pages.ConfirmPage import ConfirmPage
from pages.HomePage import HomePage
from TestData.ExcelLib import *


ConfirmPageData=getTestData("EndToEnd","test_e2e")

class TestProductCart(BaseClass):

    @pytest.fixture(params=ConfirmPageData)
    def gettestdata(self,request):
        return request.param

    def test_e2e(self,gettestdata):

        #Logger Object
        log=self.getlogger()
        log.info("Test Started")

        #Home Page

        homepage=HomePage(self.driver)
        checkoutpage=homepage.clickshop()

        #Checkout Page

        #checkoutpage=CheckoutPage(self.driver)
        products = checkoutpage.getcardtitles()
        i=-1
        for product in products:
            i=i+1
            text = product.text
            log.info(text)
            if text == "Blackberry":
                checkoutpage.clickAddButton()[i].click()
                break

        checkoutpage.clickcartcheckout()
        confirmpage=checkoutpage.clickcheckout()

        #Confirm Page

        wait = WebDriverWait(self.driver, 25)
        # wait.until(expected_conditions.presence_of_element_located((By.ID, "country")))
        self.explicit_wait("Id","country")

       # confirmpage=ConfirmPage(self.driver)
        confirmpage.enterDeliveryLocation().send_keys(gettestdata["DeliveryLocation"])

        self.explicit_wait("xpath","//a[text()='India']")



        confirmpage.enterCountry()
        confirmpage.clickcheckbox()
        confirmpage.clickpurchase()

        self.explicit_wait("css","div[class*='alert-dismissible']")


        text = confirmpage.getConfirmText().text
        assert "Success" in text
        log.info(text)
        log.info("Purchase Completed Successfully")

        self.driver.get_screenshot_as_file("../ScreenShots/ScreenShot.png")
        log.info("Test Completed")