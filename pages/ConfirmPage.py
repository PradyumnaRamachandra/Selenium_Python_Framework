from selenium.webdriver.common.by import By


class ConfirmPage():

    def __init__(self,driver):
        self.driver=driver


    delivery_location=(By.ID,"country")
    country=(By.XPATH,"//a[text()='India']")
    checkbox=(By.XPATH,"//div[@class='checkbox checkbox-primary']")
    purchase=(By.XPATH,"//input[@type='submit']")
    confirm_msg=(By.CSS_SELECTOR,"div[class*='alert-dismissible']")

    def enterDeliveryLocation(self):
        self.driver.find_element(*ConfirmPage.delivery_location).send_keys("Ind")
        #return self.driver.find_element(*ConfirmPage.delivery_location)

    def enterCountry(self):
        #return self.driver.find_element(*ConfirmPage.country)
        self.driver.find_element(*ConfirmPage.country).click()

    def clickcheckbox(self):
        #return self.driver.find_element(*ConfirmPage.checkbox)
        self.driver.find_element(*ConfirmPage.checkbox).click()

    def clickpurchase(self):
        #return self.driver.find_element(*ConfirmPage.purchase)
        self.driver.find_element(*ConfirmPage.purchase).click()

    def getConfirmText(self):
        return self.driver.find_element(*ConfirmPage.confirm_msg)
        #self.driver.find_element(*ConfirmPage.confirm_msg)