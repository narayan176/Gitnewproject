import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:
     def VerifyLinkPresence(self, text):
      wait = WebDriverWait(self.driver, 7)
      wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))