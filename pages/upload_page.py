"""
Page Object for Upload/Download page
Handles file upload operations
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import os

class UploadDownloadPage(BasePage):
    """Upload/Download page object"""
    
    # Locators
    URL = "https://demoqa.com/upload-download"
    UPLOAD_INPUT = (By.ID, "uploadFile")
    UPLOADED_PATH = (By.ID, "uploadedFilePath")
    DOWNLOAD_BUTTON = (By.ID, "downloadButton")
    
    def open(self):
        """Navigate to upload/download page"""
        self.driver.get(self.URL)
    
    def upload_file(self, file_path):
        """Upload a file"""
        absolute_path = os.path.abspath(file_path)
        upload_element = self.driver.find_element(*self.UPLOAD_INPUT)
        upload_element.send_keys(absolute_path)
    
    def get_uploaded_file_path(self):
        """Get uploaded file path text"""
        return self.get_text(self.UPLOADED_PATH)
    
    def is_file_uploaded(self):
        """Check if file upload message is displayed"""
        return self.is_element_visible(self.UPLOADED_PATH)
