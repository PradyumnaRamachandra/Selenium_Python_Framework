
from TestData.ExcelLib import *
from Utilities.BaseClass import BaseClass

from pages.BookFlightPage import BookFlightPage
from pages.ConfirmationPage import ConfirmationPage
from pages.FindFlightsPage import FindFlightsPage
from pages.LoginPage import LoginPage
import pytest

from pages.SelectFlightsPage import SelectFlightsPage

BookingData=getTestData("BookingModule","test_flightbooking")

class TestBooking(BaseClass):

    @pytest.fixture(params=BookingData)
    def BookingTestData(self,request):
        return request.param

    def test_flightbooking(self,BookingTestData):

        log=self.getlogger()
        log.info("Booking  Test Started")

        # LoginPage
        loginpage = LoginPage(self.driver)
        loginpage.Enter_Username(BookingTestData['UserName'])
        loginpage.Enter_Password(BookingTestData['Password'])
        loginpage.Click_Signin()

        #FindFlightsPage
        findflightspage=FindFlightsPage(self.driver)
        findflightspage.select_trip_type()
        findflightspage.select_passengers(BookingTestData['No_of_Passengers'])
        findflightspage.select_departing_from(BookingTestData['Departing_From'])
        findflightspage.select_departing_date(BookingTestData['Departing_Day'])
        findflightspage.click_continue()

        #SelectFlightsPage
        selectflightspage=SelectFlightsPage(self.driver)
        selectflightspage.click_flights_reservation()

        #BookFlightPage
        bookflightpage=BookFlightPage(self.driver)
        bookflightpage.enter_firstname(BookingTestData['Passenger_FirstName'])
        bookflightpage.enter_lastname(BookingTestData['Passenger_LastName'])
        bookflightpage.enter_creditCard(BookingTestData['CreditCard_No'])
        bookflightpage.click_purchase()

        #Confirmation Page
        confirmationpage=ConfirmationPage(self.driver)
        msg=self.driver.find_element(*confirmationpage.ConfirmationPageObjects['we_confirmation']).text

        assert "Your itinerary has been booked" in msg
        confirmationpage.takeScreenshot()

        confirmationpage.click_logOut()
        confirmationpage.explicit_wait(confirmationpage.ConfirmationPageObjects['btn_Logout'])

        log.info("Booking Test Completed")

