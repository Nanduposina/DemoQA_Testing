"""
Main Test Suite Executor
Runs all test cases and generates execution report

"""
import pytest
import sys
import time
from datetime import datetime

def main():
    """
    Execute all automated test cases
    Measures execution time and generates report
    """
    print("\n" + "="*70)
    print("DEMOQA AUTOMATED GUI TEST SUITE")
    print("="*70)
    print(f"Start Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Test Framework: Pytest + Selenium + Python")
    print(f"System Under Test: https://demoqa.com/")
    print("="*70 + "\n")
    
    # Record start time
    start_time = time.time()
    
    # Run all tests with detailed output
    pytest_args = [
        "tests/",
        "-v",  # Verbose output
        "--tb=short",  # Short traceback format
        "-s",  # Show print statements
        "--html=test_report.html",  # Generate HTML report (requires pytest-html)
        "--self-contained-html"  # Self-contained HTML report
    ]
    
    # Execute tests
    exit_code = pytest.main(pytest_args)
    
    # Record end time
    end_time = time.time()
    execution_time = end_time - start_time
    
    # Print summary
    print("\n" + "="*70)
    print("TEST EXECUTION SUMMARY")
    print("="*70)
    print(f"End Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Total Execution Time: {execution_time:.2f} seconds ({execution_time/60:.2f} minutes)")
    print(f"Exit Code: {exit_code}")
    
    if exit_code == 0:
        print("Status: ✓ ALL TESTS PASSED")
    else:
        print("Status: ✗ SOME TESTS FAILED")
    
    print("="*70 + "\n")
    
    return exit_code

if __name__ == "__main__":
    sys.exit(main())
