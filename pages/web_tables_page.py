"""
Page Object for Web Tables page
Handles CRUD operations on the data table
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time


class WebTablesPage(BasePage):
    """Web Tables page object"""

    URL = "https://demoqa.com/webtables"

    # Locators
    ADD_BUTTON    = (By.ID, "addNewRecordButton")
    FIRST_NAME    = (By.ID, "firstName")
    LAST_NAME     = (By.ID, "lastName")
    EMAIL         = (By.ID, "userEmail")
    AGE           = (By.ID, "age")
    SALARY        = (By.ID, "salary")
    DEPARTMENT    = (By.ID, "department")
    SUBMIT_BUTTON = (By.ID, "submit")
    DELETE_BUTTON = (By.CSS_SELECTOR, "span[title='Delete']")

    def open(self):
        """Navigate to web tables page with fixed wait"""
        self.driver.get(self.URL)
        time.sleep(5)

    def get_table_row_count(self):
        """
        Count filled data rows in the table.
        Uses multiple strategies since DemoQA uses ReactTable
        which renders empty placeholder rows alongside data rows.
        """
        time.sleep(2)

        # Strategy 1: count rows that have an edit/delete action button
        rows_with_actions = self.driver.find_elements(
            By.CSS_SELECTOR, "div.rt-tr-group div.action-buttons"
        )
        if len(rows_with_actions) > 0:
            return len(rows_with_actions)

        # Strategy 2: count rows where first cell has actual text content
        all_rows = self.driver.find_elements(
            By.CSS_SELECTOR, "div.rt-tr-group"
        )
        filled = []
        for row in all_rows:
            cells = row.find_elements(By.CSS_SELECTOR, "div.rt-td")
            if cells and cells[0].text.strip() not in ("", " "):
                filled.append(row)
        if len(filled) > 0:
            return len(filled)

        # Strategy 3: count by delete buttons present
        deletes = self.driver.find_elements(
            By.XPATH, "//*[@id='delete-record-undefined' or contains(@id,'delete-record')]"
        )
        if len(deletes) > 0:
            return len(deletes)

        # Strategy 4: fallback — count all non-empty tr-group rows
        rows = self.driver.find_elements(By.CSS_SELECTOR, ".rt-tr-group")
        return sum(1 for r in rows if r.text.strip() != "")

    def click_add(self):
        """Click Add button to open registration modal"""
        btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.ADD_BUTTON)
        )
        self.driver.execute_script("arguments[0].click();", btn)
        time.sleep(1)

    def fill_registration_form(self, first, last, email, age, salary, dept):
        """Fill all fields in the add record modal"""
        self.enter_text(self.FIRST_NAME, first)
        self.enter_text(self.LAST_NAME, last)
        self.enter_text(self.EMAIL, email)
        self.enter_text(self.AGE, age)
        self.enter_text(self.SALARY, salary)
        self.enter_text(self.DEPARTMENT, dept)

    def submit_form(self):
        """Submit the registration form using JavaScript click"""
        submit = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.SUBMIT_BUTTON)
        )
        self.driver.execute_script("arguments[0].click();", submit)
        time.sleep(2)

    def click_first_row_delete(self):
        """Click delete icon on the first table row"""
        delete_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.DELETE_BUTTON)
        )
        self.driver.execute_script("arguments[0].click();", delete_btn)
        time.sleep(1)
