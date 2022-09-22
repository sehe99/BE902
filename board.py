from typing import Tuple
from snake import Snake
import random
import direction
default_snake_start_body = [(10,10),(11,10), (12,10), (13,10), (14,10), (15,10)]

class Board:
    apple = None    
    def __init__(self, board_size_x: int, board_size_y: int, default_direction=direction.RIGHT, snake=None, init_apple = None):
        self.board_size_x = board_size_x
        self.board_size_y = board_size_y
        self.snake = Snake(snake or default_snake_start_body, default_direction)
        # This line could probably help you a bit with the score 
        self.start_length = len(self.snake)
        self.apple = init_apple
        if not init_apple:
            self._generate_new_apple()
    
    # Returns the total score of the game
    def get_score(self) -> int:
        # This function needs fixing! 
        # It should return a meaningful score of the game
        # This should probably have something to do with 
        # the number of apples eaten or similar
        # len(default_snake_start_body)
        current_length = len(self.snake) - self.start_length
        return current_length
    
    # Returns true if a position lies outside the game board in any direction
    def is_out_of_bound(self, position: tuple) -> bool:
        # This function needs fixing! 
        # Correct it to make to check if the snake is outside the board
        # You may wish to remove the print outs when you're done
        print("Current position: ", position, "Board size: ", (self.board_size_x, self.board_size_y))
        print(position[0])
        if position[0] > self.board_size_x or position[0] < 0:
            return True
        if position[1] > self.board_size_y or position[1] < 0:
            return True
        return False

    # this function sets the new direction of the snake
    # Makes sure that the snake doesn't do a U-turn on the spot
    def handle_direction_input(self, wanted_direction: tuple) -> None:
        # This function needs fixing! 
        # Right now the game allows the snake to make a u-turn on the spot and die
        # This shouldn't be possible
        # Update the function so that it ignores any new direction that creates a u-turn

        # If the desired direction isn't a value at all, don't update anything
        # In that case the snake just continues it current path
        #print(wanted_direction)
        print(self.snake.last_direction)
        if wanted_direction(0) = self.snake.last_direction(-0)
            return False
            print(False)
        # Set the new direction of the snake according input from user/A.I
        self.snake.last_direction = wanted_direction

    # Move the game one step
    # This checks if the game is over, 
    # and if not moves the snake
    # and add a new apple if needed
    def tick(self) -> None:
        if self.is_game_over():
            return
        self._move_snake(self.apple)
        if self.apple == self.snake.head():
            self._generate_new_apple()

    # Returns true if the game is over
    # The game should be over when the snake has collided with itself
    # or if the snake has gone outside the map
    def is_game_over(self) -> bool:
        return self.snake.is_snake_crossing_itself() or self.is_out_of_bound(self.snake.head())

    # This function moves the snakes to a new position by a new position
    # one step in the direction that snake is travelling
    # while also removing the last square of the snake,
    # unless the snake just ate an apple
    def _move_snake(self, apple: tuple) -> None:
        # Calculate the next position of the head
        # which is the one step in the direction the snake is travelling
        new_x_pos = self.snake.head()[0] + self.snake.last_direction[0]
        new_y_pos = self.snake.head()[1] + self.snake.last_direction[1]
        new_pos = (new_x_pos, new_y_pos)
        self.snake.extend_snake(new_pos) # Add the new position to the front of the snake
        # Check if the new position of the head is on the same spot as the apple
        is_eating_apple = new_pos == apple
        if not is_eating_apple:
            self.snake.remove_tail()

    def _generate_new_apple(self) -> None:
        # Randomly select a position on the map and place an apple there
        self.apple = self._random_board_position()
        # If that place happens to on the actual snake
        # then run the function again until it lands on a spot not occupied by snake
        while self.apple in self.snake.body: 
            self._generate_new_apple()

    def _random_board_position(self) -> Tuple:
        random_x_position = random.randrange(1, self.board_size_x)
        random_y_position = random.randrange(1, self.board_size_y)
        return (random_x_position, random_y_position)