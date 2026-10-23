"""
Test Case TC_005: Button Click Actions
Feature: Verify that double-click, right-click, and single-click are recognized.

"""
import pytest
from pages.buttons_page import ButtonsPage


class TestButtons:
    """
    Test class for Buttons page functionality.
    Covers: Feature 5 - Button Click Actions
    """

    def test_button_clicks(self, driver):
        """
        TC_005: Perform different click types and verify messages appear.

        Steps:
            1. Navigate to the Buttons page
            2. Double-click the first button, assert message
            3. Right-click the second button, assert message
            4. Single-click the third button, assert message
        
        Expected Result: Each click type triggers its corresponding message.
        """
        # Arrange: initialize page object
        page = ButtonsPage(driver)
        page.open()

        # Act & Assert: double click
        page.double_click_button()
        assert "double click" in page.get_double_click_message().lower(), \
            "Double click message should appear"

        # Act & Assert: right click
        page.right_click_button()
        assert "right click" in page.get_right_click_message().lower(), \
            "Right click message should appear"

        # Act & Assert: dynamic single click
        page.click_dynamic_button()
        assert "dynamic click" in page.get_dynamic_click_message().lower(), \
            "Dynamic click message should appear"

        print("\n✓ TC_005 Passed: All click types verified")
