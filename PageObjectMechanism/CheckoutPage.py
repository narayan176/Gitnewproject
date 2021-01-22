from selenium.webdriver.common.by import By


from selenium.webdriver.common.by import By

from PageObjectMechanism.ConfirmPage import Confirmpage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    CardTitle = (By.XPATH, "//div[@class='card h-100']")
    CardTitle1 =(By.CSS_SELECTOR, "a[class*='btn-primary']")
    CardTitle2 = (By.XPATH, "//button[@class = 'btn btn-success']")


    def getCardTitle(self):
        return self.driver.find_elements(*CheckOutPage.CardTitle)

    def getCardTitle1(self):
        return self.driver.find_element(*CheckOutPage.CardTitle1)

    def getCardTitle2(self):
        self.driver.find_element(*CheckOutPage.CardTitle2).click()
        confirmPage = Confirmpage(self.driver)
        return confirmPage




