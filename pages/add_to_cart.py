from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages import paths
from base.base_driver import Basedriver


class AddCart(Basedriver):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def add_to_cart(self):
        self.wait_until_element_is_clicklable(By.XPATH,paths.ADD_CART).click()
        self.wait_until_element_is_clicklable(By.XPATH,paths.SHOPPING_CART).click()


