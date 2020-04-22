from TestData.ExcelLib import *
from Utilities.BaseClass import BaseClass
from pages.HomePage import HomePage
import pytest
import time


homepage_data=getTestData("HomePage","test_formsubmission")


class TestHomePage(BaseClass):
    @pytest.fixture(params=homepage_data)
    def getTestData(self,request):
        return request.param


    def test_formsubmission(self,getTestData):

        log=self.getlogger()
        log.info("Test Started")

        #Homepage
        homepage=HomePage(self.driver)
        homepage.entername().send_keys(getTestData["First_Name"])
        homepage.enteremail().send_keys(getTestData["Email"])
        homepage.SelectGender()
        self.Select_Value_From_List_Box(homepage.SelectGender(), getTestData["Gender"])
        homepage.Click_Submit().click()

        self.explicit_wait("xpath","//div[contains(@class,'alert')]")
        text=homepage.Get_Text().text
        log.info(text)
        self.takeScreenshot()
        assert "Success" in text,"Text is not present"
        self.driver.refresh()
        time.sleep(1)
        log.info("Test Completed")





