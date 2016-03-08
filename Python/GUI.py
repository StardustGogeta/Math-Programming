from tkinter import *
import FC4, FC5, BC, LIC, CA, TR, decimal

class FC4Menu:
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
            
class FC5Menu:
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
        decimal.getcontext().prec = 500
        e = decimal.Decimal(self.entry.get())
        numbers = FC5.convert(e)
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


class LICMenu:
    def __init__(self,master):
        self.frame = Frame(master)
        self.ask = Radiobutton(self.frame, text="Slope / Y-Intercept", value=1, command=self.ask, indicatoron=0)
        self.calc = Radiobutton(self.frame, text="Coordinates", value=2, command=self.calculate, indicatoron=0)

        self.frame.pack(fill=BOTH,expand=True)
        self.ask.pack(fill=BOTH,expand=True)
        self.calc.pack(fill=BOTH,expand=True)

    def ask(self):
        self.ask.destroy()
        self.calc.destroy()
        self.line1 = Label(self.frame, text="Line 1 - Slope")
        self.entry = Entry(self.frame, justify=CENTER)
        self.entry.bind("<Return>",self.calc1)
        self.line2 = Label(self.frame, text="Line 1 - Y-intercept")
        self.entry2 = Entry(self.frame, justify=CENTER)
        self.entry2.bind("<Return>",self.calc1)
        self.line3 = Label(self.frame, text="Line 2 - Slope")
        self.entry3 = Entry(self.frame, justify=CENTER)
        self.entry3.bind("<Return>",self.calc1)
        self.line4 = Label(self.frame, text="Line 2 - Y-intercept")
        self.entry4 = Entry(self.frame, justify=CENTER)
        self.entry4.bind("<Return>",self.calc1)
        self.button = Button(self.frame, text="Calculate", command=self.calc1)
        self.result = Listbox(self.frame, height=1)

        self.line1.pack(fill=BOTH,expand=True)
        self.entry.pack(fill=BOTH,expand=True)
        self.line2.pack(fill=BOTH,expand=True)
        self.entry2.pack(fill=BOTH,expand=True)
        self.line3.pack(fill=BOTH,expand=True)
        self.entry3.pack(fill=BOTH,expand=True)
        self.line4.pack(fill=BOTH,expand=True)
        self.entry4.pack(fill=BOTH,expand=True)
        self.button.pack(fill=BOTH,expand=True)
        self.result.pack(fill=BOTH,expand=True)
        
    def calculate(self):
        self.ask.destroy()
        self.calc.destroy()
        frame1 = Frame(self.frame)
        frame2 = Frame(self.frame)
        frame3 = Frame(self.frame)
        frame4 = Frame(self.frame)
        self.line1 = Label(self.frame, text="Line 1 - Pair 1")
        self.entry = Entry(frame1, justify=CENTER)
        self.entry.bind("<Return>",self.calc2)
        self.entry2 = Entry(frame1, justify=CENTER)
        self.entry2.bind("<Return>",self.calc2)
        self.line2 = Label(self.frame, text="Line 1 - Pair 2")
        self.entry3 = Entry(frame2, justify=CENTER)
        self.entry3.bind("<Return>",self.calc2)
        self.entry4 = Entry(frame2, justify=CENTER)
        self.entry4.bind("<Return>",self.calc2)
        self.line3 = Label(self.frame, text="Line 2 - Pair 1")
        self.entry5 = Entry(frame3, justify=CENTER)
        self.entry5.bind("<Return>",self.calc2)
        self.entry6 = Entry(frame3, justify=CENTER)
        self.entry6.bind("<Return>",self.calc2)
        self.line4 = Label(self.frame, text="Line 2 - Pair 2")
        self.entry7 = Entry(frame4, justify=CENTER)
        self.entry7.bind("<Return>",self.calc2)
        self.entry8 = Entry(frame4, justify=CENTER)
        self.entry8.bind("<Return>",self.calc2)
        self.button = Button(self.frame, text="Calculate", command=self.calc2)
        self.result = Listbox(self.frame, height=1)

        self.line1.pack(fill=BOTH,expand=True)
        frame1.pack(fill=BOTH,expand=True)
        self.entry.pack(fill=BOTH,side=LEFT,expand=True)
        self.entry2.pack(fill=BOTH,side=RIGHT,expand=True)
        self.line2.pack(fill=BOTH,expand=True)
        frame2.pack(fill=BOTH,expand=True)
        self.entry3.pack(fill=BOTH,side=LEFT,expand=True)
        self.entry4.pack(fill=BOTH,side=RIGHT,expand=True)
        self.line3.pack(fill=BOTH,expand=True)
        frame3.pack(fill=BOTH,expand=True)
        self.entry5.pack(fill=BOTH,side=LEFT,expand=True)
        self.entry6.pack(fill=BOTH,side=RIGHT,expand=True)
        self.line4.pack(fill=BOTH,expand=True)
        frame4.pack(fill=BOTH,expand=True)
        self.entry7.pack(fill=BOTH,side=LEFT,expand=True)
        self.entry8.pack(fill=BOTH,side=RIGHT,expand=True)
        self.button.pack(fill=BOTH,expand=True)
        self.result.pack(fill=BOTH,expand=True)
        
    def calc1(self, a=1, b=1, c=1, d=1):
        a = float(self.entry.get())
        b = float(self.entry2.get())
        c = float(self.entry3.get())
        d = float(self.entry4.get())
        final = LIC.convert(a,c,b,d)
        self.result.delete(0,END)
        self.result.insert(END,final)

    def calc2(self, a=1, b=1, c=1, d=1, e=1, f=1, g=1, h=1):
        a = float(self.entry.get())
        b = float(self.entry2.get())
        c = float(self.entry3.get())
        d = float(self.entry4.get())
        e = float(self.entry5.get())
        f = float(self.entry6.get())
        g = float(self.entry7.get())
        h = float(self.entry8.get())
        final = LIC.calcslope(a,b,c,d,e,f,g,h)
        self.result.delete(0,END)
        self.result.insert(END,final)

class CAMenu:
    def __init__(self,master):
        frame = Frame(master)
        self.question = Label(frame, text="Please state an angle.")
        self.entry = Entry(frame, justify=CENTER)
        self.entry.bind("<Return>",self.calc)
        self.button = Button(frame, text="Calculate", command=self.calc)
        self.result = Listbox(frame,height=1,width=40)
        
        frame.pack(fill=BOTH,expand=True)
        self.question.pack(fill=X,expand=False)
        self.entry.pack(fill=X,expand=False)
        self.button.pack(fill=BOTH,expand=False)
        self.result.pack(side=LEFT,fill=BOTH,expand=True)
        
    def calc(self, e=1):
        e = int(self.entry.get())
        self.result.delete(0,END)
        self.result.insert(END,CA.coterminal(e))

class TRMenu:
    def __init__(self,master):
        self.frame = Frame(master)
        frame1 = Frame(self.frame)
        self.t,t=0,0
        self.deg = Radiobutton(frame1, text="Degrees", indicatoron=0, variable=t, value=1, command=self.deg)
        self.rad = Radiobutton(frame1, text="Radians", indicatoron=0, variable=t, value=2, command=self.rad)
        self.question = Label(self.frame, text="Please state an angle.")
        self.entry = Entry(self.frame, justify=CENTER)
        self.entry.bind("<Return>",self.calc)
        self.button = Button(self.frame, text="Calculate", command=self.calc)
        self.result = Listbox(self.frame,height=6,width=15)
        
        self.frame.pack(side=TOP,fill=BOTH,expand=True)
        frame1.pack(side=TOP,fill=BOTH,expand=True)
        self.deg.pack(side=LEFT,fill=BOTH,expand=True)
        self.rad.pack(side=RIGHT,fill=BOTH,expand=True)
        self.question.pack(fill=X,expand=False)
        self.entry.pack(fill=X,expand=False)
        self.button.pack(fill=BOTH,expand=False)
        self.result.pack(fill=BOTH,expand=True)

    def deg(self):
        self.rad.config(state=ACTIVE)
        if self.t==2:
            self.question1.destroy()
            self.frame2.destroy()
            self.yes.destroy()
            self.no.destroy()
        self.t = 1

    def rad(self):
        self.t = 2
        self.rad.config(state=DISABLED)
        self.question1 = Label(self.frame, text="Is it in terms of pi?")
        self.frame2 = Frame(self.frame)
        y=0
        self.yes = Radiobutton(self.frame2, variable=y, command=self.y3, text="Yes", value=3)
        self.no = Radiobutton(self.frame2, variable=y, command=self.y4, text="No", value=4)

        self.question1.pack(fill=X,expand=False)
        self.frame2.pack(fill=BOTH,expand=True)
        self.yes.pack(side=LEFT,fill=BOTH,expand=True)
        self.no.pack(side=RIGHT,fill=BOTH,expand=True)

    def y3(self):
        self.y = 3

    def y4(self):
        self.y = 4
        
    def calc(self, t=1, e=1, y=1):
        t = self.t
        e = float(self.entry.get())
        if t==2:
            y = self.y
        self.result.delete(0,END)
        x = TR.trig(t,e,y)
        for a in x:
            self.result.insert(END,a)

class rootMenu:
    def __init__(self,master):
        self.frame = Frame(master)
        self.title = Label(self.frame, text="StardustGogeta's\nMath Tools")
        self.FC4 = Button(self.frame, text="Factor Calculator 4", command=lambda:window('Factor Calculator 4', 'FC4'))
        self.FC5 = Button(self.frame, text="Factor Calculator 5", command=lambda:window('Factor Calculator 5', 'FC5'))
        self.BC = Button(self.frame, text="Base Converter", command=lambda:window('Base Converter', 'BC'))
        self.LIC = Button(self.frame, text="Line Intercept Calculator", command=lambda:window('Line Intercept Calculator', 'LIC'))
        self.CA = Button(self.frame, text="Coterminal Angle Calculator", command=lambda:window('Coterminal Calculator', 'CA'))
        self.TR = Button(self.frame, text="Trigonometric Ratio Calculator", command=lambda:window('Trigonometric Ratio Calculator', 'TR'))

        self.title.pack(fill=BOTH,expand=False)
        x = ["frame","FC4","FC5","BC","LIC","CA","TR"]
        for y in x:
            exec("self."+str(y)+".pack(fill=BOTH,expand=True)")

def window(x,y,self=0):
    exec("{1}=Tk()\n{1}.wm_title('{0}')\nmenu={1}Menu({1})\n{1}.mainloop()".format(str(x),str(y)))

window('Selection Menu', 'root')
