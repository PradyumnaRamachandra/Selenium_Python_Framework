
from TestData.ExcelLib import *
from Utilities.BaseClass import BaseClass

from pages.LoginPage import LoginPage
import pytest
import time

LoginData=getTestData("LoginModule","test_LoginTest")

class TestLogin(BaseClass):

    @pytest.fixture(params=LoginData)
    def LoginTestData(self,request):
        return request.param

    def test_LoginTest(self,LoginTestData):

        log=self.getlogger()
        log.info("Login Test Started")

        #LoginPage
        loginpage=LoginPage(self.driver)
        loginpage.Enter_Username(LoginTestData['UserName'])
        loginpage.Enter_Password(LoginTestData['Password'])
        loginpage.takeScreenshot()
        loginpage.Click_Signin()
        loginpage.Click_SignOff()
        log.info("Login Test Completed")

