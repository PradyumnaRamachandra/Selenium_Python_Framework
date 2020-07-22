import pytest
import inspect
import logging

from Utilities.Config import Config


@pytest.mark.usefixtures("browser_setup")
class BaseClass():

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





