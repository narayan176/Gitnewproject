#self.driver.find_element_by_css_selector("a[href*= 'shop']").click()
from selenium.webdriver.common.by import By

from PageObjectMechanism.CheckoutPage import CheckOutPage


class Homepage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*= 'shop']")
    def ShopItem(self):
         self.driver.find_element(*Homepage.shop).click()
         checkOutPage = CheckOutPage(self.driver)
         return checkOutPage

