import tkinter as tk
from puissance4_logic import (
    ROWS, COLS, EMPTY, RED, YELLOW,
    create_board, is_valid_column, get_next_row,
    drop_piece, check_winner, is_draw
)

board = create_board()
player = RED
moves = 0
game_over = False


# Affichage
def draw_board():
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == RED:
                cells[r][c].config(text="●", fg="red")
            elif board[r][c] == YELLOW:
                cells[r][c].config(text="●", fg="yellow")
            else:
                cells[r][c].config(text="●", fg="white")


def board_to_text():
    text = ""
    for r in range(ROWS):
        line = ""
        for c in range(COLS):
            if board[r][c] == RED:
                line = line + "R "
            elif board[r][c] == YELLOW:
                line = line + "Y "
            else:
                line = line + ". "
        text = text + line + "\n"
    return text


def write_log(text):
    log.insert(tk.END, text)
    log.see(tk.END)


# Boutons
def new_game():
    global board, player, moves, game_over

    board = create_board()
    player = RED
    moves = 0
    game_over = False

    log.delete("1.0", tk.END)

    draw_board()
    info_label.config(text="Player 1 (Red) turn")
    write_log("New game started!\n\n")


def click_column(col):
    global player, moves, game_over

    if game_over:
        return

    # Verifier si la colonne n'est pas pleine
    if not is_valid_column(board, col):
        info_label.config(text="This column is full!")
        return

    # Placer le pion
    row = get_next_row(board, col)
    drop_piece(board, row, col, player)

    moves = moves + 1
    draw_board()

    # Afficher le coup dans le journal
    if player == RED:
        write_log("Move " + str(moves) + " : Player 1 (Red), Column " + str(col + 1) + "\n")
    else:
        write_log("Move " + str(moves) + " : Player 2 (Yellow), Column " + str(col + 1) + "\n")

    write_log(board_to_text() + "\n")

    # Verifier si le joueur a gagne
    if check_winner(board, player):
        game_over = True

        if player == RED:
            info_label.config(text="Player 1 (Red) wins!")
            write_log("Player 1 (Red) wins!\n")
        else:
            info_label.config(text="Player 2 (Yellow) wins!")
            write_log("Player 2 (Yellow) wins!\n")

        return

    # Verifier si la partie est nulle
    if is_draw(board):
        game_over = True
        info_label.config(text="Draw!")
        write_log("The game is a draw!\n")
        return

    # Changer de joueur
    if player == RED:
        player = YELLOW
        info_label.config(text="Player 2 (Yellow) turn")
    else:
        player = RED
        info_label.config(text="Player 1 (Red) turn")


# Fenetre
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Puissance 4 - Human vs Human")

    left = tk.Frame(root)
    left.grid(row=0, column=0, padx=10, pady=10)

    right = tk.Frame(root)
    right.grid(row=0, column=1, padx=10, pady=10)

    # Les boutons pour choisir une colonne
    column_frame = tk.Frame(left)
    column_frame.pack()

    for c in range(COLS):
        b = tk.Button(
            column_frame,
            text=str(c + 1),
            font=("Arial", 14),
            width=4,
            command=lambda c=c: click_column(c)
        )
        b.grid(row=0, column=c, padx=2, pady=2)

    # Le damier : 6 lignes et 7 colonnes
    board_frame = tk.Frame(left, bg="blue")
    board_frame.pack(pady=5)

    cells = []

    for r in range(ROWS):
        line = []
        for c in range(COLS):
            cell = tk.Label(
                board_frame,
                text="●",
                font=("Arial", 28),
                width=3,
                height=1,
                bg="blue",
                fg="white"
            )
            cell.grid(row=r, column=c, padx=2, pady=2)
            line.append(cell)
        cells.append(line)

    info_label = tk.Label(left, text="", font=("Arial", 12))
    info_label.pack(pady=8)

    tk.Button(
        left,
        text="New Game",
        width=20,
        command=new_game
    ).pack(pady=5)

    # Journal des etapes
    scroll = tk.Scrollbar(right)
    scroll.pack(side=tk.RIGHT, fill=tk.Y)

    log = tk.Text(
        right,
        width=42,
        height=28,
        font=("Courier", 10),
        yscrollcommand=scroll.set
    )
    log.pack(side=tk.LEFT)

    scroll.config(command=log.yview)

    new_game()
    root.mainloop()