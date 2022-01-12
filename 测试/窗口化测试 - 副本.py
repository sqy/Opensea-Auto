import tkinter as tk


# 第1步，实例化object，建立窗口window
window = tk.Tk()

# 第2步，给窗口的可视化起名字
window.title("Welcome to sqy'code ")

# 第3步，设定窗口的大小(长 * 宽)
window.geometry('520x900')

def func_add_number():
    pass

var_add_number = tk.StringVar()
var_add_number.set(1)
button_add_number = tk.Checkbutton(window, text='fuck', variable=var_add_number, onvalue=1, offvalue=0, command=func_add_number)
button_add_number.place(x=250, y=70)
#button_add_number.config(state="disabled")

window.mainloop()