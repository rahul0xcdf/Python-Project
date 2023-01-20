from tkinter import *
import Transproj
root =Tk()

root.title("Transaltor")
root.geometry("1080x400")

label1=Label(root,text="LANGUAGE TRANSLATOR", font="segoe 30 bold", bg="white", width=18,bd=5,relief=GROOVE)
label1.pack()


def trans():
    Transproj.main()
    
    
b1=Button(root, text="Open translator", bd=6, bg="red", command=trans)
b1.pack()


root.mainloop()