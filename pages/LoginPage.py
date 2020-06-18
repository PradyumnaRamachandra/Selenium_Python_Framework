
from TestData.ExcelLib import *

class LoginPage():

    LoginPageObjects=read_locators("LoginPage")

    def __init__(self,driver):
        self.driver=driver

    # lnk_shop=(By.CSS_SELECTOR,"a[href*='shop']")

    def getusername(self):
        txt_username=LoginPage.LoginPageObjects['txt_username']
        return self.driver.find_element(*txt_username)

    def getpassword(self):
        txt_password=LoginPage.LoginPageObjects['txt_password']
        return self.driver.find_element(*txt_password)

    def getsignin(self):
        txt_Signin=LoginPage.LoginPageObjects['txt_Signin']
        return self.driver.find_element(*txt_Signin)

    def getSignOff(self):
        lnk_SignOff=LoginPage.LoginPageObjects['lnk_SignOff']
        return self.driver.find_element(*lnk_SignOff)



