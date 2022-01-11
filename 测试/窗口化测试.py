import tkinter as tk

# 第1步，实例化object，建立窗口window
window = tk.Tk()

# 第2步，给窗口的可视化起名字
window.title("Welcome to sqy'code ")

# 第3步，设定窗口的大小(长 * 宽)
window.geometry('500x900')

# 第5步，浏览器相关信息
tk.Label(window, text='*', font=('Arial', 12)).place(x=10, y=200)
tk.Label(window, text='Chrome Profile path :', font=('Arial', 12)).place(x=20, y=200)
var_chrome_path = tk.StringVar()
entry_chrome_path = tk.Entry(window, textvariable=var_chrome_path, font=('Arial', 12)).place(x=10, y=230, width=430)

# 第6步，NFT相关信息
# 定义初始坐标
x0, y0 = 10, 350

# 收藏夹名称
tk.Label(window, text='*', font=('Arial', 12)).place(x=x0, y=y0)
tk.Label(window, text='Collection Name :', font=('Arial', 12)).place(x=x0+10, y=y0)
var_coll_name = tk.StringVar()
entry_coll_name = tk.Entry(window, textvariable=var_coll_name, font=('Arial', 12)).place(x=x0+150, y=y0, width=300)

# NFT名称
tk.Label(window, text='*', font=('Arial', 12)).place(x=x0, y=y0+40)
tk.Label(window, text='NFT Name :', font=('Arial', 12)).place(x=x0+10, y=y0+40)
var_nft_name = tk.StringVar()
entry_nft_name = tk.Entry(window, textvariable=var_nft_name, font=('Arial', 12)).place(x=x0+150, y=y0+40, width=300)

# NFT编号
tk.Label(window, text='NFT Number :', font=('Arial', 12)).place(x=x0+10, y=y0+80)
var_nft_number = tk.StringVar()
entry_nft_number = tk.Entry(window, textvariable=var_nft_number, font=('Arial', 12)).place(x=x0+150, y=y0+80, width=100)

# NFT价格
tk.Label(window, text='*', font=('Arial', 12)).place(x=x0, y=y0+120)
tk.Label(window, text='NFT Price(ETH) :', font=('Arial', 12)).place(x=x0+10, y=y0+120)
var_nft_price = tk.StringVar()
entry_nft_price = tk.Entry(window, textvariable=var_nft_price, font=('Arial', 12)).place(x=x0+150, y=y0+120, width=100)

# 可选操作

window.mainloop()