
from TestData.ExcelLib import *
from Utilities.UtilityFunctions import UtilityFunctions


class SelectFlightsPage(UtilityFunctions):

    SelectFlightsPageObjects=read_locators("SelectFlightsPage")

    def click_flights_reservation(self):
        btn_reserveflights=SelectFlightsPage.SelectFlightsPageObjects['btn_reserveflights']
        self.Click_Element(btn_reserveflights)
