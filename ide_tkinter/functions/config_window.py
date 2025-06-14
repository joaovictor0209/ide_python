def config_window(self):
    
    from consts.const import PATH_ICONBITMAP
    
    self.window.geometry("1200x550")
    self.window.title("INTERFACE  DE  DESENVOLVIMENTO")
    self.window.iconbitmap(PATH_ICONBITMAP)
    self.window.maxsize(width=1200, height=500)
    self.window.minsize(width=1200, height=500)
    self.window.resizable(False, False)
    self.window.configure(background="#0b0b0b")