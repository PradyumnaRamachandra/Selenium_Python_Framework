
from TestData.ExcelLib import *
from Utilities.BaseClass import BaseClass

from pages.BookFlightPage import BookFlightPage
from pages.ConfirmationPage import ConfirmationPage
from pages.FindFlightsPage import FindFlightsPage
from pages.LoginPage import LoginPage
import pytest
import time
from pages.SelectFlightsPage import SelectFlightsPage

BookingData=getTestData("BookingModule","test_flightbooking")

class TestBooking(BaseClass):

    @pytest.fixture(params=BookingData)
    def BookingTestData(self,request):
        return request.param

    def test_flightbooking(self,BookingTestData):

        log=self.getlogger()
        log.info("Booking  Test Started")

        #LoginPage
        loginpage=LoginPage(self.driver)
        self.Enter_Value_In_Edit_Field(loginpage.getusername(),BookingTestData['UserName'])
        self.Enter_Value_In_Edit_Field(loginpage.getpassword(),BookingTestData['Password'])
        self.takeScreenshot()
        self.Click_Element(loginpage.getsignin())
        self.explicit_wait("xpath","//input[@value='roundtrip']")

        #FindFlightsPage
        findflightspage=FindFlightsPage(self.driver)
        self.Click_Element(findflightspage.getoneway())
        self.Select_Value_From_List_Box(findflightspage.getPassengers(),BookingTestData['No_of_Passengers'])
        self.Select_Value_From_List_Box(findflightspage.getDeparting(),BookingTestData['Departing_From'])
        self.Select_Value_From_List_Box(findflightspage.getDepartingDate(),BookingTestData['Departing_Day'])
        self.takeScreenshot()
        self.Click_Element(findflightspage.getContinue())
        self.explicit_wait("xpath","(//font[contains(text(),'DEPART')])[1]")

        #SelectFlightsPage
        selectflightspage=SelectFlightsPage(self.driver)
        self.takeScreenshot()
        self.Click_Element(selectflightspage.getflights_reservation())
        self.explicit_wait("name","passFirst0")

        #BookFlightPage
        bookflightpage=BookFlightPage(self.driver)
        self.Enter_Value_In_Edit_Field(bookflightpage.getFirstname(),BookingTestData['Passenger_FirstName'])
        self.Enter_Value_In_Edit_Field(bookflightpage.getLastname(),BookingTestData['Passenger_LastName'])
        self.Enter_Value_In_Edit_Field(bookflightpage.getCreditCard(),BookingTestData['CreditCard_No'])
        self.takeScreenshot()
        self.Click_Element(bookflightpage.getPurchase())
        self.explicit_wait("xpath","//font[contains(text(),'booked')]")

        #Confirmation Page
        confirmationpage=ConfirmationPage(self.driver)
        msg=confirmationpage.getConfirmation_msg().text
        assert "Your itinerary has been booked" in msg
        self.takeScreenshot()
        self.Click_Element(confirmationpage.getLogOut())
        self.explicit_wait("name","login")

        log.info("Booking Test Completed")

