from tkinter import *
from PIL import Image, ImageTk

def open_images(self):
    
    from consts.const import PATH_IMG_OPEN_ARCHIVE
    from consts.const import PATH_IMG_SAVE_ARCHIVE
    from consts.const import PATH_IMG_RUN_CODE
    from consts.const import PATH_IMG_EXIT_PROGRAM
    
    self.img_open = Image.open(PATH_IMG_OPEN_ARCHIVE)
    self.img_open_resizable = self.img_open.resize((55,55))
    self.img_open = ImageTk.PhotoImage(self.img_open_resizable)
    
    self.img_save = Image.open(PATH_IMG_SAVE_ARCHIVE)
    self.img_save_resizable = self.img_save.resize((55,55))
    self.img_save = ImageTk.PhotoImage(self.img_save_resizable)
    
    self.img_run = Image.open(PATH_IMG_RUN_CODE)
    self.img_run_resizable = self.img_run.resize((55,55))
    self.img_run = ImageTk.PhotoImage(self.img_run_resizable)
    
    self.img_exit = Image.open(PATH_IMG_EXIT_PROGRAM)
    self.img_exit_resizable = self.img_exit.resize((55,55))
    self.img_exit = ImageTk.PhotoImage(self.img_exit_resizable)
    
    return {
        "img_open" : self.img_open,
        "img_save" : self.img_save,
        "img_run" : self.img_run,
        "img_exit" : self.img_exit
    }