from base_page import BasePage
from goo_locators import GooLocators
from selenium.webdriver.common.keys import Keys

class Goo(BasePage, GooLocators):
    """ google page class """

    def check_page(self):
        """ Check page for ready to use """
        if self.is_element_visible(self.LOGO) and \
            self.is_element_present(self.SEARCH) and \
            self.is_element_present(self.BTN):
            return True
        return False

    def set_search_text(self, text, send_enter=False):
        """ Type text in the text area and press Enter if set flag """
        elem = self.is_element_visible(self.SEARCH)
        if elem:
            elem.clear()
            elem.send_keys(text)
            if send_enter:
                elem.send_keys(Keys.ENTER)
            return True
        return False

    def click_search(self):
        """ Cleck search button if not press Enter """
        btn = self.is_element_visible(self.BTN)
        if btn:
            btn.click()
            return True
        return False

    def check_results(self):
        """ Get results and return count of its """
        elems = self.is_elements_present(self.RESULTS)
        return len(elems)