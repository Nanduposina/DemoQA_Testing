"""
Page Object for Text Box page
Handles text input form submission and output verification
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time


class TextBoxPage(BasePage):
    """Text Box page object"""

    # Page URL
    URL = "https://demoqa.com/text-box"

    # Input field locators
    FULL_NAME = (By.ID, "userName")
    EMAIL = (By.ID, "userEmail")
    CURRENT_ADDRESS = (By.ID, "currentAddress")
    PERMANENT_ADDRESS = (By.ID, "permanentAddress")
    SUBMIT_BUTTON = (By.ID, "submit")

    # Output field locators
    OUTPUT_NAME = (By.ID, "name")
    OUTPUT_EMAIL = (By.ID, "email")
    OUTPUT_CURRENT_ADDRESS = (By.XPATH, "//p[@id='currentAddress']")
    OUTPUT_PERMANENT_ADDRESS = (By.XPATH, "//p[@id='permanentAddress']")

    def open(self):
        """Navigate to text box page and wait until input field is present"""
        max_retries = 3
        for attempt in range(max_retries):
            try:
                self.driver.get(self.URL)
                WebDriverWait(self.driver, 15).until(
                    EC.presence_of_element_located(self.FULL_NAME)
                )
                time.sleep(1)
                return
            except Exception as e:
                print(f"\n⚠ Attempt {attempt + 1} failed: {e}")
                if attempt < max_retries - 1:
                    print("Retrying in 5 seconds...")
                    time.sleep(5)
                else:
                    raise Exception(
                        f"Page {self.URL} failed to load after {max_retries} attempts."
                    )

    def fill_form(self, name, email, current_addr, permanent_addr):
        """Fill all four fields of the text box form"""
        self.enter_text(self.FULL_NAME, name)
        self.enter_text(self.EMAIL, email)
        self.enter_text(self.CURRENT_ADDRESS, current_addr)
        self.enter_text(self.PERMANENT_ADDRESS, permanent_addr)

    def submit_form(self):
        """Click the Submit button using JavaScript to bypass any ad overlay"""
        submit_btn = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.SUBMIT_BUTTON)
        )
        self.driver.execute_script("arguments[0].click();", submit_btn)

    def get_output_name(self):
        """Return the name text from the output section"""
        return self.get_text(self.OUTPUT_NAME)

    def get_output_email(self):
        """Return the email text from the output section"""
        return self.get_text(self.OUTPUT_EMAIL)

    def is_output_visible(self):
        """Check whether the output section appeared after submission"""
        return self.is_element_visible(self.OUTPUT_NAME, timeout=10)
