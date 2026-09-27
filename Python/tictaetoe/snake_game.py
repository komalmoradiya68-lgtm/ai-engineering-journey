# ==========================================
# 🐍 SNAKE GAME — Built with Pygame
# By: Shlok | Inspired by CommonLuke
# ==========================================
# This game teaches you:
#   - Game loops (the heartbeat of every game)
#   - Drawing shapes on screen
#   - Handling keyboard input
#   - Collision detection
#   - Lists (the snake's body is a list!)
# ==========================================

import pygame
import random

# ==========================================
# 1. INITIALIZE PYGAME
# ==========================================
# Teacher tip: pygame.init() starts up all the Pygame modules.
# You MUST call this before using any Pygame features!
pygame.init()

# ==========================================
# 2. GAME CONSTANTS (Settings)
# ==========================================
# Teacher tip: Constants are variables that NEVER change.
# We write them in ALL CAPS so we know they're constants.

SCREEN_WIDTH = 600       # Width of the game window (in pixels)
SCREEN_HEIGHT = 400      # Height of the game window (in pixels)
BLOCK_SIZE = 20          # Size of each snake block and food (in pixels)
FPS = 10                 # Frames Per Second — controls game speed
                         # Teacher tip: Higher FPS = faster snake!

# ==========================================
# 3. COLORS (RGB = Red, Green, Blue)
# ==========================================
# Teacher tip: Colors in Pygame use (R, G, B) format.
# Each value goes from 0 (none) to 255 (full).
# (0, 0, 0) = Black   |   (255, 255, 255) = White

BLACK  = (0, 0, 0)
WHITE  = (255, 255, 255)
GREEN  = (0, 200, 0)       # Snake body color
DARK_GREEN = (0, 150, 0)   # Snake head color (slightly darker)
RED    = (200, 0, 0)       # Food color
GRAY   = (40, 40, 40)      # Background grid color (subtle)

# ==========================================
# 4. CREATE THE GAME WINDOW
# ==========================================
# Teacher tip: pygame.display.set_mode() creates the window.
# It returns a "surface" — think of it as a canvas you draw on.
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the title that appears at the top of the window
pygame.display.set_caption("🐍 Shlok's Snake Game")

# Create a clock to control the game speed
clock = pygame.time.Clock()

# Load a font for displaying the score
# Teacher tip: None means "use the default system font"
font = pygame.font.Font(None, 35)

# ==========================================
# 5. HELPER FUNCTIONS
# ==========================================

def draw_score(score):
    """Draw the current score in the top-left corner."""
    # Teacher tip: font.render() turns text into an image (surface).
    # True = smooth text (anti-aliasing), WHITE = text color
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))
    # Teacher tip: blit() means "paste this image onto the screen"


def draw_snake(snake_body):
    """Draw every block of the snake's body."""
    for i, block in enumerate(snake_body):
        # Teacher tip: enumerate() gives us both the index (i) and the value (block)
        # block is a list like [x, y] — the position of that body segment

        # The LAST element in the list is the HEAD (newest block added)
        if i == len(snake_body) - 1:
            color = DARK_GREEN   # Head gets a special color
        else:
            color = GREEN        # Body is normal green

        # pygame.draw.rect() draws a rectangle on the screen
        # Arguments: surface, color, (x, y, width, height)
        pygame.draw.rect(screen, color, [block[0], block[1], BLOCK_SIZE, BLOCK_SIZE])

        # Draw a tiny border around each block so they look separate
        pygame.draw.rect(screen, BLACK, [block[0], block[1], BLOCK_SIZE, BLOCK_SIZE], 1)
        # Teacher tip: The last argument (1) means "border only, 1 pixel thick"


def place_food(snake_body):
    """Pick a random position for the food that is NOT on the snake."""
    # Teacher tip: We use a while True loop to keep trying
    # until we find a spot where the snake ISN'T!
    while True:
        food_x = random.randrange(0, SCREEN_WIDTH, BLOCK_SIZE)
        food_y = random.randrange(0, SCREEN_HEIGHT, BLOCK_SIZE)
        food_pos = [food_x, food_y]

        # Check: is this spot occupied by the snake?
        if food_pos not in snake_body:
            return food_pos
            # Teacher tip: 'return' exits BOTH the function AND the while loop!
        # If food landed on the snake, the loop tries again automatically


def show_game_over_screen(score):
    """Display the GAME OVER message and wait for player input."""
    screen.fill(BLACK)

    # Big "GAME OVER" text in the center
    game_over_text = font.render("GAME OVER!", True, RED)
    score_text = font.render(f"Final Score: {score}", True, WHITE)
    restart_text = font.render("Press R to Restart or Q to Quit", True, WHITE)

    # Teacher tip: get_rect() gives us the rectangle of the text surface.
    # Setting center= positions it in the middle of the screen.
    screen.blit(game_over_text, game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)))
    screen.blit(score_text, score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)))
    screen.blit(restart_text, restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)))

    # Teacher tip: pygame.display.flip() updates the ENTIRE screen
    # Nothing you draw appears until you call this!
    pygame.display.flip()

    # Wait for player to press R (restart) or Q (quit)
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False      # Player closed the window
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True   # Player wants to restart
                if event.key == pygame.K_q:
                    return False  # Player wants to quit


# ==========================================
# 6. MAIN GAME FUNCTION
# ==========================================
# Teacher tip: We put the game inside a function so we can
# easily restart it by calling the function again!

def game():
    # --- STARTING VARIABLES ---

    # Snake starts in the middle of the screen
    snake_x = SCREEN_WIDTH // 2
    snake_y = SCREEN_HEIGHT // 2

    # Movement direction (snake starts moving to the RIGHT)
    # Teacher tip: direction_x and direction_y control movement.
    # RIGHT = (BLOCK_SIZE, 0)  |  LEFT = (-BLOCK_SIZE, 0)
    # DOWN  = (0, BLOCK_SIZE)  |  UP   = (0, -BLOCK_SIZE)
    direction_x = BLOCK_SIZE
    direction_y = 0

    # The snake's body — a list of [x, y] positions!
    # Teacher tip: The snake starts with just 1 block (the head).
    # When it eats food, we ADD a new block to this list.
    # When it moves, we REMOVE the oldest block (the tail).
    snake_body = [[snake_x, snake_y]]
    snake_length = 1

    # Place the first food randomly
    food_pos = place_food(snake_body)

    # Score starts at 0
    score = 0

    # Game state
    running = True

    # ==========================================
    # 7. THE GAME LOOP ♻️
    # ==========================================
    # Teacher tip: This is the HEARTBEAT of every game!
    # Every frame, we: 1) Handle input → 2) Update game → 3) Draw everything
    # This loop runs FPS times per second (10 times = 10 FPS)

    while running:

        # ----- STEP A: Handle Events (Keyboard Input) -----
        # Teacher tip: pygame.event.get() returns a list of everything
        # that happened since the last frame (key presses, mouse, etc.)
        for event in pygame.event.get():

            # Did the player click the X button to close the window?
            if event.type == pygame.QUIT:
                return False   # Exit completely

            # Did the player press a key?
            if event.type == pygame.KEYDOWN:

                # Arrow Keys (or WASD) to change direction
                # Teacher tip: We check that the snake can't reverse
                # into itself! (e.g., if going RIGHT, can't go LEFT)

                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    if direction_y != BLOCK_SIZE:      # Not going DOWN
                        direction_x = 0
                        direction_y = -BLOCK_SIZE      # Go UP

                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if direction_y != -BLOCK_SIZE:     # Not going UP
                        direction_x = 0
                        direction_y = BLOCK_SIZE       # Go DOWN

                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if direction_x != BLOCK_SIZE:      # Not going RIGHT
                        direction_x = -BLOCK_SIZE
                        direction_y = 0                # Go LEFT

                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if direction_x != -BLOCK_SIZE:     # Not going LEFT
                        direction_x = BLOCK_SIZE
                        direction_y = 0                # Go RIGHT

        # ----- STEP B: Move the Snake -----
        # Teacher tip: We move the head by adding the direction values.
        snake_x += direction_x
        snake_y += direction_y

        # Add the new head position to the body list
        snake_body.append([snake_x, snake_y])

        # If the snake hasn't eaten food, remove the tail (oldest block)
        # This creates the "slithering" effect!
        if len(snake_body) > snake_length:
            del snake_body[0]
            # Teacher tip: del list[0] removes the FIRST element.
            # The snake moves forward by adding to the end
            # and removing from the beginning!

        # ----- STEP C: Check Collision with WALLS -----
        # Teacher tip: If the snake goes off-screen, game over!
        if snake_x < 0 or snake_x >= SCREEN_WIDTH:
            running = False   # Hit left or right wall
        if snake_y < 0 or snake_y >= SCREEN_HEIGHT:
            running = False   # Hit top or bottom wall

        # ----- STEP D: Check Collision with ITSELF -----
        # Teacher tip: If the head's position matches ANY body block
        # (except the head itself), the snake ate itself!
        # snake_body[:-1] means "all blocks EXCEPT the last one (head)"
        if [snake_x, snake_y] in snake_body[:-1]:
            running = False

        # ----- STEP E: Check if Snake ATE the Food -----
        if snake_x == food_pos[0] and snake_y == food_pos[1]:
            # Grow the snake! (don't remove the tail next frame)
            snake_length += 1
            # Increase score
            score += 10
            # Place new food in a random spot
            food_pos = place_food(snake_body)
            # Teacher tip: We could also increase FPS here
            # to make the game harder as you score more!

        # ----- STEP F: DRAW Everything -----
        # Clear the screen (paint it all black)
        screen.fill(BLACK)

        # Draw the food (a red square)
        pygame.draw.rect(screen, RED, [food_pos[0], food_pos[1], BLOCK_SIZE, BLOCK_SIZE])

        # Draw the snake
        draw_snake(snake_body)

        # Draw the score
        draw_score(score)

        # ----- STEP G: Update the Display -----
        # Teacher tip: NOTHING appears on screen until you call this!
        # Think of it as "flipping" the canvas to show your drawing.
        pygame.display.flip()

        # ----- STEP H: Control the Speed -----
        # Teacher tip: clock.tick(FPS) pauses just enough so the loop
        # runs exactly FPS times per second. Without this, the snake
        # would move at the speed of light!
        clock.tick(FPS)

    # Game loop ended — show Game Over screen
    return show_game_over_screen(score)


# ==========================================
# 8. RUN THE GAME!
# ==========================================
# Teacher tip: This loop lets us restart the game.
# game() returns True if player pressed R (restart),
# or False if they pressed Q (quit) or closed the window.

playing = True
while playing:
    playing = game()

# Clean up and close the window
pygame.quit()
print("Thanks for playing! 🐍")
