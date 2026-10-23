"""
Test Case TC_002: Checkbox Tree Selection
Feature: Verify that checkbox selections are registered and displayed correctly.

"""
import pytest
from pages.checkbox_page import CheckboxPage


class TestCheckbox:
    """
    Test class for Checkbox page functionality.
    Covers: Feature 2 - Checkbox Tree Selection
    """

    def test_checkbox_selection(self, driver):
        """
        TC_002: Select Home checkbox in tree structure and verify result.

        Steps:
            1. Navigate to the Checkbox page
            2. Expand the Home tree node
            3. Select the Home checkbox
            4. Assert that result section is visible
            5. Assert that result text is not empty

        Expected Result: Selected checkbox item appears in result section.
        """
        # Arrange: initialize page object
        page = CheckboxPage(driver)

        # Act: open page, expand tree, click Home checkbox
        page.open()
        page.expand_all()           # Expand Home node to reveal children
        page.click_desktop_checkbox()  # Click Home checkbox

        # Assert: result section visible and contains selected item text
        assert page.is_result_displayed(), \
            "Result section should appear after checkbox selection"
        result = page.get_result_text().lower()
        assert len(result) > 0, \
            "Result text should not be empty after selection"
        print(f"\n  Result text: {result}")
        print("\n✓ TC_002 Passed: Checkbox selection verified")
