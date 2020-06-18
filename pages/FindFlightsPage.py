
from TestData.ExcelLib import *

class FindFlightsPage():

    FindFlightsObjects=read_locators("FlightFinderPage")

    def __init__(self,driver):
        self.driver=driver

    def getoneway(self):
        rd_oneway=FindFlightsPage.FindFlightsObjects['rd_oneway']
        return self.driver.find_element(*rd_oneway)

    def getPassengers(self):
        lst_passengers=FindFlightsPage.FindFlightsObjects['lst_passengers']
        return self.driver.find_element(*lst_passengers)

    def getDeparting(self):
        lst_from=FindFlightsPage.FindFlightsObjects['lst_from']
        return self.driver.find_element(*lst_from)

    def getDepartingDate(self):
        lst_day=FindFlightsPage.FindFlightsObjects['lst_day']
        return self.driver.find_element(*lst_day)

    def getContinue(self):
        btn_continue=FindFlightsPage.FindFlightsObjects['btn_continue']
        return self.driver.find_element(*btn_continue)