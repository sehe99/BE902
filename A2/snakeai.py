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

        #calculates the distances from the snake head to the apple
        x = game_board.apple[0] - game_board.snake.head()[0]
        y = game_board.apple[1] - game_board.snake.head()[1]
        
        #puts snake in the direction of the apple
        if x==0 and y<0:
            options = [direction.UP]
        if x>0 and y<0:
            options = [direction.UP, direction.RIGHT]
        if x>0 and y==0:
            options = [direction.RIGHT]
        if x>0 and y>0:
            options = [direction.RIGHT, direction.DOWN]
        if x==0 and y>0:
            options = [direction.DOWN]
        if x<0 and y>0:
            options = [direction.DOWN, direction.LEFT]
        if x<0 and y==0:
            options = [direction.LEFT]
        if x<0 and y<0:
            options = [direction.LEFT, direction.UP]
            
        #removes the option for the snake to go out of bounds
        if game_board.snake.head()[0] == 1 and direction.LEFT in options:
            options.remove(direction.LEFT)
        elif game_board.snake.head()[0] == game_board.board_size_x-1 and direction.RIGHT in options:
            options.remove(direction.RIGHT)
        elif game_board.snake.head()[1] == 1 and direction.UP in options:
            options.remove(direction.UP)
        elif game_board.snake.head()[1] == game_board.board_size_y-1 and direction.DOWN in options:
            options.remove(direction.DOWN)
            
        #removes the option of 180 degree turn
        if direction.readable_direction(game_board.snake.last_direction) == "LEFT" and direction.RIGHT in options:
            options.remove(direction.RIGHT)
        elif direction.readable_direction(game_board.snake.last_direction) == "RIGHT" and direction.LEFT in options:
            options.remove(direction.LEFT)
        elif direction.readable_direction(game_board.snake.last_direction) == "UP" and direction.DOWN in options:
            options.remove(direction.DOWN)
        elif direction.readable_direction(game_board.snake.last_direction) == "DOWN" and direction.UP in options:
            options.remove(direction.UP)
        
        #removes the option for the snake to cross itself
        if game_board.snake.is_snake_crossing_itself():
            if game_board.snake.lastdirection == direction.LEFT:
                if direction.LEFT in options:
                    options.remove(direction.LEFT)
            if game_board.snake.lastdirection == direction.RIGHT:
                if direction.RIGHT in options:
                    options.remove(direction.RIGHT)
            if game_board.snake.lastdirection == direction.DOWN:
                if direction.DOWN in options:
                    options.remove(direction.DOWN)
            if game_board.snake.lastdirection == direction.UP:
                if direction.UP in options:
                    options.remove(direction.UP)
        
        ai_decision = random.choice(options)
        
        print("AI Decides that snake should go ", direction.readable_direction(ai_decision))
        print("Options ", options)
        return ai_decision