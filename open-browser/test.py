import os
from time import sleep

import unittest
import argparse
import json
import re

from appium import webdriver

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class OpenBrowserTests(unittest.TestCase):

    def setUp(self):
        desired_caps =  {
            "deviceName":"Android",
            "app" : PATH("./app-debug.apk"),
            "app-package":"com.urucas.appiumtests",
            "appWaitActivity": "com.urucas.appiumtests.activities.MainActivity",
            "browserName" : "",
            "platformName":"Android",
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

    def tearDown(self):
        # end the session
        self.driver.quit()

    def test_check_contexts(self):
        sleep(.5)
        contexts = self.driver.contexts
        self.assertIsNotNone(contexts)
        self.assertEqual(contexts[0], "NATIVE_APP")
        el = self.driver.find_element_by_id("openBrowserBtt")
        self.assertIsNotNone(el)
        el.click()
        sleep(.5)
        el = self.driver.find_element_by_id("openBrowserBtt")
        self.assertIsNotNone(el)
        el.click()
        sleep(1.5)
        contexts = self.driver.contexts
        print contexts


if __name__ == '__main__':
    # run test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(OpenBrowserTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

