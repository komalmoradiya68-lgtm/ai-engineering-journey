# =====================================================================
# 🏛️ STANDARD-1 | CHAPTER 1: THE VIEW LAYER
# File: std1_view.py
# Purpose: Visual Terminal Interface & Human Feedback
# Rule: ONLY handles display formatting and user interaction.
# =====================================================================

def render_board(board):
    """
    Renders the 9-slot board array into a clean 3x3 ASCII grid.
    If a slot is empty, we show its index number (0-8) as a subtle guide!
    """
    display_slots = []
    for i, slot in enumerate(board):
        if slot == " ":
            display_slots.append(f"\033[90m{i}\033[0m")  # Gray coordinate number
        else:
            # Bright cyan for X, Yellow for O
            color = "\033[96m" if slot == "X" else "\033[93m"
            display_slots.append(f"{color}{slot}\033[0m")

    print("\n   Current Board:")
    print(f"     {display_slots[0]} | {display_slots[1]} | {display_slots[2]}")
    print("    ---+---+---")
    print(f"     {display_slots[3]} | {display_slots[4]} | {display_slots[5]}")
    print("    ---+---+---")
    print(f"     {display_slots[6]} | {display_slots[7]} | {display_slots[8]}\n")


def prompt_move(player, valid_moves):
    """
    Prompts the active human player for a valid slot index.
    Keeps asking until a valid integer inside valid_moves is entered.
    """
    while True:
        try:
            choice = input(f"👉 Player {player}, select an available slot ({valid_moves}): ")
            position = int(choice)
            if position in valid_moves:
                return position
            else:
                print("❌ Invalid slot! Please choose from the available empty positions.")
        except ValueError:
            print("❌ Input must be a valid number (0 to 8).")


def show_winner(player):
    """Celebration screen for the winning player."""
    print(f"\n🎉 ════════════════════════════════ 🎉")
    print(f"     🏆 CONGRATULATIONS! PLAYER {player} WINS!")
    print(f"🎉 ════════════════════════════════ 🎉\n")


def show_draw():
    """Draw announcement."""
    print("\n🤝 ════════════════════════════════ 🤝")
    print("     IT'S A DRAW! Brilliant defense by both.")
    print("🤝 ════════════════════════════════ 🤝\n")
