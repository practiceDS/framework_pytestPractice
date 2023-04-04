from selenium.webdriver.common.by import By
from pages import paths

class AddPersonalInfo():
    def __init__(self,driver):
        self.driver = driver

    def add_personal_information(self,FirstName,LastName,Pincode):
        self.driver.find_element(By.XPATH, paths.FIRSTNAME).send_keys(FirstName)
        self.driver.find_element(By.XPATH, paths.LASTNAME).send_keys(LastName)
        self.driver.find_element(By.XPATH, paths.PINCODE).send_keys(Pincode)
        self.driver.find_element(By.XPATH, paths.CONTINUE_BUTTON).click()



