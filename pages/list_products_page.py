from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_driver import Basedriver
from pages import paths


class Product(Basedriver):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def select_product(self,productName):
        findpath = paths.PRODUCT_DETAILS+"'"+productName+"']"
        self.wait_until_element_is_clicklable(By.XPATH,findpath).click()

