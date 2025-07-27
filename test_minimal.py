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
debug_file = "e:/mahika_test_debug.txt"

try:
    with open(debug_file, "w") as f:
        f.write("Starting test application...\n")
    
    # Test basic imports
    import customtkinter as ctk
    with open(debug_file, "a") as f:
        f.write("CustomTkinter imported successfully\n")
    
    # Test basic window creation
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    
    with open(debug_file, "a") as f:
        f.write("CustomTkinter configured\n")
    
    # Create minimal window
    class TestApp(ctk.CTk):
        def __init__(self):
            super().__init__()
            with open(debug_file, "a") as f:
                f.write("CTk.__init__ called\n")
            self.title("Test")
            with open(debug_file, "a") as f:
                f.write("Title set\n")
    
    with open(debug_file, "a") as f:
        f.write("Creating TestApp...\n")
    
    app = TestApp()
    
    with open(debug_file, "a") as f:
        f.write("TestApp created successfully\n")
    
    app.mainloop()
    
except Exception as e:
    with open(debug_file, "a") as f:
        f.write(f"Error: {str(e)}\n")
        import traceback
        f.write(traceback.format_exc())
