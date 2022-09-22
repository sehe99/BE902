import pygame
import gamedisplay
import board
import snakeai
import time
import direction

# game_speed difficulty settings
# Easy       ->  10
# Medium     ->  25
# Hard       ->  50
# Super hard ->  120
GAME_SPEED = 10
# Change here to switch between A.I and human
USE_AI = False

# This determins the resolution of the game
# Pixels per game tile 
RESOLUTION_MULTIPLIER = 10

# This creates a new board,
# the board handles the logic of the game
# but does not handle any of the graphics
game_board = board.Board(
    board_size_x= 72,
    board_size_y=48  
)

# this creates a new game display,
# this handles anything that is graphical
display = gamedisplay.GameDisplay(game_board, 
    game_resolution_x=game_board.board_size_x*RESOLUTION_MULTIPLIER,
    game_resolution_y=game_board.board_size_y*RESOLUTION_MULTIPLIER
)

# PyGame the framework that does most of the heavy lifting for us
pygame.init()
# Initiates the A.I
ai = snakeai.SnakeAI()

# FPS (frames per second) controller
game_speed_control = pygame.time.Clock()

def get_human_next_move():
    for event in pygame.event.get():
        # Whenever a key is pressed down
        if event.type == pygame.KEYDOWN:
            # W -> Up; S -> Down; A -> Left; D -> Right
            if event.key == pygame.K_UP or event.key == ord('w'):
                return direction.UP
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                return direction.DOWN
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                return direction.LEFT
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                return direction.RIGHT
# Main logic
while not game_board.is_game_over():
    if USE_AI: 
        next_move = ai.get_next_move(game_board)
    else:
        next_move = get_human_next_move()
    
    game_board.handle_direction_input(next_move)
    # Move the game logic another step
    game_board.tick()
    # update the visible part of the game
    display.draw()
    # make sure the game pauses for a long enough time between each step
    game_speed_control.tick(GAME_SPEED)

# Game is over, draw the final message
display.draw_game_over()
# Sleep for 4 seconds before exiting the game
time.sleep(4)
# Make sure everything shuts down in an orderily fashion
pygame.display.quit()
pygame.quit()
time.sleep(1)
exit()