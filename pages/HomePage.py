from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Utilities.BaseClass import BaseClass
from pages.CheckoutPage import CheckoutPage
from TestData.ExcelLib import *

class HomePage(BaseClass):

    HomePageObjects=read_locators("HomePage")

    def __init__(self,driver):
        self.driver=driver


    # lnk_shop=(By.CSS_SELECTOR,"a[href*='shop']")
    # name=(By.CSS_SELECTOR,"input[name='name']")
    # email=(By.CSS_SELECTOR,"input[name='email']")
    # gender=(By.XPATH,"//select[@id='exampleFormControlSelect1']")
    # submit=(By.CSS_SELECTOR,"input[type='submit']")
    # message=(By.XPATH,"//div[contains(@class,'alert')]")


    def clickshop(self):
        lnk_shop=self.getbyType(HomePage.HomePageObjects['lnk_shop'])
        self.driver.find_element(*lnk_shop).click()
        checkoutpage=CheckoutPage(self.driver)
        return checkoutpage

    def entername(self):
        name=self.getbyType(HomePage.HomePageObjects['name'])
        return self.driver.find_element(*name)

    def enteremail(self):
        email=self.getbyType(HomePage.HomePageObjects['email'])
        return self.driver.find_element(*email)

    def SelectGender(self):
        gender=self.getbyType(HomePage.HomePageObjects['gender'])
        ele=self.driver.find_element(*gender)
        return ele

    def Click_Submit(self):
        submit=self.getbyType(HomePage.HomePageObjects['submit'])
        return self.driver.find_element(*submit)

    def Get_Text(self):
        message=self.getbyType(HomePage.HomePageObjects['message'])
        return self.driver.find_element(*message)
