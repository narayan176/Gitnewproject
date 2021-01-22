from selenium import webdriver
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions

from PageObjectMechanism import HomePage
from PageObjectMechanism.CheckoutPage import CheckOutPage
from PageObjectMechanism.ConfirmPage import Confirmpage
from PageObjectMechanism.HomePage import Homepage
from Utility.BaseClassCode import BaseClass
class TestOne(BaseClass):
    def test_e2e(self):
        homePage = Homepage(self.driver)
        checkOutPage = homePage.ShopItem()
        #checkOutPage = CheckOutPage(self.driver)
        products = checkOutPage.getCardTitle()
        for product in products:
            productName = product.find_element_by_xpath("div/h4/a").text
            if productName == "Blackberry":
                product.find_element_by_xpath("div/button").click()
        checkOutPage.getCardTitle1().click()
        confirmPage = checkOutPage.getCardTitle2()
        #confirmPage = Confirmpage(self.driver)
        confirmPage.ConfirmPage1().send_keys("ind")
        self.VerifyLinkPresence("India")
        # wait = WebDriverWait(self.driver, 7)
        # wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        confirmPage.ConfirmPage2().click()
        confirmPage.ConfirmPage3().click()
        confirmPage.ConfirmPage4().click()
        successText = self.driver.find_element_by_class_name("alert-success").text
        assert "Success! Thank you!" in successText
        self.driver.get_screenshot_as_file("screen.png")