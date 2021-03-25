from tkinter import *
import sys
import os



#import counting

root = Tk()
root.title('Blackjack')
root.geometry('800x400')

e = Entry(root, width=50)
e.insert(0, 'Enter the amount of money to be place')
e.pack()

#creating a lable widget
#myLabel1 = Label(root, text='Blackjack').grid(row=0, column=0)
#myLabel2 = Label(root, text='Blackjack counting cards').grid(row=1, column=0)

def myClick():
    os.system('python3 counting.py')
    myLabel = Label(root, text=e.get())
    myLabel.pack()

myButton = Button(root, text='Start', padx=100, command=myClick)
myButton.pack()


root.mainloop()

