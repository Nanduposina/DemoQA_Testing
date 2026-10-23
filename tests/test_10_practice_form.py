"""
Test Case TC_010: Practice Form Validation
Feature: Verify comprehensive form accepts valid input and shows confirmation.

"""
import pytest
from pages.practice_form_page import PracticeFormPage


class TestPracticeForm:
    """
    Test class for Practice Form page functionality.
    Covers: Feature 10 - Practice Form Validation
    """

    def test_form_submission(self, driver):
        """
        TC_010: Fill and submit the practice form with valid data.

        Steps:
            1. Navigate to the Practice Form page
            2. Fill first name, last name, email, gender, mobile, address
            3. Submit the form
            4. Assert confirmation modal is displayed
        
        Expected Result: Submission succeeds and confirmation modal appears.
        """
        # Arrange: define valid form input data
        page = PracticeFormPage(driver)
        test_data = {
            "first_name": "Emma",
            "last_name": "Johnson",
            "email": "emma.johnson@test.com",
            "mobile": "1234567890",
            "address": "789 Oak Street, Chicago"
        }

        # Act: open page and fill form with all required fields
        page.open()
        page.fill_form(
            test_data["first_name"],
            test_data["last_name"],
            test_data["email"],
            test_data["mobile"],
            test_data["address"]
        )

        # Act: submit form
        page.submit_form()

        # Assert: confirmation modal appears after successful submission
        assert page.is_modal_displayed(), \
            "Confirmation modal should display after valid form submission"

        print("\n✓ TC_010 Passed: Practice form submission verified")
