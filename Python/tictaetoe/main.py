# ==========================================
# 1. FUNCTION TO DRAW THE BOARD
# ==========================================
def display_board(board):
    # Print row 1 (slots 0, 1, 2)
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    # Print row 2 (slots 3, 4, 5)
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    # Print row 3 (slots 6, 7, 8)
    print(board[6] + " | " + board[7] + " | " + board[8])


# ==========================================
# 2. FUNCTION TO CHECK IF A PLAYER WON
# ==========================================
def check_winner(board, player):
    # Teacher tip: 'player' will be either "X" or "O"
    
    # Check all 3 Horizontal Rows
    if board[0] == player and board[1] == player and board[2] == player:
        return True
    if board[3] == player and board[4] == player and board[5] == player:
        return True
    if board[6] == player and board[7] == player and board[8] == player:
        return True

    # Check all 3 Vertical Columns
    if board[0] == player and board[3] == player and board[6] == player:
        return True
    if board[1] == player and board[4] == player and board[7] == player:
        return True
    if board[2] == player and board[5] == player and board[8] == player:
        return True

    # Check both 2 Diagonal lines (Cross lines)
    if board[0] == player and board[4] == player and board[8] == player:
        return True
    if board[2] == player and board[4] == player and board[6] == player:
        return True

    # If none of the 8 lines matched, nobody won yet!
    return False


# ==========================================
# 3. GAME SETUP (Starting Variables)
# ==========================================
# A list of 9 blank spaces representing empty spots
game_board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

# Player "X" always starts first
current_player = "X"


# ==========================================
# 4. MAIN GAME LOOP
# ==========================================
while True:
    # Step A: Show the current board to the player
    display_board(game_board)
    
    # Step B: Ask the user where they want to place their mark (0 to 8)
    position = int(input(f"Player {current_player}, enter position (0-8): "))

    # Step C: Check if the chosen spot is empty
    if game_board[position] == " ":
        # Valid move: put player's mark ("X" or "O") in that spot
        game_board[position] = current_player
    else:
        # Invalid move: spot is already taken!
        print("Position already taken. Try again.")
        # Teacher tip: 'continue' jumps back to the top of the while loop
        # so the SAME player gets to try again without losing their turn!
        continue

    # Step D: Did this move win the game?
    if check_winner(game_board, current_player):
        display_board(game_board)
        print(f"🎉 Player {current_player} wins!")
        # 'break' stops the while loop immediately because the game is over
        break

    # Step E: Is the board completely full? (Draw / Tie game)
    # If there is no " " (blank space) left, it's a draw
    if " " not in game_board:
        display_board(game_board)
        print("It's a draw! No empty spaces left.")
        break

    # Step F: Switch turns to the other player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"