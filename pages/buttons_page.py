"""
Page Object for Buttons page
Handles double-click, right-click and single-click interactions
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage
import time


class ButtonsPage(BasePage):
    """Buttons page object"""

    URL = "https://demoqa.com/buttons"

    # Button locators
    DOUBLE_CLICK_BTN  = (By.ID, "doubleClickBtn")
    RIGHT_CLICK_BTN   = (By.ID, "rightClickBtn")
    DYNAMIC_CLICK_BTN = (By.XPATH, "//button[text()='Click Me']")

    # Result message locators
    DOUBLE_CLICK_MESSAGE  = (By.ID, "doubleClickMessage")
    RIGHT_CLICK_MESSAGE   = (By.ID, "rightClickMessage")
    DYNAMIC_CLICK_MESSAGE = (By.ID, "dynamicClickMessage")

    def open(self):
        """Navigate to buttons page with fixed wait for page to settle"""
        self.driver.get(self.URL)
        time.sleep(4)  # Wait for page and ads to load

    def double_click_button(self):
        """Perform double click on the double-click button"""
        btn = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.DOUBLE_CLICK_BTN)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", btn)
        time.sleep(0.5)
        ActionChains(self.driver).double_click(btn).perform()
        time.sleep(1)

    def right_click_button(self):
        """Perform right click on the right-click button"""
        btn = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.RIGHT_CLICK_BTN)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", btn)
        time.sleep(0.5)
        ActionChains(self.driver).context_click(btn).perform()
        time.sleep(1)

    def click_dynamic_button(self):
        """Perform single click on the dynamic click button"""
        btn = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.DYNAMIC_CLICK_BTN)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", btn)
        self.driver.execute_script("arguments[0].click();", btn)
        time.sleep(1)

    def get_double_click_message(self):
        """Return message shown after double click"""
        msg = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.DOUBLE_CLICK_MESSAGE)
        )
        return msg.text

    def get_right_click_message(self):
        """Return message shown after right click"""
        msg = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.RIGHT_CLICK_MESSAGE)
        )
        return msg.text

    def get_dynamic_click_message(self):
        """Return message shown after single click"""
        msg = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.DYNAMIC_CLICK_MESSAGE)
        )
        return msg.text
