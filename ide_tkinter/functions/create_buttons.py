from tkinter import *

def create_buttons(self):
    
    from functions.open_images import open_images
    from functions.commands.close_app import close_app
    from functions.commands.open_archive import open_archive
    from functions.commands.save_archive import save_archive
    from functions.commands.execute_code import execute_code
    
    imgs_return = open_images(self)
    
    self.btn_open = Button(self.frame_left, image=imgs_return["img_open"], background="#070707", activebackground="#121212", bd=0, command=lambda:open_archive(self))
    self.btn_open.place(relx=0.26, rely=0.1)
    
    self.btn_save = Button(self.frame_left, image=imgs_return["img_save"], background="#070707", activebackground="#121212", bd=0, command=lambda:save_archive(self))
    self.btn_save.place(relx=0.26, rely=0.28)
    
    self.btn_run = Button(self.frame_left, image=imgs_return["img_run"], background="#070707", activebackground="#121212", bd=0, command=lambda:execute_code(self))
    self.btn_run.place(relx=0.26, rely=0.45)
    
    self.btn_exit = Button(self.frame_left, image=imgs_return["img_exit"], background="#070707", activebackground="#121212", bd=0, command=lambda:close_app(self))
    self.btn_exit.place(relx=0.26, rely=0.84)