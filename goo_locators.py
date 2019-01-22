from selenium.webdriver.common.by import By

class GooLocators:
    """
        Locators for google page

    """
    LOGO = (By.ID, 'hplogo')
    SEARCH = (By.NAME, 'q')
    BTN = (By.NAME, 'btnK')
    RESULTS = (By.CLASS_NAME, 'g')
