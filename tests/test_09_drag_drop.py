"""
Test Case TC_009: Drag and Drop
Feature: Verify draggable element can be dropped into target zone.

"""
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time


class TestDragDrop:
    """
    Test class for Droppable page functionality.
    Covers: Feature 9 - Drag and Drop
    """

    def test_drag_and_drop(self, driver):
        """
        TC_009: Drag element into drop zone and verify success message.

        Steps:
            1. Navigate to Droppable page
            2. Wait for drag and drop elements to load
            3. Record initial drop zone text
            4. Perform drag and drop action using ActionChains
            5. Assert drop zone text changed to 'Dropped!'
        
        Expected Result: Drop zone displays 'Dropped!' after successful drop.
        """
        # Act: navigate directly and wait for full page load
        driver.get("https://demoqa.com/droppable")
        time.sleep(3)  # Extra wait needed due to ads loading on this page

        # Wait explicitly for draggable element to be present in DOM
        drag_box = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "draggable"))
        )
        drop_box = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "droppable"))
        )

        # Scroll drag element into view to ensure it's interactable
        driver.execute_script("arguments[0].scrollIntoView(true);", drag_box)
        time.sleep(1)

        # Record initial drop zone text before action
        initial_text = drop_box.text
        print(f"Initial drop box text: '{initial_text}'")

        # Act: perform drag and drop using ActionChains
        actions = ActionChains(driver)
        actions.drag_and_drop(drag_box, drop_box).perform()
        time.sleep(2)  # Allow animation to complete

        # Assert: drop zone text changed confirming successful drop
        final_text = drop_box.text
        print(f"Final drop box text: '{final_text}'")
        assert "Dropped!" in final_text, \
            f"Expected 'Dropped!' but got '{final_text}'"

        print("\n✓ TC_009 Passed: Drag and drop verified")
