"""
Pytest configuration file
Contains fixtures and setup/teardown logic shared across all tests
"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os
import time


@pytest.fixture(scope="function")
def driver():
    """
    Setup: Create and configure Chrome WebDriver before each test.
    Teardown: Quit browser after each test completes.
    scope="function" ensures a fresh browser for every test (test independence).
    """
    # Setup phase - configure Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-notifications")

    # Suppress automation detection banners
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    # Fix for Windows: ensure driver path points to .exe
    try:
        driver_path = ChromeDriverManager().install()
        if not driver_path.endswith('chromedriver.exe'):
            driver_dir = os.path.dirname(driver_path)
            for file in os.listdir(driver_dir):
                if file == 'chromedriver.exe':
                    driver_path = os.path.join(driver_dir, file)
                    break
        service = Service(driver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)
    except Exception:
        # Fallback: let Selenium locate chromedriver automatically
        driver = webdriver.Chrome(options=chrome_options)

    # Set page load timeout and implicit wait as safety nets
    driver.set_page_load_timeout(30)
    driver.implicitly_wait(5)

    yield driver  # Hand driver to test

    # Teardown phase - always runs even if test fails
    time.sleep(1)
    driver.quit()


@pytest.fixture(scope="session", autouse=True)
def test_session_info():
    """Print session header and footer around the entire test run"""
    print("\n" + "=" * 60)
    print("DemoQA Automated Test Suite")
    print("Test Framework: Pytest + Selenium + Python")
    print("=" * 60)
    yield
    print("\n" + "=" * 60)
    print("Test Suite Execution Complete")
    print("=" * 60)
