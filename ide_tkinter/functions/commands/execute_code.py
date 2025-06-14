import subprocess
import sys
from tkinter import messagebox
from tkinter import *

def execute_code(self):
    if self.file_path == "":
        messagebox.showwarning(
            "EXECUÇÃO INTERROMPIDA",
            "PARA EXECUTAR UM ARQUIVO É NECESSÁRIO ABRIR OU CRIAR UM NOVO!"
        )
        return

    self.locale_execute = f'"{sys.executable}" "{self.file_path}"'
    self.process = subprocess.Popen(self.locale_execute, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    self.result, self.error = self.process.communicate()

    self.output = ""
    
    if self.result:
        self.output += self.result.decode("utf-8")
    else:
        self.output += self.error.decode("utf-8")
        
    self.frame_terminal.configure(state="normal")
    self.frame_terminal.delete("1.0", END)
    self.frame_terminal.insert("1.0", self.output)
    self.frame_terminal.configure(state="disabled")