from selenium.webdriver.common.by import By

from pages.ConfirmPage import ConfirmPage


class CheckoutPage():

    def __init__(self,driver):
        self.driver=driver


    cardtitle=(By.XPATH,"//h4[@class='card-title']/a")
    addbutton=(By.XPATH,"//div[@class='card-footer']/button")
    cartcheckout=(By.CSS_SELECTOR,"a[class*='btn-primary']")
    checkout=(By.CSS_SELECTOR,"button[class*='btn-success']")

    def getcardtitles(self):
        return self.driver.find_elements(*CheckoutPage.cardtitle)

    def clickAddButton(self):
        return self.driver.find_elements(*CheckoutPage.addbutton)

    def clickcartcheckout(self):
        #return self.driver.find_element(*CheckoutPage.cartcheckout)
        self.driver.find_element(*CheckoutPage.cartcheckout).click()


    def clickcheckout(self):
        #return self.driver.find_element(*CheckoutPage.checkout)
        self.driver.find_element(*CheckoutPage.checkout).click()
        confirmpage=ConfirmPage(self.driver)
        return confirmpage
