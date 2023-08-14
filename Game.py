import tkinter
import random
from tkinter import *
lap_guess=random.randint(1,100)
def check():
    user_guess=int(txt_guess.get())
    if user_guess < lap_guess:
         msg="Higher!"
    elif user_guess > lap_guess:
         msg="Lower!"
    elif user_guess == lap_guess:
         msg="Congrats!You won!!"
    else:
         msg="Something went wrong"
    result["text"]=msg
    txt_guess.delete(0,100)
def reset():
    global lap_guess
    lap_guess=random.randint(1,100)
    result["text"]="Game reset!"
    txt_guess.delete(0,100)
n=Tk()
n.configure(bg="black")
n.title("Guessing Game")
n.geometry("300x200")
title=Label(n,text="Welcome to number guessing game!!",bg="orange")
title.pack()
result=Label(n,text="Good luck! Start your game enter number(1-100)",fg="white",bg="purple")
result.pack()
btn_check=Button(n,text="check",fg="white",width=10,height=2,bg="green",command=check)
btn_check.pack(side="left")
btn_reset=Button(n,text="reset",fg="white",width=10,height=2,bg="red",command=reset)
btn_reset.pack(side="right")
txt_guess=Entry(n,width=2)
txt_guess.pack()
n.mainloop()
