from tkinter import *
import Trans
#from PIL import Image, ImageTk
root =Tk()

root.title("Transaltor")
root.geometry("1080x400")

canvas = Canvas(root, width=1080, height=400)
canvas.pack()

//
img=PhotoImage(file="Background.png")
canvas.create_image(0, 0, image=img, anchor='nw')


def trans():
    Trans.main()
    
    
b1=Button(root, text="Open translator", bd=20, bg="red", command=trans)
canvas.create_window(540,300,window=b1)


root.mainloop()
