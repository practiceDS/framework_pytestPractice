from base.base_driver import Basedriver
from pages import paths
from selenium.webdriver.common.by import By


class Login(Basedriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def enterusername_password(self, username, password):
        self.wait_until_element_is_located(By.XPATH, paths.USERNAME).send_keys(username)
        self.wait_until_element_is_located(By.XPATH, paths.PASSWORD).send_keys(password)

    def clicklogin(self):
        self.wait_until_element_is_clicklable(By.XPATH, paths.LOGIN).click()
