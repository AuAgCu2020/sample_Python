import tkinter as tk
import math
import time


class AnalogClock:
    def __init__(self, root):
        self.root = root

        # フルスクリーン
        self.root.attributes("-fullscreen", True)

        # 背景色
        self.root.configure(bg="black")

        # Canvas
        self.canvas = tk.Canvas(
            root,
            bg="black",
            highlightthickness=0
        )
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Escで終了
        self.root.bind("<Escape>", self.close)

        # クリックでも終了
        self.root.bind("<Button-1>", self.close)

        self.update_clock()

    def update_clock(self):
        # 現在時刻
        now = time.localtime()

        hour = now.tm_hour % 12
        minute = now.tm_min
        second = now.tm_sec

        # 画面サイズ
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        # 時計の中心と半径
        cx = width / 2
        cy = height / 2
        radius = min(width, height) * 0.42

        # 一度消去
        self.canvas.delete("all")

        # 時計の外周
        self.canvas.create_oval(
            cx - radius,
            cy - radius,
            cx + radius,
            cy + radius,
            outline="white",
            width=5
        )

        # 目盛り
        for i in range(60):
            angle = math.radians(i * 6 - 90)

            if i % 5 == 0:
                outer = radius * 0.96
                inner = radius * 0.88
                line_width = 6
            else:
                outer = radius * 0.96
                inner = radius * 0.92
                line_width = 2

            x1 = cx + math.cos(angle) * inner
            y1 = cy + math.sin(angle) * inner
            x2 = cx + math.cos(angle) * outer
            y2 = cy + math.sin(angle) * outer

            self.canvas.create_line(
                x1, y1, x2, y2,
                fill="white",
                width=line_width
            )

        # 数字
        for number in range(1, 13):
            angle = math.radians(number * 30 - 90)

            x = cx + math.cos(angle) * radius * 0.78
            y = cy + math.sin(angle) * radius * 0.78

            self.canvas.create_text(
                x, y,
                text=str(number),
                fill="white",
                font=("Arial", int(radius * 0.10), "bold")
            )

        # 時針
        hour_angle = math.radians(
            (hour + minute / 60) * 30 - 90
        )

        self.draw_hand(
            hour_angle,
            radius * 0.50,
            12,
            "white"
        )

        # 分針
        minute_angle = math.radians(
            (minute + second / 60) * 6 - 90
        )

        self.draw_hand(
            minute_angle,
            radius * 0.70,
            8,
            "white"
        )

        # 秒針
        second_angle = math.radians(
            second * 6 - 90
        )

        self.draw_hand(
            second_angle,
            radius * 0.78,
            3,
            "red"
        )

        # 中心
        self.canvas.create_oval(
            cx - 10,
            cy - 10,
            cx + 10,
            cy + 10,
            fill="white",
            outline="white"
        )

        # 1秒後に再描画
        self.root.after(1000, self.update_clock)

    def draw_hand(self, angle, length, width, color):
        width_canvas = self.canvas.winfo_width()
        height_canvas = self.canvas.winfo_height()

        cx = width_canvas / 2
        cy = height_canvas / 2

        x = cx + math.cos(angle) * length
        y = cy + math.sin(angle) * length

        self.canvas.create_line(
            cx, cy,
            x, y,
            fill=color,
            width=width,
            capstyle=tk.ROUND
        )

    def close(self, event=None):
        self.root.destroy()


# メイン
root = tk.Tk()
clock = AnalogClock(root)
root.mainloop()
