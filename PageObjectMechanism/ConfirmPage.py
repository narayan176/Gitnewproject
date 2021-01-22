from selenium import webdriver
from selenium.webdriver.common.by import By

class Confirmpage:

    def __init__(self, driver):
        self.driver = driver

    page1 = (By.ID, "country")
    page2 = (By.LINK_TEXT, "India")
    page3 = (By.XPATH, "//div[@class = 'checkbox checkbox-primary']")
    page4 = (By.CSS_SELECTOR, "[type = 'submit']" )

    def ConfirmPage1(self):
        return self.driver.find_element(*Confirmpage.page1)


    def ConfirmPage2(self):
        return self.driver.find_element(*Confirmpage.page2)

    def ConfirmPage3(self):
        return self.driver.find_element(*Confirmpage.page3)

    def ConfirmPage4(self):
        return self.driver.find_element(*Confirmpage.page4)
