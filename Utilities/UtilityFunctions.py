import inspect
import logging
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from Utilities.Config import Config

#Decorator for Auto Sync wait
def sync_wait(func):
    def inner(*args,**kwargs):
        instance,locator,*value=args
        locatortype,locatorvalue=locator
        wait=WebDriverWait(instance.driver,25,poll_frequency=0.5)
        wait.until(expected_conditions.presence_of_element_located((locatortype,locatorvalue)))
        return func(*args,**kwargs)

    return inner

#Log Function
def getlogger():
    loggername = inspect.stack()[1][3]
    logger = logging.getLogger(loggername)
    filehandler = logging.FileHandler(Config["Log_File_Path"])
    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)
    logger.setLevel(logging.INFO)
    return logger

class UtilityFunctions():

    def __init__(self,driver):
        self.driver=driver

    #To log Info
    log=getlogger()

    # To return the Type of Locator
    def getbyType(self, locator):
        if len(locator)!=2:
            raise AttributeError("Locator not entered correctly in 'Test_Objects' Sheet")

        locatortype, locatorvalue = locator
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
            self.log.info("Locator type is not supported")

    @sync_wait
    def Select_Value_From_List_Box(self, locator, text):
        locatortype,locatorvalue=self.getbyType(locator)
        element=self.driver.find_element(locatortype,locatorvalue)
        select = Select(element)
        if isinstance(text, str):
            select.select_by_visible_text(text)
            self.log.info(f'Selected {text} value in {locatorvalue}')
        else:
            select.select_by_index(text)
            self.log.info(f'Selected {text} value in {locatorvalue}')

    @sync_wait
    def Click_Element(self, locator):
        locatortype, locatorvalue = self.getbyType(locator)
        self.driver.find_element(locatortype,locatorvalue).click()
        self.log.info(f'Clicked on {locatorvalue} value')

    @sync_wait
    def Enter_Value_In_Edit_Field(self, locator, value):
        locatortype, locatorvalue = self.getbyType(locator)
        self.driver.find_element(locatortype,locatorvalue).clear()
        self.driver.find_element(locatortype, locatorvalue).send_keys(value)
        self.log.info(f'Entered {value} on {locatorvalue} value')


    @sync_wait
    def Mouse_Hover(self, locator):
        locatortype, locatorvalue = self.getbyType(locator)
        element=self.driver.find_element(locatortype,locatorvalue)
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    @sync_wait
    def Mouse_Hover_Click(self, locator):
        locatortype, locatorvalue = self.getbyType(locator)
        element=self.driver.find_element(locatortype,locatorvalue)
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

    def explicit_wait(self, locator):
        locatortype, locatorvalue = self.getbyType(locator)
        wait = WebDriverWait(self.driver, 25)
        wait.until(expected_conditions.presence_of_element_located((locatortype, locatorvalue)))

    def select_multiple_items(self, locator, *items):
        locatortype, locatorvalue = self.getbyType(locator)
        element = self.driver.find_element(locatortype, locatorvalue)
        select = Select(element)
        select.deselect_all()
        for item in items:
            if isinstance(item, str):
                select.select_by_visible_text(item)
            else:
                select.select_by_index(item)

    def send_keyboard_input(self, key):
        action = ActionChains(self.driver)
        if key.upper() == 'ARROW_DOWN':
            action.send_keys(Keys.ARROW_DOWN).perform()
            self.log.info('Performed keyboard action Arrow Down')
        elif key.upper() == 'ARROW_UP':
            action.send_keys(Keys.ARROW_UP).perform()
            self.log.info('Performed keyboard action Arrow Up')
        elif key.upper() == 'BACK_SPACE':
            action.send_keys(Keys.BACK_SPACE).perform()
            self.log.info('Performed keyboard action Back Space')
        elif key.upper() == 'ESCAPE':
            action.send_keys(Keys.ESCAPE).perform()
            self.log.info('Performed keyboard action Escape')
        elif key.upper() == 'TAB':
            action.send_keys(Keys.TAB).perform()
            self.log.info('Performed keyboard action Tab')
        elif key.upper() == 'ENTER':
            action.send_keys(Keys.ENTER).perform()
            self.log.info('Performed keyboard action Enter')

    def switch_to_window(self, window_index):
        if window_index < len(self.driver.window_handles):
            self.driver.switch_to.window(self.driver.window_handles[window_index])
            self.log.info(f'Switched to window index: {window_index}')
        else:
            raise Exception(f'Window index :{window_index} does not exist')

    def switch_to_parent_window(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.log.info('Switched to Parent window')

    def js_scroll_up(self):
        self.driver.execute_script('window.scrollBy(0,-300)')
        self.log.info('Scrolling Up')

    def js_scroll_down(self):
        self.driver.execute_script('window.scrollBy(0,300)')
        self.log.info('Scrolling Down')

    def js_scroll_right(self):
        self.driver.execute_script('window.scrollBy(300,0)')
        self.log.info('Scrolling Right')

    def js_scroll_left(self):
        self.driver.execute_script('window.scrollBy(-300,0)')
        self.log.info('Scrolling Left')

    def js_scroll_element(self, locator):
        locatortype, locatorvalue = self.getbyType(locator)
        element = self.driver.find_element(locatortype, locatorvalue)
        self.driver.execute_script('arguments[0].scrollIntoView()', element)
        self.log.info(f'Scrolling to element { locatorvalue }')

    def get_web_elements(self, locator):
        locatortype, locatorvalue = self.getbyType(locator)
        return self.driver.find_elements(locatortype, locatorvalue)

##################################################################################################################