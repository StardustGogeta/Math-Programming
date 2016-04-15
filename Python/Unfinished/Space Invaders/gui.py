from tkinter import *
import main

class rootMenu:
    def __init__(self):
        self.root = Tk()
        self.root.wm_title('root')
        self.frame = Frame(self.root)
        self.title = Label(self.frame, text="Space Invaders")
        self.start = Button(self.frame, text="Start Game", command=self.start)
        self.title.pack(fill=BOTH,expand=False)
        x = ["frame","start"]
        for y in x:
            exec("self."+str(y)+".pack(fill=BOTH,expand=True)")
        self.root.overrideredirect(True)
        self.root.mainloop()

    def start(self):
        self.root.destroy()
        main.begin()

menu = rootMenu()
