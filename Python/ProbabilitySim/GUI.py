from tkinter import *
import subprocess

# 1 2 15000
def cpp_open(fp,args):
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    p = subprocess.Popen(fp+args, startupinfo=startupinfo,stdout=subprocess.PIPE)
    stdout, stderr = p.communicate()
    return stdout.split()[1].decode()

class CFMenu:
    def __init__(self,master):
        frame = Frame(master)
        self.question = Label(frame, text="What is the number?")
        self.entry = Entry(frame, justify=CENTER)
        self.entry.bind("<Return>",self.calc)
        self.button = Button(frame, text="Flip", command=self.calc)
        self.result = Listbox(frame,height=1)
        
        frame.pack(fill=BOTH,expand=True)
        self.question.pack(fill=X,expand=False)
        self.entry.pack(fill=X,expand=False)
        self.button.pack(fill=BOTH,expand=False)
        self.result.pack(side=LEFT,fill=BOTH,expand=True)
        
    def calc(self, a=1, b=1, c=1):
        a,b,c=1,2,10000
        self.result.delete(0,END)
            

class rootMenu:
    def __init__(self,master):
        self.frame = Frame(master)
        self.title = Label(self.frame, text="StardustGogeta's\nProbability Simulators")
        self.CF = Button(self.frame, text="Coin Flip", command=lambda:window('Coin Flip', 'CF'))
        
        self.title.pack(fill=BOTH,expand=False)
        x = ["frame","CF"]
        for y in x:
            exec("self."+str(y)+".pack(fill=BOTH,expand=True)")

def window(x,y='root',self=0):
    exec("{1}=Tk()\n{1}.wm_title('{0}')\nmenu={1}Menu({1})\n{1}.mainloop()".format(x,y))

window('Main Menu')
