# =====================================================================
# 🏛️ STANDARD-1 | CHAPTER 1: THE ENGINE LAYER
# File: std1_engine.py
# Purpose: Pure Mathematical State & Rules of Tic-Tac-Toe
# Rule: NO print() or input() calls are allowed in this file.
# =====================================================================

# 1. State Generator
def create_board():
    """Returns a fresh, empty 9-slot board state."""
    # Teacher tip: A list of 9 blank spaces represents our universe.
    return [" "] * 9


# 2. State Inspector: Available Actions
def get_available_moves(board):
    """
    Returns a list of integer indices (0-8) that are currently empty.
    Example: If slots 0 and 4 are taken, returns [1, 2, 3, 5, 6, 7, 8]
    """
    moves = []
    for index, slot in enumerate(board):
        if slot == " ":
            moves.append(index)
    return moves


# 3. State Inspector: Winning Lines
WINNING_COMBINATIONS = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal Rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical Columns
    (0, 4, 8), (2, 4, 6)              # Diagonals
)

def check_winner(board, player):
    """
    Pure Function: Checks if 'player' ('X' or 'O') has won the game.
    Returns: True if won, False otherwise.
    """
    for a, b, c in WINNING_COMBINATIONS:
        if board[a] == player and board[b] == player and board[c] == player:
            return True
    return False


# 4. State Inspector: Terminal (Game Over) Check
def is_board_full(board):
    """Returns True if there are no empty spaces remaining."""
    return " " not in board


# 5. State Transition Function
def make_move(board, position, player):
    """
    Applies an action to the state.
    Returns: True if the move was legal and applied, False if illegal.
    """
    if 0 <= position <= 8 and board[position] == " ":
        board[position] = player
        return True
    return False
