"""
Test Case TC_004: Web Table CRUD Operations
Feature: Verify adding and deleting records in a web table.

"""
import pytest
from pages.web_tables_page import WebTablesPage


class TestWebTables:
    """
    Test class for Web Tables page functionality.
    Covers: Feature 4 - Web Table Data Management
    """

    def test_add_and_delete_record(self, driver):
        """
        TC_004: Add a new record to the table and verify it appears.

        Steps:
            1. Navigate to the Web Tables page
            2. Record initial number of rows
            3. Click Add, fill the registration form, submit
            4. Assert row count increased after adding
            5. Click delete on first available record
            6. Assert row count decreased after deleting

        Expected Result: Table correctly reflects add and delete operations.
        """
        # Arrange: initialize page and define new record data
        page = WebTablesPage(driver)
        test_data = {
            "first_name": "Alice", "last_name": "Smith",
            "email": "alice.smith@test.com", "age": "30",
            "salary": "75000", "department": "QA"
        }

        # Act: open page
        page.open()
        initial_count = page.get_table_row_count()
        print(f"\n  Initial row count: {initial_count}")

        # Act: add a new record
        page.click_add()
        page.fill_registration_form(
            test_data["first_name"], test_data["last_name"],
            test_data["email"], test_data["age"],
            test_data["salary"], test_data["department"]
        )
        page.submit_form()

        # Assert: row count increased after adding
        after_add_count = page.get_table_row_count()
        print(f"  After add count: {after_add_count}")
        assert after_add_count > initial_count, \
            f"Row count should increase after adding. Before: {initial_count}, After: {after_add_count}"

        # Act: delete first record
        page.click_first_row_delete()

        # Assert: row count decreased after deleting
        after_delete_count = page.get_table_row_count()
        print(f"  After delete count: {after_delete_count}")
        assert after_delete_count < after_add_count, \
            f"Row count should decrease after deleting. Before delete: {after_add_count}, After: {after_delete_count}"

        print("\n✓ TC_004 Passed: Web table add and delete operations verified")
