import tkinter
from tkinter import *

title = 'Calculator'
lbltext = str()
colour = 'white'
keys = [1, 2, 3, '=', 'CE', 4, 5, 6, '+', '(', 7, 8, 9, '-', ')', 0, '.0', '.00', '*', '[', '.', '%', '^', '/', ']']
condition = True
valuefunction = '1'
count = 0

def onclick(st):
    global lbltext
    lbltext = lbltext + st
    equation.set(lbltext)
    return

def result():    
	try: 
		global lbltext
		total = str(eval(lbltext)) 
		equation.set(total) 
		lbltext = total

	except: 
		equation.set('Error') 
		lbltext = ''

def onclear():
    global lbltext
    lbltext = str()
    equation.set(str())
    return

def frame():
    btnrow1 = Frame(root, bg = colour)
    btnrow1.pack(expand = True, fill = 'both')
    return

def binlabel():
    lbl = Label(
        root,
        text = 'Simple Calculator',
        anchor = NE,
        font = ('Verdana', 8),
        bg = colour,
        fg = '#999', 
    )
    lbl.pack(expand = True, fill = 'both')
    return

def label():
    lbl = Label(
        root,
        text = lbltext,
        anchor = SE,
        font = ('Verdana', 18),
        bg = colour,
        fg = '#999',
        textvariable = equation,
    )
    lbl.pack(expand = True, fill = 'both')
    return

def button():
    for i in keys:
        if (i == 'CE'):
            function = onclear
        elif (i == '='):
            function =result
        else:
            function = lambda: onclick(str(i))
        btn = Button(
            btnrow1,
            text= i,
            font = ('Verdana', 16),
            relief = GROOVE,
            width = 1,
            border = 1,
            bg = '#333',
            fg = '#f3f3f3',
            command = function,
        )
        btn.pack(side= LEFT, expand = condition, fill = 'both')
        keys.pop(0)
        break
    return

root = tkinter.Tk()
root.geometry('250x400')
root.resizable(0, 0)
root.title(title)

equation = StringVar()

binlabel()
label()

btnrow1 = Frame(
    root,
    bg = 'blue',
    height = 3,
    )
btnrow1.pack(expand = False, fill = 'both')

for i in range(1, 6):
    btnrow1 = Frame(root, bg = colour)
    btnrow1.pack(expand = True, fill = 'both')
    for i in range(1, 6):
        button()

btnrow1 = Frame(
    root,
    bg = 'blue',
    height = 3,
    )
btnrow1.pack(expand = False, fill = 'both')

root.mainloop()
