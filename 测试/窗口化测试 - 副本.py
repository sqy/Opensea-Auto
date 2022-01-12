import tkinter as tk

# 第1步，实例化object，建立窗口window
window = tk.Tk()

# 第2步，给窗口的可视化起名字
window.title("Welcome to sqy'code ")

# 第3步，设定窗口的大小(长 * 宽)
window.geometry('500x300')



def func_menu_chinese():
    langmenu.entryconfig(index='Chinese', label='中文')

def func_menu_english():
    langmenu.entryconfig(index='中文', label='Chinese')

# 第5步，创建菜单栏
menubar = tk.Menu(window)
# 创建一个Language菜单项
langmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='Language', menu=langmenu)
# 在File中加入New、Open、Save等小菜单，即我们平时看到的下拉菜单，每一个小菜单对应命令操作。
#var1 = tk.StringVar()
#var1.set('Chinese')
langmenu.add_command(label='Chinese', command=func_menu_chinese)
langmenu.add_command(label='English', command=func_menu_english)
window.config(menu=menubar)
# 可选操作
#l = tk.Label(window, text='      ', bg='green')
#l.pack()

window.mainloop()