"""
Base Page Object Model class
Contains common methods shared by all page objects
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

class BasePage:
    """Base class for all page objects"""

    def __init__(self, driver):
        """Initialize base page with driver and longer default timeout"""
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)  # Increased from 10 to 20 seconds

    def find_element(self, locator):
        """Find single element with explicit wait"""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_elements(self, locator):
        """Find multiple elements"""
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click_element(self, locator):
        """Click on element after scrolling into view"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.scroll_to_element(element)
        element.click()

    def enter_text(self, locator, text):
        """Clear field and enter text"""
        element = self.find_element(locator)
        self.scroll_to_element(element)
        element.clear()
        element.send_keys(text)

    def scroll_to_element(self, element):
        """Scroll element into view using JavaScript"""
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(0.3)

    def get_text(self, locator):
        """Get visible text from element"""
        element = self.find_element(locator)
        return element.text

    def is_element_visible(self, locator, timeout=5):
        """Check if element is visible within given timeout"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False
