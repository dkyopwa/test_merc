from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES

WAITING_TIMEOUT = 5

class BasePage(object):
    """ Base class to initialize the base page that will be called from all pages.
        Implementation of class, that set selenuim driver and defined common functions.
    """

    def __init__(self, driver, top_element_locator=None):
        self.driver = driver
        self.top_element_locator = top_element_locator


    def is_element_present(self, locator):
        """ Check present of element.
            Return element, if it available or None in other case.
        """
        try:
            element = WebDriverWait(self.driver, WAITING_TIMEOUT).until(
                ES.presence_of_element_located(locator)
            )
            return element
        except:
            print("There isn't '{}' element".format(locator))
            return None


    def is_elements_present(self, locator):
        """ Check present of elements.
            Return elements (array), if they available or None in other case.
        """
        try:
            elements = WebDriverWait(self.driver, WAITING_TIMEOUT).until(
                ES.presence_of_all_elements_located(locator)
            )
            return elements
        except:
            print("There isn't '{}' elements".format(locator))
            return list()


    def is_element_visible(self, locator, scroll_to = True):
        """ Check element visibility in browser.
            Return element, if it available on viewport or None in other case.
        """
        try:
            element = WebDriverWait(self.driver, WAITING_TIMEOUT).until(
                ES.visibility_of_element_located(locator)
            )
            return element
        except:
            print("Element '{}' doesn't visible".format(locator))
            return None
