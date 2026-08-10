# auagcu2020@auagcu2020-FMVA50B3W2:~$ ollama run llama3.2
# >>> PythonのTkinterを使って電卓アプリを作成してください。
import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculator")

        # Entry field for display
        self.entry_field = tk.Entry(self.window, width=35, borderwidth=5)
        self.entry_field.grid(row=0, column=0, columnspan=4)

        # Number buttons
        self.button_7 = tk.Button(self.window, text="7", padx=40, pady=20, command=lambda: self.append_to_entry("7"))
        self.button_8 = tk.Button(self.window, text="8", padx=40, pady=20, command=lambda: self.append_to_entry("8"))
        self.button_9 = tk.Button(self.window, text="9", padx=40, pady=20, command=lambda: self.append_to_entry("9"))
        self.button_divide = tk.Button(self.window, text="/", padx=40, pady=20, command=lambda: self.append_to_entry("/"))

        self.button_4 = tk.Button(self.window, text="4", padx=40, pady=20, command=lambda: self.append_to_entry("4"))
        self.button_5 = tk.Button(self.window, text="5", padx=40, pady=20, command=lambda: self.append_to_entry("5"))
        self.button_6 = tk.Button(self.window, text="6", padx=40, pady=20, command=lambda: self.append_to_entry("6"))
        self.button_multiply = tk.Button(self.window, text="*", padx=40, pady=20, command=lambda: self.append_to_entry("*"))

        self.button_1 = tk.Button(self.window, text="1", padx=40, pady=20, command=lambda: self.append_to_entry("1"))
        self.button_2 = tk.Button(self.window, text="2", padx=40, pady=20, command=lambda: self.append_to_entry("2"))
        self.button_3 = tk.Button(self.window, text="3", padx=40, pady=20, command=lambda: self.append_to_entry("3"))
        self.button_subtract = tk.Button(self.window, text="-", padx=41, pady=20, command=lambda: self.append_to_entry("-"))

        self.button_0 = tk.Button(self.window, text="0", padx=40, pady=20, command=lambda: self.append_to_entry("0"))
        self.button_decimal = tk.Button(self.window, text=".", padx=40, pady=20, command=lambda: self.append_to_entry("."))
        self.button_equals = tk.Button(self.window, text="=", padx=91, pady=20, command=self.calculate)
        self.button_add = tk.Button(self.window, text="+", padx=40, pady=20, command=lambda: self.append_to_entry("+"))

        # Button frame
        button_frame = tk.Frame(self.window)
        button_frame.grid(row=4, column=0, columnspan=4)

        # Button widgets
        self.button_7.grid(row=1, column=0)
        self.button_8.grid(row=1, column=1)
        self.button_9.grid(row=1, column=2)
        self.button_divide.grid(row=1, column=3)

        self.button_4.grid(row=2, column=0)
        self.button_5.grid(row=2, column=1)
        self.button_6.grid(row=2, column=2)
        self.button_multiply.grid(row=2, column=3)

        self.button_1.grid(row=3, column=0)
        self.button_2.grid(row=3, column=1)
        self.button_3.grid(row=3, column=2)
        self.button_subtract.grid(row=3, column=3)

        self.button_0.grid(row=4, column=0)
        self.button_decimal.grid(row=4, column=1)
        self.button_equals.grid(row=4, column=2, columnspan=2)
        self.button_add.grid(row=4, column=3)

        # Clear button
        self.button_clear = tk.Button(self.window, text="Clear", padx=79, pady=20, command=self.clear)
        self.button_clear.grid(row=5, column=0, columnspan=4)

    def append_to_entry(self, value):
        current_value = self.entry_field.get()
        new_value = current_value + value
        self.entry_field.delete(0, tk.END)
        self.entry_field.insert(tk.END, new_value)

    def calculate(self):
        try:
            result = eval(self.entry_field.get())
            self.entry_field.delete(0, tk.END)
            self.entry_field.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def clear(self):
        self.entry_field.delete(0, tk.END)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()

# >>> 

