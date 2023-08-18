import tkinter as tk
from tkinter import messagebox

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(all(cell != " " for cell in row) for row in board)

def minimax(board, depth, is_maximizing):
    scores = {
        "X": 1,
        "O": -1,
        "tie": 0
    }

    if check_winner(board, "X"):
        return scores["X"]
    if check_winner(board, "O"):
        return scores["O"]
    if is_board_full(board):
        return scores["tie"]

    if is_maximizing:
        max_score = float("-inf")
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = "X"
                    score = minimax(board, depth + 1, False)
                    board[row][col] = " "
                    max_score = max(max_score, score)
        return max_score
    else:
        min_score = float("inf")
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = "O"
                    score = minimax(board, depth + 1, True)
                    board[row][col] = " "
                    min_score = min(min_score, score)
        return min_score

def find_best_move(board):
    best_score = float("-inf")
    best_move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = "X"
                score = minimax(board, 0, False)
                board[row][col] = " "
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
    return best_move

def update_button(row, col):
    global player_turn, board

    if board[row][col] == " " and player_turn == "O":
        buttons[row][col].config(text="O")
        board[row][col] = "O"
        if check_winner(board, "O"):
            messagebox.showinfo("Result", "You win!")
            reset_game()
        elif is_board_full(board):
            messagebox.showinfo("Result", "It's a tie!")
            reset_game()
        else:
            player_turn = "X"
            computer_turn()

def computer_turn():
    global player_turn, board

    computer_row, computer_col = find_best_move(board)
    buttons[computer_row][computer_col].config(text="X")
    board[computer_row][computer_col] = "X"
    if check_winner(board, "X"):
        messagebox.showinfo("Result", "Computer wins!")
        reset_game()
    elif is_board_full(board):
        messagebox.showinfo("Result", "It's a tie!")
        reset_game()
    else:
        player_turn = "O"

def reset_game():
    global board
    board = [[" " for _ in range(3)] for _ in range(3)]
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text=" ")
    global player_turn
    player_turn = "O"

def main():
    global buttons, board, player_turn
    board = [[" " for _ in range(3)] for _ in range(3)]
    player_turn = "O"

    root = tk.Tk()
    root.title("Tic-Tac-Toe")

    buttons = [[None, None, None], [None, None, None], [None, None, None]]

    for row in range(3):
        for col in range(3):
            buttons[row][col] = tk.Button(root, text=" ", font=("Helvetica", 24), height=2, width=5,
                                          command=lambda row=row, col=col: update_button(row, col))
            buttons[row][col].grid(row=row, column=col)

    root.mainloop()

if __name__ == "__main__":
    main()
