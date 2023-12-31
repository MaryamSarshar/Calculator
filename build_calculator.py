from tkinter import *
root = Tk()
root.title("Cat Calculator")
root.iconbitmap("C:\\Users\\lenovo\\Desktop\\png_folder\\ph-ico.ico")
e = Entry(root,width=28,borderwidth=5,fg="black",bg="grey",font=1)
e.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

def button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number))

def button_clear():
    e.delete(0,END)

def button_add():
    first_num = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_num)
    e.delete(0,END)

def button_equal():
    second_num = e.get()
    e.delete(0,END)
    if math == "addition":
        e.insert(0,f_num + int(second_num))
    if math == "subtraction":
        e.insert(0,f_num - int(second_num))
    if math == "multiplication":
        e.insert(0,f_num * int(second_num))
    if math == "division":
        e.insert(0,f_num / int(second_num))

def button_subtract():
    first_num = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_num)
    e.delete(0,END)



def button_multiply():
    first_num = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_num)
    e.delete(0,END)


def button_divide():
    first_num = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_num)
    e.delete(0,END)


button_0 = Button(root,text="0",padx=30.1,pady=10,command=lambda: button_click(0),fg ="black",bg="yellow",font= 1)
button_1 = Button(root,text="1",padx=29.5,pady=10,command=lambda: button_click(1),fg ="black",bg="yellow",font= 1)
button_2 = Button(root,text="2",padx=30,pady=10,command=lambda: button_click(2),fg ="black",bg="yellow",font= 1)
button_3 = Button(root,text="3",padx=31.2,pady=10,command=lambda: button_click(3),fg ="black",bg="yellow",font= 1)
button_4 = Button(root,text="4",padx=30,pady=10,command=lambda: button_click(4),fg ="black",bg="yellow",font= 1)
button_5 = Button(root,text="5",padx=30,pady=10,command=lambda: button_click(5),fg ="black",bg="yellow",font= 1)
button_6 = Button(root,text="6",padx=31,pady=10,command=lambda: button_click(6),fg ="black",bg="yellow",font= 1)
button_7 = Button(root,text="7",padx=30,pady=10,command=lambda: button_click(7),fg ="black",bg="yellow",font= 1)
button_8 = Button(root,text="8",padx=30,pady=10,command=lambda: button_click(8),fg ="black",bg="yellow",font= 1)
button_9 = Button(root,text="9",padx=31,pady=10,command=lambda: button_click(9),fg ="black",bg="yellow",font= 1)
button_add =Button(root,text="+",padx=29.5,pady=10,command= button_add,fg="black",bg="grey",font= 1)
button_equal =Button(root,text="=",padx=29.4,pady=10,command= button_equal,fg="black",bg="green",font= 1)
button_clear =Button(root,text="Clear",padx=13,pady=10,command= button_clear,fg="black",bg="red",font= 1)

button_subtract =Button(root,text="-",padx=32.5,pady=10,command= button_subtract,fg="black",bg="grey",font= 1)
button_multiply =Button(root,text="*",padx=31.5,pady=10,command= button_multiply,fg="black",bg="grey",font= 1)
button_divide =Button(root,text="/",padx=32.5,pady=10,command= button_divide,fg="black",bg="grey",font= 1)

button_0.grid(row=4,column=1)
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_add.grid(row=4,column=3)
button_clear.grid(row=4,column=2)
button_equal.grid(row=4,column=0)
button_subtract.grid(row=3,column=3)
button_multiply.grid(row=2,column=3)
button_divide.grid(row=1,column=3)




root.mainloop()