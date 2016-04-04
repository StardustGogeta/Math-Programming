from tkinter import *
from tkinter import filedialog
import CPP_Compiler as cpp

class rootMenu:
    def __init__(self,master):
        self.frame = Frame(master)
        self.load = Button(self.frame, text='Load File', command=self.loadFile)
        self.save = Button(self.frame, text='Save File', command=self.saveFile)
        self.submit = Button(self.frame, text='Compile Python to C++', command=self.compiler)
        for y in ["frame","load","save","submit"]:
            exec("self."+str(y)+".pack(fill=BOTH,expand=True)")
            
    def loadFile(self):
        self.lFile = filedialog.askopenfilename(filetypes=(("Python files", "*.py"),
                                                           ("All files", "*.*")))
    def saveFile(self):
        self.sFile = filedialog.asksaveasfilename(filetypes=(("C++ files", "*.cpp"),
                                                           ("All files", "*.*")))
    def compiler(self):
        cpp.compiler(self.lFile,self.sFile)

def window(x,y,self=0):
    exec("{1}=Tk()\n{1}.wm_title('{0}')\nmenu={1}Menu({1})\n{1}.mainloop()".format(str(x),str(y)))

window('Selection Menu', 'root')
