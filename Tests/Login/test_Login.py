# Test Case
from TestData.ExcelLib import *
from Utilities.BaseTest import BaseTest

from pages.LoginPage import LoginPage
import pytest
import time

LoginData=getTestData("LoginModule","test_LoginTest")

class TestLogin(BaseTest):

    @pytest.fixture(params=LoginData)
    def LoginTestData(self,request):
        return request.param

    def test_LoginTest(self,LoginTestData):


        #LoginPage
        loginpage=LoginPage(self.driver)
        loginpage.Enter_Username(LoginTestData['UserName'])
        loginpage.Enter_Password(LoginTestData['Password'])
        loginpage.takeScreenshot()
        loginpage.Click_Signin()
        loginpage.Click_SignOff()


