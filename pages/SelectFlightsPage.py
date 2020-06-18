
from TestData.ExcelLib import *

class SelectFlightsPage():

    SelectFlightsPageObjects=read_locators("SelectFlightsPage")

    def __init__(self,driver):
        self.driver=driver

    def getflights_reservation(self):
        btn_reserveflights=SelectFlightsPage.SelectFlightsPageObjects['btn_reserveflights']
        return self.driver.find_element(*btn_reserveflights)
