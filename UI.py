__author__ = 'User'
import tkinter

__author__ = 'User'
from tkinter import *
class Window(Frame):


    def __init__(self, master=None,):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def func1(self):
        print('hello1')

    def func2(self):
        print('hello2')

    def func3(self):
        print('hello3')

    #Creation of init_window
    def init_window(self):
        # Title
        self.master.title("Weather Forecast")

        v = StringVar()
        Label(self, text=" Input Current Date DD/MM/YY",textvariable=v, height=20,width=70,).grid(row=0)
        v.set("Hellwo")


        e1 = Entry(self)
        e1.grid(row=0, column=1)
        e1.place(x=180,y=170)

        self.pack(fill=BOTH, expand=1)
        button1 = Button(self, command=self.func1, text="Predict Weather")
        button1.place(x=110, y=200)

        self.pack(fill=BOTH, expand=1)
        button2 = Button(self, command=self.func2,text="  In 24 Hours  ")
        button2.place(x=210, y=200)

        self.pack(fill=BOTH, expand=1)
        button3 = Button(self, command=self.func3,text="  In 7 Days   ")
        button3.place(x=300, y=200)

        w = Label(root, text="Hello Tkinter!")
        w.pack()
        w.place(x=210,y=250)

root = tkinter.Tk()
#size of the window
root.geometry("500x500")
app = Window(root)
root.mainloop()