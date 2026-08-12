'''
>>> PythonのTkinterを使って電卓アプリを作成してください。
Thinking...
考え...

Okay, the user wants me to create a calculator app using Python's Tkinter. Let me start by recalling how Tkinter 
works. Tkinter is Python's standard GUI library, so I'll need to import tkinter and create a main window.
さて、ユーザーからPythonのTkinterを使って電卓アプリを作成してほしいという依頼がありました。
まずはTkinterの仕組みを復習しましょう。
TkinterはPythonの標準GUIライブラリなので、まずはtkinterをインポートしてメインウィンドウを作成する必要があります。

First, I'll set up the main window with a title and maybe a size. Then, I need to create the display area where the 
input and results will be shown. A label or an entry widget would work here. The entry should be read-only so users 
can't edit it directly.
まず、メインウィンドウにタイトルとサイズを設定します。次に、入力内容と結果を表示する表示領域を作成する必要があります。
ラベルまたは入力ウィジェットが適しています。入力内容は読み取り専用とし、ユーザーが直接編集できないようにします。

Next, the buttons. The calculator typically has digits 0-9, operators like +, -, *, /, and functions like equals, 
clear, and maybe a delete button. I'll need to arrange these buttons in a grid layout. Each button will have a 
command that's a function I define.
次に、ボタンです。電卓には通常、0～9の数字、+、-、*、/などの演算子、イコール、クリアなどの関数、そして場合によっては削除ボタンがあります。
これらのボタンをグリッド状に配置する必要があります。各ボタンには、私が定義する関数であるコマンドが割り当てられます。

For the logic, when a button is pressed, it should append the corresponding value to the entry. The equals button 
will evaluate the expression. But I have to be careful with the evaluation to avoid errors, maybe using try-except 
blocks.
ロジックとしては、ボタンが押されたら、対応する値をエントリに追加する必要があります。
イコールボタンは式を評価しますが、エラーを避けるために評価には注意が必要で、try-exceptブロックを使う必要があるかもしれません。

The clear button will reset the entry. The delete button can remove the last character. Also, handling the decimal 
point to prevent multiple dots in a number.
クリアボタンで入力内容をリセットできます。削除ボタンで最後の文字を削除できます。また、小数点処理で数字に複数の小数点が入らないようにすることもできます。

Wait, I should make sure that the entry widget is properly updated. Maybe use the config method to set the text. 
Also, the grid layout needs to be structured so that buttons are in the right positions, like 0-9 in the first four 
rows, and the operators in the fifth row.
待って、入力ウィジェットが正しく更新されているか確認しないと。設定メソッドを使ってテキストを設定するのがいいかもしれない。
それから、グリッドレイアウトも、ボタンが正しい位置に配置されるようにする必要がある。例えば、最初の4行に0～9、5行目に演算子を配置するなど。

Testing the code is important. I'll need to handle cases where the user might input invalid expressions, like 
dividing by zero. But maybe for simplicity, just let it raise an error and catch it to display a message.
コードのテストは重要です。ユーザーがゼロ除算のような無効な式を入力した場合にも対応する必要があります。
しかし、簡略化のために、エラーを発生させてそれをキャッチし、メッセージを表示するだけでも良いかもしれません。

Putting it all together: create the window, entry widget, buttons, and their respective functions. Then, pack or 
grid them appropriately. Let me draft the code step by step, making sure each part is correctly implemented.
すべてをまとめると、ウィンドウ、エントリウィジェット、ボタン、そしてそれぞれの機能を作成します。
次に、それらを適切に配置またはグリッド化します。各部分が正しく実装されていることを確認しながら、コードを段階的に作成していきます。

...done thinking.
考えるのはもう終わりだ。
'''

import tkinter as tk
# 等号を押したときの処理
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
# 清浄
def clear():
    entry.delete(0, tk.END)
# 表示に文字を追加
def append(text):
    entry.insert(tk.END, text)
# Tkinterの初期化
root = tk.Tk()
root.title("電卓")
# 表示用のラベル
entry = tk.Entry(root, font=("Arial", 24), justify="right")
entry.grid(row=0, column=0, columnspan=4, sticky="nsew")
# ボタンの配置
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "C"
]
# ボタンを配置
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
# ウインドウのサイズを動的に調整
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(5):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()
# 
### 説明
##1. **Tkinterの初期化**: `tk.Tk()`でウィンドウを作成し、タイトルを設定します。
##2. **表示領域**: `Entry`ウィジェットで入力と結果を表示します。
##3. **ボタンの配置**: 0-9、演算子（+、-、*、/）、等号（=）、クリア（C）を配置します。
##4. **機能**:
##   - `calculate()`: `eval()`で式を評価し、結果を表示。
##   - `clear()`: 入力領域をクリア。
##   - `append()`: ボタンの値を入力領域に追加。
##5. **エラー処理**: 無効な式（例: 0で割る）は`try-except`でキャッチし、エラーメッセージを表示。
##
##このコードは基本的な電卓機能を実装しており、カスタマイズ可能です。

