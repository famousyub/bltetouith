from tkinter import *
from tkinter import messagebox

def about():
    toplevel = Toplevel()
    toplevel.geometry("300x200")
    toplevel.title("About")
    toplevel.resizable(width=FALSE, height=False)
    label1 = Label(toplevel, font=("Maiandra GD", 14), text="\n\n           Temperature Converter")
    label2 = Label(toplevel, text="                 - Developed By D.Ashwin\n\n")

    label1.grid()
    label2.grid()

def cal():
    try:
        inputCelsius = float(TextBox1.get("1.0", "end-1c"))
        fahrenheit = (inputCelsius * 1.8) + 32
        TextBox2.insert(INSERT,fahrenheit)
    except:
        messagebox.showerror("Error","Please enter integer/float value")

def calF():
    try:
        inputFah = float(TextBox3.get("1.0", "end-1c"))
        Celsius = (inputFah - 32) * 5/9
        TextBox4.insert(INSERT,Celsius)
    except:
        messagebox.showerror("Error","Please enter integer/float value")

def clr():
    TextBox1.delete('1.0', END)
    TextBox2.delete('1.0', END)
    TextBox3.delete('1.0', END)
    TextBox4.delete('1.0', END)

root = Tk()
root.title("Temperature Converter")
root.geometry("400x500")
root.resizable(width=FALSE, height=False)
menubar = Menu(root)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)

label1 = Label(root, text="\nEnter Temperature in Celsius")
label1.grid(row=3, column=3)
TextBox1 = Text(root, height=2, width=7,font=(30))
TextBox1.grid(row=4, column=3, sticky=N)

b1 = Button(compound=LEFT, text="Submit", foreground="blue",command=cal)
b1.grid(row=5,column=3)
label2 = Label(root, text="\nTemperature in Fahrenheit")
label2.grid(row=6, column=3)
TextBox2 = Text(root, height=2, width=7,font=(30))
TextBox2.grid(row=7, column=3, sticky=N)

label3= Label(root,text="-------------------------------------")
label3.grid(row=8,column=3)

label1 = Label(root, text="\nEnter Temperature in Fahrenheit")
label1.grid(row=9, column=3)
TextBox3 = Text(root, height=2, width=7,font=(30))
TextBox3.grid(row=10, column=3, sticky=N)

b2 = Button(compound=LEFT, text="Submit", foreground="blue",command=calF)
b2.grid(row=11,column=3)
label4 = Label(root, text="\nTemperature in Celsius")
label4.grid(row=12, column=3)
TextBox4 = Text(root, height=2, width=7,font=(30))
TextBox4.grid(row=13, column=3, sticky=N)
label5 = Label(root, text="")
label5.grid(row=14, column=3)
b3 = Button(compound=LEFT, text="Clear TextBox", fg="white",height=2,width=12,background="black",borderwidth=2, relief="groove",command=clr)
b3.grid(row=15,column=3)



label2 = Label(root, font=("Maiandra GD", 28), text="Temperature Converter")
label2.grid(row=1, column=3)

root.mainloop()