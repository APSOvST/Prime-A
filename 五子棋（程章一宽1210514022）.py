import tkinter as tk
from tkinter import messagebox
class GomokuGame:
    def __init__(self, master):
        self.master = master
        self.master.title("五子棋")
        self.canvas = tk.Canvas(master, width=450, height=450, bg='light gray')
        self.canvas.pack()
        self.board = [[0 for _ in range(15)] for _ in range(15)]
        self.current_player = 1  # 1 for black, -1 for white
        self.record = []
        self.draw_grid()
        self.canvas.bind("<Button-1>", self.callback1)
        self.canvas.bind("<Button-3>", self.callback2)
    def draw_grid(self):
        for i in range(15):
            x0, y0, x1, y1 = i * 30 + 15, 0, i * 30 + 15, 450
            self.canvas.create_line(x0, y0, x1, y1)
            self.canvas.create_line(y0, x0, y1, x1)
    def callback1(self, event):
        if self.place_stone(event, 1):
            self.check_winner()
    def callback2(self, event):
        if self.place_stone(event, -1):
            self.check_winner()
    def place_stone(self, event, player):
        x, y = event.x // 30, event.y // 30
        if 0 <= x < 15 and 0 <= y < 15 and self.board[y][x] == 0:
            self.board[y][x] = player
            color = 'black' if player == 1 else 'white'
            self.canvas.create_oval(x * 30 + 5, y * 30 + 5, x * 30 + 25, y * 30 + 25, fill=color)
            self.record.append((x, y))
            self.current_player *= -1
            return True
        return False
    def check_winner(self):
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for x, y in self.record:
            for dx, dy in directions:
                count = 1
                for i in range(1, 5):
                    nx, ny = x + dx * i, y + dy * i
                    if 0 <= nx < 15 and 0 <= ny < 15 and self.board[ny][nx] == self.board[y][x]:
                        count += 1
                    else:
                        break
                for i in range(1, 5):
                    nx, ny = x - dx * i, y - dy * i
                    if 0 <= nx < 15 and 0 <= ny < 15 and self.board[ny][nx] == self.board[y][x]:
                        count += 1
                    else:
                        break
                if count >= 5:
                    winner = "Black" if self.board[y][x] == 1 else "White"
                    messagebox.showinfo("Game Over", f"{winner} wins!")
                    self.master.quit()
                    return
if __name__ == "__main__":
    root = tk.Tk()
    game = GomokuGame(root)
root.mainloop()