from tkinter import *

root = Tk()
root.title("Kalkulator")
root.configure(bg="#909090")

root.resizable(False, False)

by_text = Label(root, text="by Harun", bg="#909090", font="Helvetica")
by_text.grid(row=0, column=3, columnspan=4)

e = Entry(root, width=20, borderwidth=4, relief="ridge", fg="black", bg="#9BE2FF")
e.grid(row=0, column=0, columnspan=2, pady=5)

def button_click(number):
	current = e.get()
	e.delete(0, END)
	e.insert(0, str(current) + str(number))

def button_clear():
	e.delete(0, END)

def button_add():
	first_number = e.get()
	global f_num
	global math
	math = "addition"
	f_num = int(first_number)
	e.delete(0, END)

def button_equal():
	second_number = e.get()
	e.delete(0, END)
	
	if math == "addition":
		e.insert(0, f_num + int(second_number))

	if math == "subtraction":
		e.insert(0, f_num - int(second_number))

	if math == "multiplication":
		e.insert(0, f_num * int(second_number))

	if math == "division":
		e.insert(0, f_num / int(second_number))

	

def button_subtract():
	first_number = e.get()
	global f_num
	global math
	math = "subtraction"
	f_num = int(first_number)
	e.delete(0, END)

def button_multiply():
	first_number = e.get()
	global f_num
	global math
	math = "multiplication"
	f_num = int(first_number)
	e.delete(0, END)

def button_divide():
	first_number = e.get()
	global f_num
	global math
	math = "division"
	f_num = int(first_number)
	e.delete(0, END)


button_1 = Button(root, text="1", bg="#9BE2FF", relief="ridge", padx=30, pady=15, command=lambda: button_click(1))
button_2 = Button(root, text="2", bg="#9BE2FF", relief="ridge", padx=30, pady=15, command=lambda: button_click(2))
button_3 = Button(root, text="3", bg="#9BE2FF", relief="ridge", padx=30, pady=15, command=lambda: button_click(3))
button_4 = Button(root, text="4", bg="#9BE2FF", relief="ridge", padx=30, pady=15, command=lambda: button_click(4))
button_5 = Button(root, text="5", bg="#9BE2FF", relief="ridge", padx=30, pady=15, command=lambda: button_click(5))
button_6 = Button(root, text="6", bg="#9BE2FF", relief="ridge", padx=30, pady=15, command=lambda: button_click(6))
button_7 = Button(root, text="7", bg="#9BE2FF", relief="ridge", padx=30, pady=15, command=lambda: button_click(7))
button_8 = Button(root, text="8", bg="#9BE2FF", relief="ridge", padx=30, pady=15, command=lambda: button_click(8))
button_9 = Button(root, text="9", bg="#9BE2FF", relief="ridge", padx=30, pady=15, command=lambda: button_click(9))
button_0 = Button(root, text="0", bg="#A8A8A8", relief="ridge", padx=30, pady=15, command=lambda: button_click(0))
button_add = Button(root, text="  + ", bg="#A8A8A8", relief="ridge", padx=23.5, pady=15, command=button_add)
button_equal = Button(root, text="=", bg="#A8A8A8", relief="ridge", padx=29, pady=15, command=button_equal)
button_clear = Button(root, text="Izbrisi", bg="#A8A8A8", relief="ridge", padx=18, pady=15, command=button_clear)

button_subtract = Button(root, text="-", bg="#A8A8A8", relief="ridge", padx=30, pady=15, command=button_subtract)
button_multiply = Button(root, text="*", bg="#A8A8A8", relief="ridge", padx=30, pady=15, command=button_multiply)
button_divide = Button(root, text="/", bg="#A8A8A8", relief="ridge", padx=30, pady=15, command=button_divide)

# Grid

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1)
button_add.grid(row=1, column=3)
button_equal.grid(row=4, column=2)

button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)

root.mainloop()
