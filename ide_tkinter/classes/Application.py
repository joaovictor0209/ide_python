from tkinter import *

class Application:
    
    from functions.config_window import config_window
    from functions.create_frames import create_frames
    from functions.open_images import open_images
    from functions.create_buttons import create_buttons
    
    def __init__(self):
        self.window = Tk()
        self.file_path = ""
        self.path_archive = ""
        self.config_window()
        self.create_frames()
        self.open_images()
        self.create_buttons()
        self.window.mainloop()
    