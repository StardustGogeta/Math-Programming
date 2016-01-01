from tkinter import *
import FC4
import BC

class FCMenu:
    def __init__(self,master):
        frame = Frame(master)
        self.question = Label(frame, text="What is the number?")
        self.entry = Entry(frame, justify=CENTER)
        self.entry.bind("<Return>",self.calc)
        self.button = Button(frame, text="Factorize", command=self.calc)
        self.scroll = Scrollbar(frame)
        self.result = Listbox(frame,height=12,width=30,selectmode=EXTENDED,yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.result.yview)
        
        frame.pack(fill=BOTH,expand=True)
        self.question.pack(fill=X,expand=False)
        self.entry.pack(fill=X,expand=False)
        self.button.pack(fill=BOTH,expand=False)
        self.scroll.pack(side=RIGHT,fill=Y,expand=False)
        self.result.pack(side=LEFT,fill=BOTH,expand=True)
        
    def calc(self, e=1):
        e = int(self.entry.get())
        numbers = FC4.convert(e)
        self.result.delete(0,END)
        for x in numbers:
            self.result.insert(END,x)

class BCMenu:
    def __init__(self,master):
        frame = Frame(master)
        frame1 = Frame(frame)
        frame2 = Frame(frame)
        frame3 = Frame(frame)
        self.question = Label(frame1, text="What is the number?")
        self.entry = Entry(frame1, justify=CENTER)
        self.entry.bind("<Return>",self.calc)
        self.question2 = Label(frame2, text="What is the first base?")
        self.entry2 = Entry(frame2, justify=CENTER)
        self.entry2.bind("<Return>",self.calc)
        self.question3 = Label(frame3, text="What is the second base?")
        self.entry3 = Entry(frame3, justify=CENTER)
        self.entry3.bind("<Return>",self.calc)
        self.button = Button(frame, text="Convert", command=self.calc)
        self.result = Listbox(frame, height=1)
        
        frame.pack(fill=BOTH,expand=True)
        frame1.pack(fill=BOTH,expand=True)
        frame2.pack(fill=BOTH,expand=True)
        frame3.pack(fill=BOTH,expand=True)
        self.question.pack(side=LEFT,fill=BOTH,expand=False)
        self.entry.pack(side=RIGHT,fill=BOTH,expand=False)
        self.question2.pack(side=LEFT,fill=BOTH,expand=False)
        self.entry2.pack(side=RIGHT,fill=BOTH,expand=False)
        self.question3.pack(side=LEFT,fill=BOTH,expand=False)
        self.entry3.pack(side=RIGHT,fill=BOTH,expand=False)
        self.button.pack(fill=BOTH,expand=True)
        self.result.pack(fill=BOTH,expand=True)
        
    def calc(self, a=1, b=1, c=1):
        a = int(self.entry.get())
        b = int(self.entry2.get())
        c = int(self.entry3.get())
        final = BC.convert(a,b,c)
        self.result.delete(0,END)
        self.result.insert(END,final)

class Menu:
    def __init__(self,master):
        frame = Frame(master)
        self.title = Label(frame, text="StardustGogete's\nMath Tools")
        self.FC = Button(frame, text="Factor Calculator", command=self.FC)
        self.BC = Button(frame, text="Base Converter", command=self.BC)

        frame.pack(fill=BOTH,expand=True)
        self.title.pack(fill=BOTH,expand=False)
        self.FC.pack(fill=BOTH,expand=True)
        self.BC.pack(fill=BOTH,expand=True)
        
    def FC(self):
        FCwindow = Tk()
        FCwindow.wm_title("Factor Calculator")
        menu=FCMenu(FCwindow)
        FCwindow.mainloop()

    def BC(self):
        BCwindow = Tk()
        BCwindow.wm_title("Base Converter")
        menu=BCMenu(BCwindow)
        BCwindow.mainloop()

root = Tk()
root.wm_title("Selection Menu")
menu=Menu(root)
root.mainloop()
