from selenium.webdriver.common.by import By
from TestData.ExcelLib import *
from Utilities.BaseClass import BaseClass


class FormPage(BaseClass):

    # Read Locators from TestObjects File
    FormPageObjects = read_locators("FormPage")

    def __init__(self,driver):
        self.driver=driver

    def getName(self):
        txt_name=self.getbyType(FormPage.FormPageObjects['txt_name'])
        return self.driver.find_element(*txt_name)

    def getEmail(self):
        txt_email=self.getbyType(FormPage.FormPageObjects['txt_email'])
        return self.driver.find_element(*txt_email)

    def getCheckBox(self):
        txt_checkbox=self.getbyType(FormPage.FormPageObjects['txt_checkbox'])
        return self.driver.find_element(*txt_checkbox)

    def getGender(self):
        lst_Gender=self.getbyType(FormPage.FormPageObjects['lst_Gender'])
        return self.driver.find_element(*lst_Gender)

    def getEmploymentStatus(self):
        rd_EmploymentStatus=self.getbyType(FormPage.FormPageObjects['rd_EmploymentStatus'])
        return self.driver.find_element(*rd_EmploymentStatus)

    def getDOB(self):
        txt_DOB=self.getbyType(FormPage.FormPageObjects['txt_DOB'])
        return self.driver.find_element(*txt_DOB)

    def getSubmit(self):
        btn_Submit=self.getbyType(FormPage.FormPageObjects['btn_Submit'])
        return self.driver.find_element(*btn_Submit)

    def getMessage(self):
        message=self.getbyType(FormPage.FormPageObjects['message'])
        return self.driver.find_element(*message)