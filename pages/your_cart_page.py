from selenium.webdriver.common.by import By
from pages import paths
from base.base_driver import Basedriver


class YourCart(Basedriver):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def checkout_cart(self):
        self.wait_until_element_is_clicklable(By.XPATH, paths.CHECKOUT_BUTTON).click()
