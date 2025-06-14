from tkinter import *
from tkinter.filedialog import askopenfilename

def open_archive(self):
    
    from functions.commands.set_path import set_path
    
    self.path_open = askopenfilename(defaultextension=".py", filetypes=[("Python Files", "*.py")])
    with open(self.path_open, "r", encoding="utf-8") as open_content:
        self.content_archive = open_content.read()
        self.frame_code.delete("1.0", END)
        self.frame_code.insert("1.0", self.content_archive)
        set_path(self, self.path_open)