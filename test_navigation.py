#!/usr/bin/env python3
"""
Test script to verify navigation functionality
Run this to test Shift+H (back) and Shift+L (forward) navigation
"""

import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.ui.app import App
from src.utils.enums.page_name import PageName

def test_navigation():
    print("Navigation Test Instructions:")
    print("1. Application will start with Login page")
    print("2. Login with any credentials")
    print("3. Navigate through pages using normal keys (j to enter, l/h to move)")
    print("4. Use Shift+H to go back to previous page")
    print("5. Use Shift+L to go forward (if available)")
    print("6. Test on all pages: Login -> File List -> Word List -> Word Detail")
    print("-" * 60)
    
    app = App()
    app.mainloop()

if __name__ == "__main__":
    test_navigation()
