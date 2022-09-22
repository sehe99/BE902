from typing import Tuple
import random
import board
import direction

class SnakeAI:
    # Rewrite this to make it more intelligent. 
    # The function should return a direction
    # Notice that the snake can't turn to the complete oposite direction
    # Going up right now, the snake can't suddenly go down without turning first
    def get_next_move(self, game_board: board.Board) -> tuple:
        print("Apple x posiiton: ", game_board.apple[0], "Apple y posiiton: ", game_board.apple[1])
        print("Head x posiiton: ", game_board.snake.head()[0], "Apple y posiiton: ", game_board.snake.head()[1])
        print("Current Direction", direction.readable_direction(game_board.snake.last_direction))
        print("Current Body Positions: ", game_board.snake.body[:-1])
        options = [direction.DOWN, direction.UP, direction.RIGHT, direction.LEFT]
        # Generate a random number between 0 and 1, if the number is bigger than 0.3,
        # randomly select a new direction, else continue previous direction
        if random.random() > 0.3:
            ai_decision = random.choice(options)
        else:
            ai_decision = game_board.snake.last_direction
        print("AI Decides that snake should go ", direction.readable_direction(ai_decision))
        return ai_decision