from ast import Expression
import tkinter as tk
import tkinter.messagebox as tkm

def click_number(event): # 練習3
    btn = event.widget
    num = btn["text"]
    #tkm.showinfo(f"{num}", f"{num}のボタンが押されました")
    if num == "=":
        click_equal()
    elif num == "del":
        click_clear()
    else:
        entry.insert(tk.END, num) # 練習5
def click_equal():
    y = str(eval(entry.get()))
    entry.delete(0, tk.END)
    entry.insert(0,y)

def click_clear():
    entry.delete(0, tk.END)
                    
root = tk.Tk() # 練習1
root.geometry("380x500")

entry = tk.Entry(root, width=10, font=(", 40"), justify="right") # 練習4
entry.grid(row=0, column=0, columnspan=3)

r, c = 1, 0 # r: 行を表す変数／c：列を表す変数
numbers = list(range(9, -1, -1)) # 数字だけのリスト
operators = ["+","-","*","/","=","del"] # 演算子だけのリスト
for i, num in enumerate(numbers+operators, 1):
    btn = tk.Button(root, text=f"{num}", font=("", 30), width=4, height=2)
    btn.bind("<1>", click_number)
    btn.grid(row=r, column=c)
    c += 1
    if i%4 == 0:
        r += 1
        c = 0

root.mainloop()