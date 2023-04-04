from selenium.webdriver.common.by import By
from pages import paths
from base.base_driver import Basedriver


class PurchaseComplete(Basedriver):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def vaildate_purchase_success(self):
        self.wait_until_element_is_clicklable(By.XPATH, paths.FINISH_PURCHASE).click()
        text = self.driver.find_element(By.XPATH, paths.ORDER_PLACED).text
        actual_string = "Thank you for your order!"
        if text == actual_string:
            assert True
        else:
            assert False