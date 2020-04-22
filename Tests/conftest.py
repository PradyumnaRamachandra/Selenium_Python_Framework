import datetime
import pytest
from selenium import webdriver

from Utilities.Config import Config
driver=None

# def pytest_addoption(parser):
#     parser.addoption(
#         "--browser_name", action="store", default="chrome"
#     )


@pytest.fixture(scope="class")
def browser_setup(request):
    #browser_name=request.config.getoption("browser_name")
    global driver
    if Config['Browser_Name'].upper() == "CHROME":
        driver = webdriver.Chrome(Config['Chrome_Driver_Path'])
    elif Config['Browser_Name'].upper() == "FIREFOX":
        driver = webdriver.Firefox(executable_path=r"C:\PythonProjects\Selenium_Python_Framework\Drivers\geckodriver.exe")
    else:
        driver = webdriver.Ie([Config['IE_Driver_Path']])

    driver.maximize_window()
    driver.implicitly_wait(Config['Wait_Time'])
    driver.get(Config['App_URL'])

    request.cls.driver=driver

    yield
    driver.close()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file("../TestReports/"+name)


