import pytest
import inspect
import os
import time
import logging

from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from Utilities.Config import Config


@pytest.mark.usefixtures("browser_setup")
class BaseClass():

    # To return the Type of Locator
    def getbyType(self, locatortype):

        locatortype, locatorvalue = locatortype
        locatortype = locatortype.lower()

        if locatortype == "id":
            return By.ID, locatorvalue
        elif locatortype == "xpath":
            return By.XPATH, locatorvalue
        elif locatortype == "class":
            return By.CLASS_NAME, locatorvalue
        elif locatortype == "css":
            return By.CSS_SELECTOR, locatorvalue
        elif locatortype == "linktext":
            return By.LINK_TEXT, locatorvalue
        elif locatortype == "name":
            return By.NAME, locatorvalue
        elif locatortype == "partiallinktext":
            return By.PARTIAL_LINK_TEXT, locatorvalue
        elif locatortype == "tagname":
            return By.TAG_NAME, locatorvalue
        else:
            print("Locator type is not supported")

    # Log File Function
    def getlogger(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        filehandler = logging.FileHandler(Config["Log_File_Path"])
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)
        return logger

    def explicit_wait(self, locatortype, locatorvalue):
        Web_Element = (locatortype, locatorvalue)
        locatortype, locatorvalue = self.getbyType(Web_Element)
        wait = WebDriverWait(self.driver, 25)
        wait.until(expected_conditions.presence_of_element_located((locatortype, locatorvalue)))

    def takeScreenshot(self):
        # Foldername=os.getcwd().split('TestReports')[0]+'TestReports'
        Foldername = Config["Screen_Shots_Path"]
        # if not os.path.isdir(Foldername+'SnapShots'):
        #     os.chdir(Foldername)
        #     os.mkdir(Foldername+'SnapShots/')
        filename = str(round(time.time() * 1000)) + ".png"
        try:
            self.driver.save_screenshot(Foldername + '/' + filename)

        except Exception as e:
            print("Exception is ", e)

    ###   Utility Functions   ###

    def Select_Value_From_List_Box(self, ele, text):
        select = Select(ele)
        if isinstance(text, str):
            select.select_by_visible_text(text)
        else:
            select.select_by_index(text)

    def Click_Element(self, locator):
        locator.click()

    def Enter_Value_In_Edit_Field(self, locator, value):
        locator.clear()
        locator.send_keys(value)

    def Mouse_Hover(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    def Mouse_Hover_Click(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element).click().perform()

    def Accept_Alert(self):
        alert = Alert(self.driver)
        alert.accept()

    def Dismiss_Alert(self):
        alert = Alert(self.driver)
        alert.dismiss()

    def Alert_Text(self):
        alert = Alert(self.driver)
        text = alert.text
        return text.strip() if alert.text.strip() else None





