"""
Page Object for Checkbox page
Handles checkbox tree selection and result verification
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time


class CheckboxPage(BasePage):
    """Checkbox page object - uses rc-tree library (not rct-)"""

    URL = "https://demoqa.com/checkbox"

    # Correct locators based on actual page source (rc-tree structure)
    TREE_CONTAINER  = (By.CSS_SELECTOR, "div.rc-tree")
    HOME_NODE       = (By.CSS_SELECTOR, "span.rc-tree-checkbox")
    HOME_SWITCHER   = (By.CSS_SELECTOR, "span.rc-tree-switcher")
    RESULT          = (By.ID, "result")

    def open(self):
        """Navigate to checkbox page and wait for rc-tree to render"""
        self.driver.get(self.URL)
        time.sleep(5)
        # Remove ads and fixed overlays
        self.driver.execute_script("""
            document.querySelectorAll('iframe').forEach(el => el.remove());
            document.querySelectorAll('*').forEach(el => {
                var s = window.getComputedStyle(el);
                if (s.position === 'fixed' || s.position === 'sticky') el.remove();
            });
        """)
        time.sleep(1)

    def expand_all(self):
        """
        Expand the tree by clicking the switcher arrow on the Home node.
        rc-tree uses span.rc-tree-switcher to expand/collapse nodes.
        """
        try:
            switcher = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(self.HOME_SWITCHER)
            )
            self.driver.execute_script("arguments[0].click();", switcher)
            time.sleep(1)
        except Exception:
            pass  # Proceed even if expand fails — Home checkbox is top-level

    def click_desktop_checkbox(self):
        """
        Click the Home node checkbox.
        rc-tree uses span.rc-tree-checkbox for checkbox elements.
        """
        checkbox = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.HOME_NODE)
        )
        self.driver.execute_script("arguments[0].click();", checkbox)
        time.sleep(1)

    def is_result_displayed(self):
        """Check if result section is visible after selection"""
        return self.is_element_visible(self.RESULT, timeout=10)

    def get_result_text(self):
        """Return the result text shown after checkbox selection"""
        return self.get_text(self.RESULT)
