from tkinter import *
import random
screen = Tk()
screen.geometry('640x480')

score = 0

lbl = Label(screen, text = "are you ready?")
lbl.place(x=300, y=10)

def move():
    global score
    a = random.randint(1, 600)
    b = random.randint(1,600)
    btn.place(x=a, y=b)
    score = score + 1
    lbl2.configure(text="Score: "+ str(score))

btn = Button(screen, text="press me", command = move)
btn.place(x=400,y=50)

lbl2 = Label(screen, text = "Score: " )
lbl2.place(x=300, y=30)









screen.mainloop()