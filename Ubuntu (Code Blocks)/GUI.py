from tkinter import *
import FC4

class FCMenu:
    def __init__(self,master):
        frame = Frame(master)
        self.question = Label(frame, text="What is the number?")
        self.entry = Entry(frame)
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

class Menu:
    def __init__(self,master):
        frame = Frame(master)
        self.title = Label(frame, text="StardustGogete's\nMath Tools")
        self.FC = Button(frame, text="Factor Calculator", command=self.FC)

        frame.pack(fill=BOTH,expand=True)
        self.title.pack(fill=BOTH,expand=False)
        self.FC.pack(fill=BOTH,expand=True)
    def FC(self):
        FCwindow = Tk()
        FCwindow.wm_title("Factor Calculator")
        menu=FCMenu(FCwindow)
        FCwindow.mainloop()

root = Tk()
root.wm_title("Selection Menu")
menu=Menu(root)
root.mainloop()
