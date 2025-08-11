import customtkinter as ctk
import tkinter.messagebox as messagebox
import random

class TicTacToe(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Tic-Tac-Toe AI")
        self.geometry("400x540")
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        # Game state
        self.scores = {"X": 0, "O": 0, "Draw": 0}
        self.current_player = "X"
        self.ai_enabled = True
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.game_over = False

        # Title
        self.title_label = ctk.CTkLabel(self, text="Tic-Tac-Toe", font=("Helvetica", 28, "bold"))
        self.title_label.pack(pady=18)

        # Mode Selection
        self.mode_frame = ctk.CTkFrame(self)
        self.mode_frame.pack(pady=4)
        self.mode_label = ctk.CTkLabel(self.mode_frame, text="Mode:", font=("Helvetica", 14))
        self.mode_label.grid(row=0, column=0, padx=4)
        self.mode_select = ctk.CTkOptionMenu(self.mode_frame, values=["Vs AI", "2 Players"], command=self.change_mode)
        self.mode_select.grid(row=0, column=1, padx=4)
        self.mode_select.set("Vs AI")

        # Status & Score
        self.status_label = ctk.CTkLabel(self, text="Player X's turn", font=("Helvetica", 16))
        self.status_label.pack(pady=8)

        self.score_frame = ctk.CTkFrame(self)
        self.score_frame.pack(pady=6)
        self.x_score = ctk.CTkLabel(self.score_frame, text="X: 0", font=("Helvetica", 14, "bold"))
        self.x_score.grid(row=0, column=0, padx=8)
        self.o_score = ctk.CTkLabel(self.score_frame, text="O: 0", font=("Helvetica", 14, "bold"))
        self.o_score.grid(row=0, column=1, padx=8)
        self.draw_score = ctk.CTkLabel(self.score_frame, text="Draw: 0", font=("Helvetica", 14, "bold"))
        self.draw_score.grid(row=0, column=2, padx=8)

        # Game Board
        self.button_frame = ctk.CTkFrame(self)
        self.button_frame.pack(pady=12)
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                btn = ctk.CTkButton(
                    self.button_frame, text="", width=80, height=80,
                    font=("Helvetica", 34, "bold"), corner_radius=18,
                    fg_color="#333C4A", hover_color="#395886",
                    command=lambda r=row, c=col: self.make_move(r, c)
                )
                btn.grid(row=row, column=col, padx=10, pady=10)
                self.buttons[row][col] = btn

        # Reset Button
        self.reset_btn = ctk.CTkButton(self, text="Reset Game", command=self.reset_game, width=150)
        self.reset_btn.pack(pady=18)

        self.update_scoreboard()

    def change_mode(self, mode):
        self.ai_enabled = (mode == "Vs AI")
        self.reset_game()

    def make_move(self, row, col):
        if self.board[row][col] == "" and not self.game_over:
            self.board[row][col] = self.current_player
            self.buttons[row][col].configure(text=self.current_player, state="disabled", fg_color="#395886" if self.current_player == "X" else "#E17055")
            winner = self.check_winner()
            if winner or self.is_draw():
                self.handle_game_end(winner)
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.status_label.configure(text=f"Player {self.current_player}'s turn")
                # AI's turn
                if self.ai_enabled and self.current_player == "O":
                    self.after(350, self.ai_move)

    def ai_move(self):
        if self.game_over:
            return
        row, col = self.find_best_move()
        if row is not None and col is not None:
            self.make_move(row, col)

    def check_winner(self):
        b = self.board
        for i in range(3):
            if b[i][0] == b[i][1] == b[i][2] != "":
                return b[i][0]
            if b[0][i] == b[1][i] == b[2][i] != "":
                return b[0][i]
        if b[0][0] == b[1][1] == b[2][2] != "":
            return b[0][0]
        if b[0][2] == b[1][1] == b[2][0] != "":
            return b[0][2]
        return None

    def is_draw(self):
        return all(self.board[row][col] != "" for row in range(3) for col in range(3))

    def handle_game_end(self, winner):
        self.game_over = True
        if winner:
            self.status_label.configure(text=f"Player {winner} wins!")
            self.scores[winner] += 1
            self.highlight_winning_line(winner)
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
        else:
            self.status_label.configure(text="Draw!")
            self.scores["Draw"] += 1
            messagebox.showinfo("Game Over", "It's a draw!")
        self.update_scoreboard()
        # Disable board
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].configure(state="disabled")

    def update_scoreboard(self):
        self.x_score.configure(text=f"X: {self.scores['X']}")
        self.o_score.configure(text=f"O: {self.scores['O']}")
        self.draw_score.configure(text=f"Draw: {self.scores['Draw']}")

    def highlight_winning_line(self, winner):
        b = self.board
        for i in range(3):
            if b[i][0] == b[i][1] == b[i][2] == winner:
                for col in range(3):
                    self.buttons[i][col].configure(fg_color="#00B894")
                return
            if b[0][i] == b[1][i] == b[2][i] == winner:
                for row in range(3):
                    self.buttons[row][i].configure(fg_color="#00B894")
                return
        if b[0][0] == b[1][1] == b[2][2] == winner:
            for i in range(3):
                self.buttons[i][i].configure(fg_color="#00B894")
            return
        if b[0][2] == b[1][1] == b[2][0] == winner:
            for i in range(3):
                self.buttons[i][2-i].configure(fg_color="#00B894")
            return

    def reset_game(self):
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.game_over = False
        self.status_label.configure(text="Player X's turn")
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].configure(text="", state="normal", fg_color="#333C4A")
        if self.ai_enabled and self.current_player == "O":
            self.after(400, self.ai_move)

    # Minimax AI (unbeatable)
    def find_best_move(self):
        best_score = -float("inf")
        best_move = None
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == "":
                    self.board[row][col] = "O"
                    score = self.minimax(False)
                    self.board[row][col] = ""
                    if score > best_score:
                        best_score = score
                        best_move = (row, col)
        # If no best move (shouldn't happen), pick random
        if not best_move:
            empty = [(r, c) for r in range(3) for c in range(3) if self.board[r][c] == ""]
            return random.choice(empty) if empty else (None, None)
        return best_move

    def minimax(self, is_ai):
        winner = self.check_winner()
        if winner == "O":
            return 1
        elif winner == "X":
            return -1
        elif self.is_draw():
            return 0

        if is_ai:
            best_score = -float("inf")
            for row in range(3):
                for col in range(3):
                    if self.board[row][col] == "":
                        self.board[row][col] = "O"
                        score = self.minimax(False)
                        self.board[row][col] = ""
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float("inf")
            for row in range(3):
                for col in range(3):
                    if self.board[row][col] == "":
                        self.board[row][col] = "X"
                        score = self.minimax(True)
                        self.board[row][col] = ""
                        best_score = min(score, best_score)
            return best_score

if __name__ == "__main__":
    app = TicTacToe()
    app.mainloop()