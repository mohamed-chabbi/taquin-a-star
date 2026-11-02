# Configuration du jeu
ROWS = 6
COLS = 7

EMPTY = 0
RED = 1
YELLOW = 2


# Creation du damier
def create_board():
    board = []
    for r in range(ROWS):
        line = []
        for c in range(COLS):
            line.append(EMPTY)
        board.append(line)
    return board


# Verifier si une colonne est valide
def is_valid_column(board, col):
    return board[0][col] == EMPTY


# Trouver la ligne ou le pion va tomber
def get_next_row(board, col):
    for r in range(ROWS - 1, -1, -1):
        if board[r][col] == EMPTY:
            return r
    return None


# Placer un pion dans une colonne
def drop_piece(board, row, col, player):
    board[row][col] = player


# Verifier si un joueur a gagne
def check_winner(board, player):

    # Verification horizontale
    for r in range(ROWS):
        for c in range(COLS - 3):
            if (board[r][c] == player and
                board[r][c + 1] == player and
                board[r][c + 2] == player and
                board[r][c + 3] == player):
                return True

    # Verification verticale
    for r in range(ROWS - 3):
        for c in range(COLS):
            if (board[r][c] == player and
                board[r + 1][c] == player and
                board[r + 2][c] == player and
                board[r + 3][c] == player):
                return True

    # Verification diagonale descendante
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            if (board[r][c] == player and
                board[r + 1][c + 1] == player and
                board[r + 2][c + 2] == player and
                board[r + 3][c + 3] == player):
                return True

    # Verification diagonale montante
    for r in range(3, ROWS):
        for c in range(COLS - 3):
            if (board[r][c] == player and
                board[r - 1][c + 1] == player and
                board[r - 2][c + 2] == player and
                board[r - 3][c + 3] == player):
                return True

    return False


# Verifier si le damier est plein
def is_draw(board):
    for c in range(COLS):
        if board[0][c] == EMPTY:
            return False
    return True