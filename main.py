import tkinter as tk
from tkinter import messagebox
import random

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")

        self.menu = tk.Menu(root)
        self.root.config(menu=self.menu)

        self.mode_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Game Mode", menu=self.mode_menu)
        self.mode_menu.add_command(label="Single Player", command=lambda: self.start_game(single_player=True))
        self.mode_menu.add_command(label="Two Players", command=lambda: self.start_game(single_player=False))
        self.mode_menu.add_separator()
        self.mode_menu.add_command(label="Quit", command=root.destroy)

    def start_game(self, single_player):
        self.game_frame = tk.Toplevel(self.root)
        self.game = TicTacToeGame(self.game_frame, single_player)

class TicTacToeGame:
    def __init__(self, frame, single_player):
        self.frame = frame
        self.single_player = single_player
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]

        self.buttons = [[None] * 3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(
                    frame, text="", font=("Helvetica", 16), width=6, height=3, command=lambda row=i, col=j: self.make_move(row, col)
                )
                self.buttons[i][j].grid(row=i, column=j)

        if single_player and self.current_player == "O":
            self.computer_move()

    def make_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.is_board_full():
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                if self.single_player and self.current_player == "O":
                    self.computer_move()

    def computer_move(self):
        empty_cells = [(row, col) for row in range(3) for col in range(3) if self.board[row][col] == " "]
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.make_move(row, col)

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return True
        return False

    def is_board_full(self):
        return all(all(cell != " " for cell in row) for row in self.board)

    def reset_game(self):
        self.frame.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGUI(root)
    root.mainloop()
