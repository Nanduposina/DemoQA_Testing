"""
Page Object for Radio Button page
Handles radio button selection
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class RadioButtonPage(BasePage):
    """Radio Button page object"""
    
    # Locators
    URL = "https://demoqa.com/radio-button"
    YES_RADIO = (By.CSS_SELECTOR, "label[for='yesRadio']")
    IMPRESSIVE_RADIO = (By.CSS_SELECTOR, "label[for='impressiveRadio']")
    NO_RADIO = (By.CSS_SELECTOR, "label[for='noRadio']")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "span.text-success")
    
    def open(self):
        """Navigate to radio button page"""
        self.driver.get(self.URL)
    
    def click_yes_radio(self):
        """Click Yes radio button"""
        self.click_element(self.YES_RADIO)
    
    def click_impressive_radio(self):
        """Click Impressive radio button"""
        self.click_element(self.IMPRESSIVE_RADIO)
    
    def get_selected_value(self):
        """Get selected radio button value"""
        return self.get_text(self.SUCCESS_MESSAGE)
    
    def is_result_displayed(self):
        """Check if result is displayed"""
        return self.is_element_visible(self.SUCCESS_MESSAGE)
