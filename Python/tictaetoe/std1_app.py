# =====================================================================
# 🏛️ STANDARD-1 | CHAPTER 1: THE ORCHESTRATOR
# File: std1_app.py
# Purpose: Connects Engine (Pure Logic) with View (Presentation)
# =====================================================================

import Python.tictaetoe.std1_engine as engine
import Python.tictaetoe.std1_view as view

def main():
    print("===========================================")
    print("   🎮 ACADEMY TIC-TAC-TOE (ARCHITECTED)   ")
    print("===========================================")

    # 1. Initialize State
    board = engine.create_board()
    current_player = "X"

    # 2. Main Execution Loop
    while True:
        # Step A: View observes the state
        view.render_board(board)

        # Step B: Engine computes what moves are legally possible
        available = engine.get_available_moves(board)

        # Step C: View prompts the human for an action
        move = view.prompt_move(current_player, available)

        # Step D: Engine updates the state with the action
        engine.make_move(board, move, current_player)

        # Step E: Engine evaluates if a terminal state has been reached
        if engine.check_winner(board, current_player):
            view.render_board(board)
            view.show_winner(current_player)
            break

        if engine.is_board_full(board):
            view.render_board(board)
            view.show_draw()
            break

        # Step F: Switch turns (Deterministic State Transition)
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()
