"""
Test Case TC_007: File Upload
Feature: Verify that a file can be uploaded and path is confirmed.

"""
import pytest
import os
from pages.upload_page import UploadDownloadPage


class TestUpload:
    """
    Test class for Upload/Download page functionality.
    Covers: Feature 7 - File Upload
    """

    def test_file_upload(self, driver):
        """
        TC_007: Upload a file and verify the file path is displayed.

        Steps:
            1. Create a sample text file in test_data/ if not present
            2. Navigate to Upload/Download page
            3. Send file path to the upload input element
            4. Assert upload confirmation is visible
            5. Assert uploaded file name appears in confirmation
        
        Expected Result: File upload is confirmed with correct file name shown.
        """
        # Arrange: create test file if it doesn't already exist
        page = UploadDownloadPage(driver)
        test_file_path = "test_data/sample_file.txt"
        os.makedirs("test_data", exist_ok=True)
        if not os.path.exists(test_file_path):
            with open(test_file_path, "w") as f:
                f.write("Test file for automated upload testing.")

        # Act: open page and upload the file
        page.open()
        page.upload_file(test_file_path)  # Sends absolute path to file input

        # Assert: upload confirmation is shown with correct file name
        assert page.is_file_uploaded(), \
            "File upload confirmation should be displayed"
        assert "sample_file.txt" in page.get_uploaded_file_path(), \
            "Uploaded file name should appear in confirmation"

        print("\n✓ TC_007 Passed: File upload verified")
