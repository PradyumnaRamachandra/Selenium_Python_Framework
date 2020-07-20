
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
        self.Enter_Value_In_Edit_Field(loginpage.getusername(),LoginTestData['UserName'])
        self.Enter_Value_In_Edit_Field(loginpage.getpassword(),LoginTestData['Password'])
        self.takeScreenshot()
        self.Click_Element(loginpage.getsignin())
        # self.explicit_wait("xpath","//input[@value='roundtrip']")
        self.explicit_wait("xpath","//a[text()='SIGN-OFF']")
        self.Click_Element(loginpage.getSignOff())
        self.explicit_wait("name","submit")
        log.info("Login Test Completed")

