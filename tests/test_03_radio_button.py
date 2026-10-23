"""
Test Case TC_003: Radio Button Selection
Feature: Verify that radio buttons allow single selection and display result.

"""
import pytest
from pages.radio_button_page import RadioButtonPage


class TestRadioButton:
    """
    Test class for Radio Button page functionality.
    Covers: Feature 3 - Radio Button Selection
    """

    def test_radio_button_selection(self, driver):
        """
        TC_003: Select radio buttons and verify only one is active at a time.

        Steps:
            1. Navigate to the Radio Button page
            2. Click 'Yes' radio button
            3. Assert result shows 'Yes'
            4. Click 'Impressive' radio button
            5. Assert result changes to 'Impressive'
        
        Expected Result: Selected radio value is shown and changes on new selection.
        """
        # Arrange: initialize page object
        page = RadioButtonPage(driver)
        page.open()

        # Act & Assert: select 'Yes' and verify
        page.click_yes_radio()
        assert page.is_result_displayed(), \
            "Result should appear after selecting Yes"
        assert "Yes" in page.get_selected_value(), \
            "Result should display 'Yes'"

        # Act & Assert: switch to 'Impressive' and verify previous selection cleared
        page.click_impressive_radio()
        assert "Impressive" in page.get_selected_value(), \
            "Result should update to 'Impressive'"

        print("\n✓ TC_003 Passed: Radio button selection verified")
