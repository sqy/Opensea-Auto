import tkinter as tk
window = tk.Tk()
window.title('my window')
window.geometry('300x100')

l = tk.Label(window,
    text='OMG! this is TK!',    # 标签的文字
    bg='blue',     # 背景颜色
    font=('Arial', 12),     # 字体和字体大小
    width=15, height=2
    )  # 标签长宽
l.pack()    # 固定窗口位置

window.mainloop()