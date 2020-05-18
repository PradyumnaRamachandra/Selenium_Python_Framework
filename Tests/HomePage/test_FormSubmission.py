import time
import pytest
from TestData.ExcelLib import *
from Utilities.BaseClass import BaseClass
from pages.FormPage import FormPage

formpagedata=getTestData("FormPage","test_formstests")

#To validate for Test data rows

# if len(formpagedata)==0:
# #     print("No Test Data Rows Selected")

class TestFormSubmission(BaseClass):

    @pytest.fixture(params=formpagedata)
    def gettestdata(self,request):
        return request.param


    def test_formstests(self,gettestdata):

        formpage=FormPage(self.driver)

        #EnterName
        self.Enter_Value_In_Edit_Field(formpage.getName(),gettestdata["First_Name"])

        #Enter Email
        self.Enter_Value_In_Edit_Field(formpage.getEmail(),gettestdata["Email"])

        #Click on CheckBox
        self.Click_Element(formpage.getCheckBox())

        #Select Gender
        self.Select_Value_From_List_Box(formpage.getGender(),gettestdata["Gender"])

        #Click on Employment Status
        self.Click_Element(formpage.getEmploymentStatus())

        #Enter DOB
        formpage.getDOB().send_keys(gettestdata["Date_Of_Birth"])
        # self.Enter_Value_In_Edit_Field(formpage.getDOB(),gettestdata["Date_Of_Birth"])

        #Click Submit Button
        self.Click_Element(formpage.getSubmit())

        time.sleep(1)

        #Get Message
        text=formpage.getMessage().text
        assert "Success" in text,"Text is not matching"





