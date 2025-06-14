from tkinter import *
from tkinter.filedialog import asksaveasfilename

def save_archive(self):
    
    from functions.commands.set_path import set_path
    
    if self.file_path == "":
        self.new_archive = asksaveasfilename(defaultextension=".py", filetypes=[("Python Files", "*.py")])
        with open(self.new_archive, "w", encoding="utf-8") as save_content:
            self.content = self.frame_code.get("1.0", END)
            save_content.write(f"{self.content}")
            set_path(self, self.new_archive)            
    else:
        with open(self.file_path, "w", encoding="utf-8") as save_content:
            self.content = self.frame_code.get("1.0", END)
            save_content.write(f"{self.content}")
