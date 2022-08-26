from appium import webdriver
import unittest


class CellPhone(unittest.TestCase):
    def __init__(self):
        self.desired_capabilities = {
            "appium:platformVersion": "11",
            "appium:UDID": "t8ibyp8xgi95xsga",
            "platformName": "Android",
            "appium:noReset": True,
            "appium:deviceName": "Redmi",
            "appium:ignoreHiddenApiPolicyError": True
        }

    def start_server(self):
        driver = webdriver.Remote("http://localhost:4723/wd/hub", self.desired_capabilities)
        return driver
