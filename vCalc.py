# ---------------------------------------------------
# Python Program to create a Calculator using Tkinter
# Author            : Vijnan Vijay K K
# Creation period   : July 2020
# ---------------------------------------------------

# To Import from tkinter module
from tkinter import *
from tkinter.font import Font

# To create a GUI window & to set the properties
window = Tk()
window.geometry('325x400')
window.title("Calculator")
window.iconbitmap('calc.ico')
window.resizable(0, 0)
window.config(background="#c4c9bf")

# Globally declared 2 variables
text_inp = StringVar()
txt_var = ""

# To set Font
myFont = Font(family="Seven Segment", size=26, weight="bold")
myFont1 = Font(family="Seven Segment", size=10, weight="bold")

# To create Entry/Display text
cal_text = Entry(window, textvariable=text_inp, font=myFont, justify="right", bd="5px",
                 disabledforeground="black", state=DISABLED)
cal_text.place(x=10, y=15, width=305, height=50)

# To create labels
lab_text1 = Label(window, text="§ Standard Calculator", font="Arial 10 italic", bg="#c4c9bf", fg="black")
lab_text1.place(x=10, y=70)

lab_text2 = Label(window, text="my®Calc", font="Courier 22 bold", bg="#c4c9bf", fg="#2f80ed")
lab_text2.place(x=170, y=95)

lab_text3 = Label(window, text="15 DIGIT", font=myFont1, bg="#c4c9bf", fg="black")
lab_text3.place(x=240, y=125)


# Function to update text in Entry box
def calc(num):
    global txt_var
    if num == ".":
        button_dot['state'] = DISABLED
        if txt_var == "":
            txt_var = "0"
    else:
        if txt_var == "0":
            txt_var = ""
        button_dot['state'] = NORMAL

    txt_var = txt_var + str(num)
    text_inp.set(txt_var)


# Function to Clear contents in Entry box
def cls():
    global txt_var
    txt_var = ""
    text_inp.set(txt_var)
    button_dot['state'] = NORMAL


# Function to Calculate
def cal_equal():
    global txt_var
    try:
        total = str(round(eval(txt_var), 2))
        text_inp.set(total)
        txt_var = total
    except:
        text_inp.set(" error ")
        txt_var = ""


# Clear Button row
button_clr = Button(window, text='CE', bd="4px", width="5", height="2", command=lambda: cls(),
                    font="Courier 12 bold", bg="#b3e6f9", fg="black")
button_clr.place(x=25, y=100)

# First row Buttons-> 7 8 9 /
button_7 = Button(window, text='7', bd="4px", width="5", height="2", command=lambda: calc(7),
                  font="Courier 12 bold", bg="grey", fg="white")
button_8 = Button(window, text='8', bd="4px", width="5", height="2", command=lambda: calc(8),
                  font="Courier 12 bold", bg="grey", fg="white")
button_9 = Button(window, text='9', bd="4px", width="5", height="2", command=lambda: calc(9),
                  font="Courier 12 bold", bg="grey", fg="white")
button_div = Button(window, text='÷', bd="4px", width="5", height="2", command=lambda: calc("/"),
                    font="Courier 12 bold")
orig_color = button_div.cget('background')

button_7.place(x=25, y=158)
button_8.place(x=95, y=158)
button_9.place(x=165, y=158)
button_div.place(x=235, y=158)

# Second row Buttons-> 4 5 6 *
button_4 = Button(window, text='4', bd="4px", width="5", height="2", command=lambda: calc(4),
                  font="Verdana 11 bold", bg="grey", fg="white")
button_5 = Button(window, text='5', bd="4px", width="5", height="2", command=lambda: calc(5),
                  font="Verdana 11 bold", bg="grey", fg="white")
button_6 = Button(window, text='6', bd="4px", width="5", height="2", command=lambda: calc(6),
                  font="Verdana 11 bold", bg="grey", fg="white")
button_mul = Button(window, text='x', bd="4px", width="5", height="2", command=lambda: calc('*'),
                    font="Verdana 11 bold")

button_4.place(x=25, y=216)
button_5.place(x=95, y=216)
button_6.place(x=165, y=216)
button_mul.place(x=235, y=216)

# Third row Buttons-> 1 2 3 -
button_1 = Button(window, text='1', bd="4px", width="5", height="2", command=lambda: calc(1),
                  font="Verdana 11 bold", bg="grey", fg="white")
button_2 = Button(window, text='2', bd="4px", width="5", height="2", command=lambda: calc(2),
                  font="Verdana 11 bold", bg="grey", fg="white")
button_3 = Button(window, text='3', bd="4px", width="5", height="2", command=lambda: calc(3),
                  font="Verdana 11 bold", bg="grey", fg="white")
button_sub = Button(window, text='—', bd="4px", width="5", height="2", command=lambda: calc('-'),
                    font="Verdana 11 bold")

button_1.place(x=25, y=274)
button_2.place(x=95, y=274)
button_3.place(x=165, y=274)
button_sub.place(x=235, y=274)

# Fourth row Buttons-> 0 . = +
button_0 = Button(window, text='0', bd="4px", width="5", height="2", command=lambda: calc(0),
                  font="Verdana 11 bold", bg="grey", fg="white")
button_dot = Button(window, text='•', bd="4px", width="5", height="2", command=lambda: calc('.'),
                    font="Verdana 11 bold", bg="grey", fg="white", disabledforeground="white")
button_equ = Button(window, text='=', bd="4px", width="5", height="2", command=lambda: cal_equal(),
                    font="Verdana 11 bold", bg="#f89a4d")
button_add = Button(window, text='+', bd="4px", width="5", height="2", command=lambda: calc('+'),
                    font="Verdana 11 bold")

button_0.place(x=25, y=332)
button_dot.place(x=95, y=332)
button_equ.place(x=165, y=332)
button_add.place(x=235, y=332)


# Functions for button hover effect / color change
def on_enter1(e):
    button_1['background'] = '#666666'


def on_leave1(e):
    button_1['background'] = 'grey'


def on_enter2(e):
    button_2['background'] = '#666666'


def on_leave2(e):
    button_2['background'] = 'grey'


def on_enter3(e):
    button_3['background'] = '#666666'


def on_leave3(e):
    button_3['background'] = 'grey'


def on_enter4(e):
    button_4['background'] = '#666666'


def on_leave4(e):
    button_4['background'] = 'grey'


def on_enter5(e):
    button_5['background'] = '#666666'


def on_leave5(e):
    button_5['background'] = 'grey'


def on_enter6(e):
    button_6['background'] = '#666666'


def on_leave6(e):
    button_6['background'] = 'grey'


def on_enter7(e):
    button_7['background'] = '#666666'


def on_leave7(e):
    button_7['background'] = 'grey'


def on_enter8(e):
    button_8['background'] = '#666666'


def on_leave8(e):
    button_8['background'] = 'grey'


def on_enter9(e):
    button_9['background'] = '#666666'


def on_leave9(e):
    button_9['background'] = 'grey'


def on_enter0(e):
    button_0['background'] = '#666666'


def on_leave0(e):
    button_0['background'] = 'grey'


def on_enter_dot(e):
    button_dot['background'] = '#666666'


def on_leave_dot(e):
    button_dot['background'] = 'grey'


def on_enter_div(e):
    button_div['background'] = '#d9d9d9'


def on_leave_div(e):
    button_div['background'] = orig_color


def on_enter_mul(e):
    button_mul['background'] = '#d9d9d9'


def on_leave_mul(e):
    button_mul['background'] = orig_color


def on_enter_sub(e):
    button_sub['background'] = '#d9d9d9'


def on_leave_sub(e):
    button_sub['background'] = orig_color


def on_enter_add(e):
    button_add['background'] = '#d9d9d9'


def on_leave_add(e):
    button_add['background'] = orig_color


def on_enter_clr(e):
    button_clr['background'] = '#0f8ebd'


def on_leave_clr(e):
    button_clr['background'] = '#b3e6f9'


def on_enter_equ(e):
    button_equ['background'] = '#cb5c01'


def on_leave_equ(e):
    button_equ['background'] = '#f67001'


button_1.bind("<Enter>", on_enter1)
button_1.bind("<Leave>", on_leave1)
button_2.bind("<Enter>", on_enter2)
button_2.bind("<Leave>", on_leave2)
button_3.bind("<Enter>", on_enter3)
button_3.bind("<Leave>", on_leave3)
button_4.bind("<Enter>", on_enter4)
button_4.bind("<Leave>", on_leave4)
button_5.bind("<Enter>", on_enter5)
button_5.bind("<Leave>", on_leave5)
button_6.bind("<Enter>", on_enter6)
button_6.bind("<Leave>", on_leave6)
button_7.bind("<Enter>", on_enter7)
button_7.bind("<Leave>", on_leave7)
button_8.bind("<Enter>", on_enter8)
button_8.bind("<Leave>", on_leave8)
button_9.bind("<Enter>", on_enter9)
button_9.bind("<Leave>", on_leave9)
button_0.bind("<Enter>", on_enter0)
button_0.bind("<Leave>", on_leave0)
button_dot.bind("<Enter>", on_enter_dot)
button_dot.bind("<Leave>", on_leave_dot)
button_div.bind("<Enter>", on_enter_div)
button_div.bind("<Leave>", on_leave_div)
button_mul.bind("<Enter>", on_enter_mul)
button_mul.bind("<Leave>", on_leave_mul)
button_sub.bind("<Enter>", on_enter_sub)
button_sub.bind("<Leave>", on_leave_sub)
button_add.bind("<Enter>", on_enter_add)
button_add.bind("<Leave>", on_leave_add)
button_clr.bind("<Enter>", on_enter_clr)
button_clr.bind("<Leave>", on_leave_clr)
button_equ.bind("<Enter>", on_enter_equ)
button_equ.bind("<Leave>", on_leave_equ)

window.mainloop()
