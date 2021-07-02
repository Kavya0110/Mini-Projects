from tkinter import TK

import tkinter
from tkinter import *
import random

top = Tk()
top.geometry('500x400+10+0')


def window1():
    new_window = Toplevel()
    new_window.geometry('500x400+10+0')

    ask_ques = Label(new_window, text="What do you want to ask Magic 8ball", fg="#333b47", font=("Comic Sans MS", 15, "bold")).place(x=60, y=100)
    ques= Entry(new_window).place(x=170, y=150, width=150)
    submit_ques = Button(new_window, text="Ask", command=window2, bg="#333b47", fg="white", width=10, font=("Comic Sans MS", 8)).place(x=200, y=180)

def window2():
    new_window2 = Toplevel()
    new_window2.geometry('500x400+10+0')
    random_ans = answers[random.randrange(len(answers))]
    ball_ans = Label(new_window2, text="Magic 8Ball's Answer Is: ", fg="#333b47", font=("Comic Sans MS", 20, "bold")).place(x=80, y=100)
    ball_ans1 = Label(new_window2, text=random_ans, fg="#333b47", font=("Comic Sans MS", 20, "bold")).place(x=150, y=140)
    play_again = Button(new_window2, text="Play Again!", command=window1, bg="#333b47", fg="white", width=10, font=("Comic Sans MS", 8)).place(x=200, y=200)
    quit_game = Button(new_window2, text="Quit Game", command=quit, bg="#333b47", fg="white", width=10, font=("Comic Sans MS", 8)).place(x=200, y=240)



welcome = Label(top, text="Welcome", fg="#333b47", font=("Comic Sans MS", 30, "bold")).place(x=160, y=30)
submit_name = Button(top, text="Let's Play!", bg="#333b47", fg="white", width=20, font=("Comic Sans MS", 8), command=window1).place(x=170, y=130)


answers = ["Certainly",
           "Definitely",
           "You may rely on it",
           "As I see it, Yes",
           "Most Likely",
           "Better not tell you now",
           "Very doubtful",
           "Outlook is not so good",
           "Probably not",
           "Signs point to yes",
           ]


top.mainloop()


















