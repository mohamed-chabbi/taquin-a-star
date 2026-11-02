import tkinter as tk
from taquin_logic import GOAL, h_manhattan, move_tile, shuffle_state, a_star

HEURISTIC = h_manhattan

state = GOAL          
moves = 0             
locked = False        


# Affichage
def draw_board(board):
    for i in range(9):
        if board[i] == 0:
            buttons[i].config(text="", bg="lightgray")
        else:
            buttons[i].config(text=str(board[i]), bg="white")


def board_to_text(board):
    text = ""
    for r in range(3):
        line = ""
        for c in range(3):
            v = board[r * 3 + c]
            if v == 0:
                line = line + "_ "
            else:
                line = line + str(v) + " "
        text = text + "    " + line + "\n"
    return text


def write_log(text):
    log.insert(tk.END, text)
    log.see(tk.END)                           


def log_step(title, board, g):
    # ecrit une etape : titre, scores g h f, et le damier
    h = HEURISTIC(board)
    f = g + h
    write_log(title + " :  g=" + str(g) + "  h=" + str(h) + "  f=" + str(f) + "\n")
    write_log(board_to_text(board) + "\n")
    info_label.config(text="g=" + str(g) + "   h=" + str(h) + "   f=" + str(f))



# Boutons
def new_board(board, title):
    # repart de zero avec un nouveau damier
    global state, moves
    state = board
    moves = 0
    log.delete("1.0", tk.END)
    draw_board(state)
    log_step(title, state, 0)


def click_tile(i):
    # le joueur glisse un jeton ; on affiche l'etape tout de suite
    global state, moves
    if locked:
        return
    new_state = move_tile(state, i)
    if new_state is None:
        return
    state = new_state
    moves = moves + 1
    draw_board(state)
    log_step("Move " + str(moves), state, moves)
    if state == GOAL:
        write_log("Goal reached in " + str(moves) + " moves!\n")


def shuffle():
    if locked:
        return
    new_board(shuffle_state(state, 30), "Start state S")


def reset():
    if locked:
        return
    new_board(GOAL, "Start state S")


def solve():
    global locked
    if locked:
        return
    if state == GOAL:
        info_label.config(text="Already at the goal")
        return

    path, explored = a_star(state, HEURISTIC)

    # on affiche toutes les explorations dans le journal
    log.delete("1.0", tk.END)
    write_log("A* from this state :\n" + board_to_text(state) + "\n")
    n = 1
    for (board, g, h, f) in explored:
        log_step("Exploration " + str(n), board, g)
        n = n + 1
    write_log("Solution found in " + str(len(path) - 1) + " moves.\n")
    write_log("Nodes explored : " + str(len(explored)) + "\n")

    # puis on rejoue la solution sur le damier
    locked = True
    play_step(path, 0)


def play_step(path, i):
    global state, moves, locked
    if i >= len(path):
        state = GOAL
        moves = 0
        locked = False
        info_label.config(text="Goal reached in " + str(len(path) - 1) + " moves")
        return
    draw_board(path[i])
    info_label.config(text="Solution : move " + str(i) + "/" + str(len(path) - 1))
    root.after(600, play_step, path, i + 1)


# Fenetre
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Taquin - A*")

    left = tk.Frame(root)
    left.grid(row=0, column=0, padx=10, pady=10)
    right = tk.Frame(root)
    right.grid(row=0, column=1, padx=10, pady=10)

    # le damier : 9 boutons
    board_frame = tk.Frame(left)
    board_frame.pack()
    buttons = []
    for i in range(9):
        b = tk.Button(board_frame, text="", font=("Arial", 28), width=3, height=1,
                      command=lambda i=i: click_tile(i))
        b.grid(row=i // 3, column=i % 3, padx=2, pady=2)
        buttons.append(b)

    info_label = tk.Label(left, text="", font=("Arial", 11))
    info_label.pack(pady=8)

    tk.Button(left, text="Shuffle", width=20, command=shuffle).pack(pady=2)
    tk.Button(left, text="Reset", width=20, command=reset).pack(pady=2)
    tk.Button(left, text="Solve with A*", width=20, command=solve).pack(pady=2)

    # journal des etapes
    scroll = tk.Scrollbar(right)
    scroll.pack(side=tk.RIGHT, fill=tk.Y)
    log = tk.Text(right, width=38, height=28, font=("Courier", 10),
                  yscrollcommand=scroll.set)
    log.pack(side=tk.LEFT)
    scroll.config(command=log.yview)

    new_board(GOAL, "Start state S")
    root.mainloop()