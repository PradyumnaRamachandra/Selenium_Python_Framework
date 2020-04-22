import inspect
import os
import time
import pytest
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("browser_setup")
class BaseClass():

    def getbyType(self,locatortype):
        locatortype=locatortype.lower()
        if locatortype=="id":
            return By.ID
        elif locatortype=="xpath":
            return By.XPATH
        elif locatortype=="class":
            return By.CLASS_NAME
        elif locatortype=="css":
            return By.CSS_SELECTOR
        elif locatortype=="linktext":
            return By.LINK_TEXT
        elif locatortype=="name":
            return By.NAME
        elif locatortype=="partiallinktext":
            return By.PARTIAL_LINK_TEXT
        elif locatortype=="tagname":
            return By.TAG_NAME
        else:
            print("Locator type is not supported")


    def getlogger(self):
        loggername=inspect.stack()[1][3]
        logger=logging.getLogger(loggername)
        filehandler=logging.FileHandler("../Logs/logfile.log")
        formatter=logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)
        return logger

    def explicit_wait(self,locatortype,locatorvalue):
        bytype=self.getbyType(locatortype)
        wait = WebDriverWait(self.driver, 25)
        wait.until(expected_conditions.presence_of_element_located((bytype, locatorvalue)))

    def Select_Value_From_List_Box(self,ele,text):
        select = Select(ele)
        select.select_by_visible_text(text)


    def takeScreenshot(self):
        # Foldername=os.getcwd().split('TestReports')[0]+'TestReports'
        Foldername="../TestReports"
        if not os.path.isdir(Foldername+'/ScreenShots'):
            os.chdir(Foldername)
            os.mkdir(Foldername+'/ScreenShots/')
        filename=str(round(time.time()*1000))+".png"
        try:
            self.driver.save_screenshot(Foldername+'/ScreenShots/'+filename)
        except Exception as e:
            print("Exception is ",e)

    def Click_Element(self,locator):
        locator.click()