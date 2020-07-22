
from TestData.ExcelLib import *
from Utilities.UtilityFunctions import UtilityFunctions


class FindFlightsPage(UtilityFunctions):

    FindFlightsObjects=read_locators("FlightFinderPage")

    def select_flights(self):
        lnk_flights=FindFlightsPage.FindFlightsObjects['lnk_flights']
        self.Click_Element(lnk_flights)

    def select_trip_type(self):
        rd_oneway=FindFlightsPage.FindFlightsObjects['rd_oneway']
        self.Click_Element(rd_oneway)

    def select_passengers(self,value):
        lst_passengers=FindFlightsPage.FindFlightsObjects['lst_passengers']
        self.Select_Value_From_List_Box(lst_passengers,value)

    def select_departing_from(self,value):
        lst_from=FindFlightsPage.FindFlightsObjects['lst_from']
        self.Select_Value_From_List_Box(lst_from, value)

    def select_departing_date(self,value):
        lst_day=FindFlightsPage.FindFlightsObjects['lst_day']
        self.Select_Value_From_List_Box(lst_day, value)

    def click_continue(self):
        btn_continue=FindFlightsPage.FindFlightsObjects['btn_continue']
        self.Click_Element(btn_continue)