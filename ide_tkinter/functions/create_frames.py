from tkinter import *

def create_frames(self):
    
    self.frame_left = Frame(self.window, background="#070707")
    self.frame_left.place(relx=0, rely=0, relwidth=0.1, relheight=1.0)
    
    self.frame_code = Text(self.window, background="#070707", foreground="#f8f8f8", font=("consolas", 10, "bold"))
    self.frame_code.place(relx=0.11, rely=0.02, relwidth=0.88, relheight=0.5)
    
    self.frame_terminal = Text(self.window, background="#070707", foreground="#f8f8f8", font=("consolas", 10, "bold"))
    self.frame_terminal.insert("1.0", ">> 💻 Área de saída — Aqui será exibido o resultado do código executado...")
    self.frame_terminal.configure(state="disabled")
    self.frame_terminal.place(relx=0.11, rely=0.54, relwidth=0.88, relheight=0.4)