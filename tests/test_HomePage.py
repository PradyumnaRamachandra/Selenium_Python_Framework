from TestData.HomePageData import HomePageData
from Utilities.BaseClass import BaseClass
from pages.HomePage import HomePage
import pytest
import time



class TestHomePage(BaseClass):

    @pytest.fixture(params=HomePageData.test_HomePage)
    def getTestData(self,request):
        return request.param


    def test_formsubmission(self,getTestData):

        log=self.getlogger()
        log.info("Test Started")
        self.driver

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
        assert "Success" in text,"Text is not present"
        self.driver.refresh()
        time.sleep(1)
        log.info("Test Completed")





