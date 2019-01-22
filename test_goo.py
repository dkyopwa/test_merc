"""
    Vladimir Nedved, 2019

"""

import pytest
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver import DesiredCapabilities
from goo import Goo
import os
import logging

class Test_Goo:
    def start_browser(self, browser, maximaze_window=True):
        """ Starting browser and return driver """
        path = './chromedriver'
        addr = 'https://google.com'
        remote_flag = True

        driver = None

        # set desktop browser
        if browser == 'Chrome':
            d = DesiredCapabilities.CHROME
            d['loggingPrefs'] = {'browser': 'ALL'}
            if remote_flag:
                driver = webdriver.Remote(
                    command_executor='http://selenium-hub:4444/wd/hub',
                    # desired_capabilities=DesiredCapabilities.CHROME)
                    desired_capabilities = d)
            else:
                driver = webdriver.Chrome(executable_path=path, desired_capabilities=d)
        else:
            if browser == 'Firefox':
                if remote_flag:
                    driver = webdriver.Remote(
                        command_executor='http://selenium-hub:4444/wd/hub',
                        desired_capabilities=DesiredCapabilities.FIREFOX)
                else:
                    driver = webdriver.Firefox(executable_path=path)
            else:
                logging.error('Not supported browser {}'.format(browser))
                exit(0)

        # check for remote execution (because driver.maximize_window doesn't work on remote)
        if remote_flag == 'False' and maximaze_window:
            try:
                driver.maximize_window()
            except WebDriverException:
                logging.warning("Message: unknown error: failed to change window state to maximized, current state is normal")
                driver.set_window_size(1820, 950)
            except:
                logging.warning("Message: unknown error when maximize window")
        else:
            driver.set_window_size(1920, 950)

        driver.get(addr)
        return driver

    def setup_method(self):
        """ The setUp method will get called before every test method (before execute fixture).
            If need to execute function after execute fixture use setup.
        """
        self.search_text = os.environ['SEARCH_TEXT']
        logging.info('Start test')

    def teardown_method(self):
        """  The tearDown method will get called after every test method  """
        logging.info('Stop test')

    def test_1(self, app):
        """ Open page, set keyword and check results """
        self.driver = self.start_browser(app.browser)

        goo = Goo(self.driver)
        assert goo.check_page(), 'Page not ready'
        assert goo.set_search_text(self.search_text), 'Search text didn\'t set'
        assert goo.click_search(), 'Error clicking button'
        assert goo.check_results(), 'There aren\'t results'
