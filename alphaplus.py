import os
import ctypes
import shutil
from tkinter import Tk, filedialog, simpledialog

class AlphaPlus:
    def __init__(self):
        self.desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    
    def organize_icons(self):
        categories = simpledialog.askstring("Input", "Enter categories separated by commas (e.g., Work, Personal, Games):")
        if categories:
            categories = [category.strip() for category in categories.split(',')]
            for category in categories:
                category_path = os.path.join(self.desktop_path, category)
                if not os.path.exists(category_path):
                    os.makedirs(category_path)
            self.categorize_files(categories)
    
    def categorize_files(self, categories):
        for file in os.listdir(self.desktop_path):
            file_path = os.path.join(self.desktop_path, file)
            if os.path.isfile(file_path):
                category = simpledialog.askstring("Input", f"Enter a category for '{file}' (Available: {', '.join(categories)}):")
                if category in categories:
                    shutil.move(file_path, os.path.join(self.desktop_path, category))
    
    def set_icon_size(self, size):
        # Windows uses specific values for icon sizes: 0 (small), 1 (medium), 2 (large)
        size_map = {"small": 0, "medium": 1, "large": 2}
        if size in size_map:
            SPI_SETICONMETRICS = 0x002E
            icon_metrics = ctypes.windll.user32.SystemParametersInfoW(SPI_SETICONMETRICS, 0, size_map[size], 0)
            if icon_metrics:
                print(f"Icon size set to {size}")
            else:
                print("Failed to set icon size")
    
    def run(self):
        print("AlphaPlus: Organize and Customize Your Desktop Icons")
        root = Tk()
        root.withdraw()  # Hide the main window
        self.organize_icons()
        size = simpledialog.askstring("Input", "Enter preferred icon size (small, medium, large):")
        self.set_icon_size(size)
        print("Desktop customization complete.")

if __name__ == "__main__":
    app = AlphaPlus()
    app.run()