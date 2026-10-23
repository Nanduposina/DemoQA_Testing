"""
Helper utilities for test automation
Provides common functions used across test cases
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

class TestHelpers:
    """Helper methods for test execution"""
    
    @staticmethod
    def wait_for_element(driver, locator, timeout=10):
        """Wait for element to be visible"""
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return element
        except TimeoutException:
            print(f"Element {locator} not found within {timeout} seconds")
            return None
    
    @staticmethod
    def wait_for_element_clickable(driver, locator, timeout=10):
        """Wait for element to be clickable"""
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            return element
        except TimeoutException:
            print(f"Element {locator} not clickable within {timeout} seconds")
            return None
    
    @staticmethod
    def scroll_to_element(driver, element):
        """Scroll element into view"""
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(0.5)
    
    @staticmethod
    def take_screenshot(driver, filename):
        """Take screenshot and save to file"""
        driver.save_screenshot(filename)
