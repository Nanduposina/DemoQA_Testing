"""
Test Cases TC_006a/b/c: Alert Dialog Handling
Feature: Verify simple alert, confirm alert, and prompt alert are handled correctly.

"""
import pytest
from pages.alerts_page import AlertsPage


class TestAlerts:
    """
    Test class for Alerts page functionality.
    Covers: Feature 6 - JavaScript Alert Handling
    """

    def test_simple_alert(self, driver):
        """
        TC_006a: Trigger a simple alert and dismiss it.

        Steps:
            1. Navigate to Alerts page
            2. Click the Alert button
            3. Accept the alert dialog
        
        Expected Result: Alert is dismissed without error.
        """
        # Arrange
        page = AlertsPage(driver)
        page.open()

        # Act: trigger and accept the simple alert
        page.click_alert_button()
        page.accept_alert()  # Dismiss by clicking OK

        # Assert: no exception means alert was handled successfully
        print("\n✓ TC_006a Passed: Simple alert dismissed")

    def test_confirm_alert(self, driver):
        """
        TC_006b: Trigger confirm alert, click OK, and verify result message.

        Steps:
            1. Navigate to Alerts page
            2. Click Confirm button to trigger dialog
            3. Accept the confirm dialog
            4. Assert result shows 'Ok'
        
        Expected Result: Confirm result shows user clicked OK.
        """
        # Arrange
        page = AlertsPage(driver)
        page.open()

        # Act: trigger confirm alert and accept it
        page.click_confirm_button()
        page.accept_alert()

        # Assert: result message reflects OK was chosen
        assert "Ok" in page.get_confirm_result(), \
            "Confirm result should indicate 'Ok' was selected"

        print("\n✓ TC_006b Passed: Confirm alert accepted and result verified")

    def test_prompt_alert(self, driver):
        """
        TC_006c: Trigger prompt alert, enter text, and verify result.

        Steps:
            1. Navigate to Alerts page
            2. Click Prompt button
            3. Enter text into the prompt dialog
            4. Assert the entered text is displayed on the page
        
        Expected Result: Page displays the text entered in the prompt.
        """
        # Arrange
        page = AlertsPage(driver)
        test_name = "TestUser"  # Text to enter into the prompt
        page.open()

        # Act: trigger prompt, send text, and confirm
        page.click_prompt_button()
        page.send_text_to_alert(test_name)

        # Assert: entered text appears in result
        assert test_name in page.get_prompt_result(), \
            f"Prompt result should contain '{test_name}'"

        print("\n✓ TC_006c Passed: Prompt alert input verified")
