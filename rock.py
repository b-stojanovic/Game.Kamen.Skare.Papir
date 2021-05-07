from tkinter import *
import random

#initialize window
root = Tk()
root.geometry('400x400')
root.resizable(0,0)
root.title('Kamen,škare,papir')
root.config(bg ='seashell3')

#heading
Label(root, text ='Kamen,škare,papir', font='arial 20 bold', bg = 'seashell2').pack()

#User Choice
user_take = StringVar()
Label(root, text ='Izaberi jednu opciju: kamen,skare,papir', font='arial 15 bold', bg = 'seashell2').place(x = 20,y=70)
Entry(root, font ='arial 15', textvariable = user_take, bg = 'antiquewhite2').place(x=90, y=130)

#computer choice
comp_pick = random.randint(1,3)
if comp_pick == 1:
    comp_pick = 'kamen'
elif comp_pick ==2:
    comp_pick = 'skare'
else:
    comp_pick = 'papir'

#Function to play
Result = StringVar()

def play():
    user_pick = user_take.get()
    if user_pick == comp_pick:
        Result.set('Rezultat je neriješen')
    elif user_pick == 'kamen' and comp_pick =='skare':
        Result.set('Pobijedio si! Kompjuter je izabrao skare!')
    elif user_pick == 'kamen' and comp_pick =='papir':
        Result.set('Pobijedio si! Kompjuter je izabrao papir!')
    elif user_pick == 'skare' and comp_pick == 'kamen':
        Result.set('Izgubio si! Kompjuter je izabrao kamen!')
    elif user_pick == 'skare' and comp_pick == 'papir':
        Result.set('Izgubio si! Kompjuter je izabrao papir!')
    elif user_pick == 'papir' and comp_pick == 'skare':
        Result.set('Izgubio si! Kompjuter je izabrao skare!')
    elif user_pick == 'papir' and comp_pick == 'kamen':
        Result.set('Izgubio si! Kompjuter je izabrao kamen!')
    else:
        Result.set('neispravno: izaberi jednu opciju: kamen, skare, papir')

#function to reset
def Reset():
    Result.set("")
    user_take.set("")

#function to exit
def Exit():
    root.destroy()

#buttons

Entry(root, font = 'arial 10 bold', textvariable = Result, bg ='antiquewhite2', width= 50,).place(x=25, y=250)
Button(root, font= 'arial 13 bold', text = 'Play', padx=5, bg = 'seashell4', command = play). place(x=150, y=190)
Button(root, font= 'arial 13 bold', text = 'Reset', padx=5, bg = 'seashell4', command = Reset).place(x=70, y=310)
Button(root, font= 'arial 13 bold', text = 'Exit', padx=5, bg = 'seashell4', command = Exit).place(x=230,y=310)
root.mainloop()

