import tkinter as tk

# 第1步，实例化object，建立窗口window
window = tk.Tk()

# 第2步，给窗口的可视化起名字
window.title("Welcome to sqy'code ")
window.geometry('300x100')

l = tk.Label(window,
    text='OMG! this is TK!',    # 标签的文字
    bg='blue',     # 背景颜色
    font=('Arial', 12),     # 字体和字体大小
    width=15, height=2
    )  # 标签长宽
l.pack()    # 固定窗口位置

window.mainloop()