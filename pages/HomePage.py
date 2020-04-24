from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Utilities.BaseClass import BaseClass
from pages.CheckoutPage import CheckoutPage


class HomePage():

    def __init__(self,driver):
        self.driver=driver


    lnk_shop=(By.CSS_SELECTOR,"a[href*='shop']")
    name=(By.CSS_SELECTOR,"input[name='name']")
    email=(By.CSS_SELECTOR,"input[name='email']")
    gender=(By.XPATH,"//select[@id='exampleFormControlSelect1']")
    submit=(By.CSS_SELECTOR,"input[type='submit']")
    message=(By.XPATH,"//div[contains(@class,'alert')]")


    def clickshop(self):
        self.driver.find_element(*HomePage.lnk_shop).click()
        checkoutpage=CheckoutPage(self.driver)
        return checkoutpage

        #self.driver.find_element_by_css_selector("a[href*='shop']").click()

    def entername(self):
        return self.driver.find_element(*HomePage.name)

    def enteremail(self):
        return self.driver.find_element(*HomePage.email)

    def SelectGender(self):
        ele=self.driver.find_element(*HomePage.gender)
        return ele

    def Click_Submit(self):
        return self.driver.find_element(*HomePage.submit)

    def Get_Text(self):
        return self.driver.find_element(*HomePage.message)
