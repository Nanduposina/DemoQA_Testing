"""
Page Object for Alerts page
Handles alert, confirm, and prompt dialogs
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time

class AlertsPage(BasePage):
    """Alerts page object"""
    
    # Locators
    URL = "https://demoqa.com/alerts"
    ALERT_BUTTON = (By.ID, "alertButton")
    TIMER_ALERT_BUTTON = (By.ID, "timerAlertButton")
    CONFIRM_BUTTON = (By.ID, "confirmButton")
    PROMPT_BUTTON = (By.ID, "promtButton")
    CONFIRM_RESULT = (By.ID, "confirmResult")
    PROMPT_RESULT = (By.ID, "promptResult")
    
    def open(self):
        """Navigate to alerts page"""
        self.driver.get(self.URL)
    
    def click_alert_button(self):
        """Click simple alert button"""
        self.click_element(self.ALERT_BUTTON)
    
    def click_timer_alert_button(self):
        """Click timer alert button"""
        self.click_element(self.TIMER_ALERT_BUTTON)
    
    def click_confirm_button(self):
        """Click confirm button"""
        self.click_element(self.CONFIRM_BUTTON)
    
    def click_prompt_button(self):
        """Click prompt button"""
        self.click_element(self.PROMPT_BUTTON)
    
    def accept_alert(self):
        """Accept alert dialog"""
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()
    
    def dismiss_alert(self):
        """Dismiss alert dialog"""
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.dismiss()
    
    def send_text_to_alert(self, text):
        """Send text to prompt alert"""
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.send_keys(text)
        alert.accept()
    
    def get_confirm_result(self):
        """Get confirm result text"""
        return self.get_text(self.CONFIRM_RESULT)
    
    def get_prompt_result(self):
        """Get prompt result text"""
        return self.get_text(self.PROMPT_RESULT)
