"""
Page Object for Practice Form page
Handles full form submission with multiple input types
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time


class PracticeFormPage(BasePage):
    """Practice Form page object"""

    URL = "https://demoqa.com/automation-practice-form"

    # Input locators
    FIRST_NAME      = (By.ID, "firstName")
    LAST_NAME       = (By.ID, "lastName")
    EMAIL           = (By.ID, "userEmail")
    MOBILE          = (By.ID, "userNumber")
    CURRENT_ADDRESS = (By.ID, "currentAddress")
    GENDER_MALE     = (By.XPATH, "//label[@for='gender-radio-1']")
    HOBBIES_SPORTS  = (By.XPATH, "//label[@for='hobbies-checkbox-1']")
    SUBMIT_BUTTON   = (By.ID, "submit")

    # Modal locator
    MODAL           = (By.CLASS_NAME, "modal-content")

    def open(self):
        """Navigate to practice form page and remove ads that intercept clicks"""
        max_retries = 3
        for attempt in range(max_retries):
            try:
                self.driver.get(self.URL)
                WebDriverWait(self.driver, 15).until(
                    EC.presence_of_element_located(self.FIRST_NAME)
                )
                time.sleep(1)
                # Remove ad iframes and fixed banners that block clicks
                self.driver.execute_script("""
                    // Remove all ad iframes
                    var iframes = document.querySelectorAll('iframe');
                    iframes.forEach(function(el) { el.remove(); });
                    // Remove fixed position elements (ad banners)
                    var allEls = document.querySelectorAll('*');
                    allEls.forEach(function(el) {
                        var style = window.getComputedStyle(el);
                        if (style.position === 'fixed' || style.position === 'sticky') {
                            el.remove();
                        }
                    });
                """)
                time.sleep(0.5)
                return
            except Exception as e:
                print(f"\n⚠ Attempt {attempt + 1} failed: {e}")
                if attempt < max_retries - 1:
                    time.sleep(5)
                else:
                    raise Exception(f"Practice form page failed after {max_retries} attempts.")

    def fill_form(self, first, last, email, mobile, address):
        """Fill all required fields in the practice form"""
        # Fill text fields
        self.enter_text(self.FIRST_NAME, first)
        self.enter_text(self.LAST_NAME, last)
        self.enter_text(self.EMAIL, email)
        self.enter_text(self.MOBILE, mobile)

        # Select gender using JavaScript to avoid overlay interference
        gender = self.driver.find_element(*self.GENDER_MALE)
        self.driver.execute_script("arguments[0].click();", gender)
        time.sleep(0.3)

        # Select hobbies checkbox using JavaScript click
        hobbies = self.driver.find_element(*self.HOBBIES_SPORTS)
        self.driver.execute_script("arguments[0].click();", hobbies)
        time.sleep(0.3)

        # Fill address
        self.enter_text(self.CURRENT_ADDRESS, address)

    def submit_form(self):
        """Submit form using JavaScript click to bypass any remaining overlays"""
        submit = self.driver.find_element(*self.SUBMIT_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", submit)
        time.sleep(0.5)
        self.driver.execute_script("arguments[0].click();", submit)
        time.sleep(2)

    def is_modal_displayed(self):
        """Check if confirmation modal appeared after submission"""
        return self.is_element_visible(self.MODAL, timeout=10)
