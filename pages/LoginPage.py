
from TestData.ExcelLib import *
from Utilities.UtilityFunctions import UtilityFunctions


class LoginPage(UtilityFunctions):

    LoginPageObjects=read_locators("LoginPage")

    def Enter_Username(self,username):
        txt_username=LoginPage.LoginPageObjects['txt_username']
        self.Enter_Value_In_Edit_Field(txt_username,username)

    def Enter_Password(self,password):
        txt_password=LoginPage.LoginPageObjects['txt_password']
        self.Enter_Value_In_Edit_Field(txt_password, password)

    def Click_Signin(self):
        txt_Signin=LoginPage.LoginPageObjects['txt_Signin']
        self.Click_Element(txt_Signin)

    def Click_SignOff(self):
        lnk_SignOff=LoginPage.LoginPageObjects['lnk_SignOff']
        self.Click_Element(lnk_SignOff)



