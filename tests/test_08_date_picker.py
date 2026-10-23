"""
Test Case TC_008: Date Picker Selection
Feature: Verify that a date can be selected and displayed in the input field.

"""
import pytest
from pages.date_picker_page import DatePickerPage


class TestDatePicker:
    """
    Test class for Date Picker page functionality.
    Covers: Feature 8 - Date Picker Selection
    """

    def test_date_selection(self, driver):
        """
        TC_008: Enter a date using the date picker and verify it is set.

        Steps:
            1. Navigate to the Date Picker page
            2. Assert date input is displayed
            3. Enter date value using keyboard input
            4. Assert the input field holds the correct date
        
        Expected Result: Selected date appears correctly in the input field.
        """
        # Arrange: define expected date value
        page = DatePickerPage(driver)
        test_date = "12/25/2025"  # MM/DD/YYYY format expected by DemoQA

        # Act: open page and enter date
        page.open()
        assert page.is_date_picker_displayed(), \
            "Date picker input should be visible on page"
        page.select_date(test_date)  # Clears field and types date

        # Assert: input field holds the exact entered date
        assert "12/25/2025" in page.get_selected_date(), \
            f"Date field should contain {test_date}"

        print("\n✓ TC_008 Passed: Date picker selection verified")
