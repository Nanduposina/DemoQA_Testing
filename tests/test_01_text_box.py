"""
Test Case TC_001: Text Box Form Submission
Feature: Verify that the text box form accepts user input and displays it correctly.

"""
import pytest
from pages.text_box_page import TextBoxPage


class TestTextBox:
    """
    Test class for Text Box page functionality.
    Covers: Feature 1 - Text Box Form Submission
    """

    def test_text_box_submission(self, driver):
        """
        TC_001: Submit text box form and verify output is displayed correctly.

        Steps:
            1. Navigate to the Text Box page
            2. Fill in full name, email, current address, permanent address
            3. Click the Submit button
            4. Assert that the output section is visible
            5. Assert that the output contains the entered name and email
        
        Expected Result: All entered data is displayed in the output section.
        """
        # Arrange: prepare page object and test input data
        page = TextBoxPage(driver)
        test_data = {
            "name": "Nandu posina",
            "email": "nandu.posina@example.com",
            "current_address": "123 Main Street, New York",
            "permanent_address": "456 Park Avenue, Boston"
        }

        # Act: open page, fill form, and submit
        page.open()
        page.fill_form(
            test_data["name"],
            test_data["email"],
            test_data["current_address"],
            test_data["permanent_address"]
        )
        page.submit_form()

        # Assert: output section is visible and contains correct data
        assert page.is_output_visible(), \
            "Output section should be visible after form submission"
        assert test_data["name"] in page.get_output_name(), \
            "Output should display the submitted name"
        assert test_data["email"] in page.get_output_email(), \
            "Output should display the submitted email"

        print("\n✓ TC_001 Passed: Text box form submitted and output verified")
