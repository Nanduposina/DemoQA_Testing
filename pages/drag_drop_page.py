"""
Page Object for Droppable page
Handles drag and drop operations
"""
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from pages.base_page import BasePage

class DragDropPage(BasePage):
    """Drag and Drop page object"""
    
    # Locators
    URL = "https://demoqa.com/droppable"
    DRAG_BOX = (By.ID, "draggable")
    DROP_BOX = (By.ID, "droppable")
    DROP_TEXT = (By.XPATH, "//div[@id='droppable']/p")
    
    def open(self):
        """Navigate to droppable page"""
        self.driver.get(self.URL)
    
    def drag_and_drop(self):
        """Perform drag and drop operation"""
        source = self.find_element(self.DRAG_BOX)
        target = self.find_element(self.DROP_BOX)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source, target).perform()
    
    def get_drop_text(self):
        """Get drop box text"""
        return self.get_text(self.DROP_TEXT)
    
    def get_drop_box_color(self):
        """Get drop box background color"""
        element = self.find_element(self.DROP_BOX)
        return element.value_of_css_property("background-color")
