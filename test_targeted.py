import sys
import os

# Add error handling for executable distribution
if hasattr(sys, '_MEIPASS'):
    # Running as exe - add the bundled directory to path
    os.chdir(sys._MEIPASS)
else:
    # Running as script - use current directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Write debug output to file
debug_file = "e:/mahika_targeted_debug.txt"

try:
    with open(debug_file, "w") as f:
        f.write("Starting targeted test...\n")
    
    import customtkinter as ctk
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    
    with open(debug_file, "a") as f:
        f.write("Basic CTk setup done\n")
    
    # Test importing our modules
    from src.utils.enums.page_name import PageName
    with open(debug_file, "a") as f:
        f.write("PageName imported\n")
        f.write(f"LOGIN value: {PageName.LOGIN.value}\n")
    
    # Test creating main app window
    class TestApp(ctk.CTk):
        def __init__(self):
            super().__init__()
            with open(debug_file, "a") as f:
                f.write("TestApp CTk init done\n")
            
            # Test the problematic title setting
            self.title("Test App")
            with open(debug_file, "a") as f:
                f.write("Title set to string\n")
            
            # Test setting title with enum value
            self.title(PageName.LOGIN.value)
            with open(debug_file, "a") as f:
                f.write(f"Title set to enum value: {PageName.LOGIN.value}\n")
            
            # Test importing and creating LoginWindow
            from src.ui.login import LoginWindow
            with open(debug_file, "a") as f:
                f.write("LoginWindow imported\n")
            
            login_window = LoginWindow(self)
            with open(debug_file, "a") as f:
                f.write("LoginWindow created\n")
    
    with open(debug_file, "a") as f:
        f.write("Creating TestApp...\n")
    
    app = TestApp()
    
    with open(debug_file, "a") as f:
        f.write("TestApp created successfully - starting mainloop\n")
    
    app.mainloop()
    
except Exception as e:
    with open(debug_file, "a") as f:
        f.write(f"Error: {str(e)}\n")
        import traceback
        f.write(traceback.format_exc())
