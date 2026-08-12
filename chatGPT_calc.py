import tkinter as tk

# メインウィンドウ作成
root = tk.Tk()
root.title("電卓")
root.geometry("300x400")


# 入力欄
entry = tk.Entry(root, font=("Arial", 24), borderwidth=2, relief="ridge", justify="right")
entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

# ボタン押下時処理
def click_button(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(value))

# 計算処理
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# クリア処理
def clear():
    entry.delete(0, tk.END)

# ボタン配置
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

frame = tk.Frame(root)
frame.pack()

for row in buttons:
    row_frame = tk.Frame(frame)
    row_frame.pack(expand=True, fill="both")

    for btn in row:
        if btn == "=":
            command = calculate
        else:
            command = lambda x=btn: click_button(x)

        button = tk.Button(
            row_frame,
            text=btn,
            font=("Arial", 18),
            command=command
        )
        button.pack(side="left", expand=True, fill="both", padx=2, pady=2)

# クリアボタン
clear_button = tk.Button(
    root,
    text="C",
    font=("Arial", 18),
    command=clear
)
clear_button.pack(fill="both", padx=10, pady=10)

# 実行
root.mainloop()

