# 以下は、PythonのTkinterを用いて作成するシンプルな電卓アプリのコードです。

# python
import tkinter as tk

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear():
    entry.delete(0, tk.END)

def append(text):
    entry.insert(tk.END, text)

root = tk.Tk()
root.title("電卓")

entry = tk.Entry(root, font=("Arial", 24), justify="right")
entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "C"
]

for i, btn in enumerate(buttons):
    row = i // 4
    col = i % 4
    if btn == "C":
        btn_widget = tk.Button(root, text=btn, font=("Arial", 18), command=clear)
    elif btn == "=":
        btn_widget = tk.Button(root, text=btn, font=("Arial", 18), command=calculate)
    else:
        btn_widget = tk.Button(root, text=btn, font=("Arial", 18), command=lambda t=btn: append(t))
    btn_widget.grid(row=row+1, column=col, sticky="nsew")

for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(5):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()

### 説明
#- `Entry` ウィジェットで入力と結果を表示します。
#- ボタンは `7`, `8`, `9`, `/` など、電卓の基本的な機能を実装しています。
#- `calculate()` は式を評価し、`clear()` は入力内容をクリアします。
#- `append()` は入力文字を追加します。
#- エラー処理も含まれており、無効な式の場合は「Error」と表示されます。
#
#このコードは、Tkinterを使って電卓アプリを構築する基本的な例です。必要に応じてデザインや機能をカスタマイズできます。

