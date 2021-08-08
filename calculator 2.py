from tkinter import *

ws = Tk()
ws.title('Calculator')
ws.geometry('250x400+500+100')
ws.resizable(0,0)

# global variables
num = ''

# functions
def display(number):
    global num 
    num = num + str(number)
    scr_lbl['text'] = num
    

def clear_scr():
    global num
    num = ''
    scr_lbl['text'] = num


def equal_btn():
     global num
     add=str(eval(num))
     scr_lbl['text'] = add
     num=''
def equal_btn():
     global num
     sub=str(eval(num))
     scr_lbl['text'] = sub
     num=''     
def equal_btn():
     global num
     mul=str(eval(num))
     scr_lbl['text'] = mul
     num=''
def equal_btn():
     global num
     div=str(eval(num))
     scr_lbl['text'] = div
     num=''    

var = StringVar()

# frames 
frame_1 = Frame(ws) 
frame_1.pack(expand=True, fill=BOTH)

frame_2 = Frame(ws)
frame_2.pack(expand=True, fill=BOTH)

frame_3 = Frame(ws)
frame_3.pack(expand=True, fill=BOTH)

frame_4 = Frame(ws)
frame_4.pack(expand=True, fill=BOTH)

# label
scr_lbl = Label(
    frame_1,
    textvariable='',
    font=('Arial', 20),
    anchor = SE,
    bg = '#595954',
    fg = 'white' 
    )

scr_lbl.pack(expand=True, fill=BOTH)

# buttons
key_1 = Button(
    frame_1,
    text='1',
    font=('Arial', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: display(1)
    )

key_1.pack(expand=True, fill=BOTH, side=LEFT)

key_2 = Button(
    frame_1,
    text='2',
    font=('Arial', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: display(2)
    )

key_2.pack(expand=True, fill=BOTH, side=LEFT)

key_3 = Button(
    frame_1,
    text='3',
    font=('Arial', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: display(3)
    )

key_3.pack(expand=True, fill=BOTH, side=LEFT)

key_add = Button(
    frame_1,
    text='+',
    font=('Arial', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: display('+')
    )

key_add.pack(expand=True, fill=BOTH, side=LEFT)

key_4 = Button(
    frame_2,
    text='4',
    font=('Arial', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: display(4)
    )

key_4.pack(expand=True, fill=BOTH, side=LEFT)

key_5 = Button(
    frame_2,
    text='5',
    font=('Arial', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: display(5)
    )

key_5.pack(expand=True, fill=BOTH, side=LEFT)

key_6 = Button(
    frame_2,
    text='6',
    font=('Arial', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: display(6)
    )

key_6.pack(expand=True, fill=BOTH, side=LEFT)

key_sub = Button(
    frame_2,
    text='-',
    font=('Arial', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: display('-')
    )

key_sub.pack(expand=True, fill=BOTH, side=LEFT)

key_7 = Button(
    frame_3,
    text='7',
    font=('Arial', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: display(7)
    )

key_7.pack(expand=True, fill=BOTH, side=LEFT)

key_8 = Button(
    frame_3,
    text='8',
    font=('Arial', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: display(8)
    )

key_8.pack(expand=True, fill=BOTH, side=LEFT)

key_9 = Button(
    frame_3,
    text='9',
    font=('Arial', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: display(9)
    )

key_9.pack(expand=True, fill=BOTH, side=LEFT)

key_mul = Button(
    frame_3,
    text='*',
    font=('Arial', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: display('*')
    )

key_mul.pack(expand=True, fill=BOTH, side=LEFT)


key_clr = Button(
    frame_4,
    text='C',
    font=('Arial', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = clear_scr 
    )

key_clr.pack(expand=True, fill=BOTH, side=LEFT)

key_0 = Button(
    frame_4,
    text='0',
    font=('Arial', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: display(0)
    )

key_0.pack(expand=True, fill=BOTH, side=LEFT)

key_res = Button(
    frame_4,
    text='=',
    font=('Arial', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = equal_btn
    )

key_res.pack(expand=True, fill=BOTH, side=LEFT)

key_div = Button(
    frame_4,
    text='/',
    font=('Arial', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: display('/')
    )

key_div.pack(expand=True, fill=BOTH, side=LEFT)

ws.mainloop()
