"""
Page Object for Date Picker page
Handles date selection
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage

class DatePickerPage(BasePage):
    """Date Picker page object"""
    
    # Locators
    URL = "https://demoqa.com/date-picker"
    DATE_INPUT = (By.ID, "datePickerMonthYearInput")
    DATE_TIME_INPUT = (By.ID, "dateAndTimePickerInput")
    
    def open(self):
        """Navigate to date picker page"""
        self.driver.get(self.URL)
    
    def select_date(self, date_string):
        """Select date by entering text (format: MM/DD/YYYY)"""
        element = self.find_element(self.DATE_INPUT)
        self.scroll_to_element(element)
        element.click()
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(date_string)
        element.send_keys(Keys.ENTER)
    
    def get_selected_date(self):
        """Get selected date value"""
        element = self.find_element(self.DATE_INPUT)
        return element.get_attribute("value")
    
    def is_date_picker_displayed(self):
        """Check if date picker is displayed"""
        return self.is_element_visible(self.DATE_INPUT)
