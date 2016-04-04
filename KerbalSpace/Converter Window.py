from tkinter import *
import COMPILER as c, os
from subprocess import Popen

class rootMenu:
    def __init__(self,master):
        self.frame = Frame(master)
        self.load = Button(self.frame, text='Load File', command=self.loadFile)
        self.save = Button(self.frame, text='Save File', command=self.saveFile)
        self.submit = Button(self.frame, text='Compile Python\nto KerbalSpace', command=self.compiler)
        self.run = Button(self.frame, text='Run Output', command=self.run)
        for y in ["frame","load","save","submit","run"]:
            exec("self."+str(y)+".pack(fill=BOTH,expand=True)")
            
    def loadFile(self):
        self.lFile = filedialog.askopenfilename(filetypes=(("KerbalSpace files", "*.ks"),
                                                           ("All files", "*.*")))
    def saveFile(self):
        self.sFile = filedialog.asksaveasfilename(filetypes=(("Python files", "*.py"),
                                                           ("All files", "*.*")))
    def compiler(self):
        c.compiler(self.lFile,self.sFile)

    def run(self):
        bat = open('RUNTIME.bat','w')
        bat.write('python '+self.sFile+'\npause\n')
        bat.close()
        p = Popen("RUNTIME.bat")
        stdout, stderr = p.communicate()
        os.remove('RUNTIME.bat')

def window(x,y,self=0):
    exec("{1}=Tk()\n{1}.wm_title('{0}')\nmenu={1}Menu({1})\n{1}.mainloop()".format(str(x),str(y)))

window('Selection Menu', 'root')
