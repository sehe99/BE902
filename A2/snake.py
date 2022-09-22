# the snake is stored a list of tuples,
# Each tuple represents a position on 
# the game board that the snake occupies
# The first position of the list is the snakes tail
# the last position of the list of the snakes head
# Example [ (10,11), (10, 12), (10, 13), (11,13) ]

from typing import Tuple

class Snake:    
    def __init__(self, body: list, last_direction: tuple):
        self.body = body
        # In which direction did the snake move tick?
        self.last_direction = last_direction

    def __len__(self) -> int:
        return len(self.body)

    def __str__(self) -> str:
        return str(self.body)

    # The head is defined as the very last tuple of in the body list
    def head(self) -> tuple:
        return self.body[-1]

    # This function effectivly moves the snake by adding a new position as the new head
    def extend_snake(self, position: Tuple) -> None: 
        self.body.append(position) # New position added last to the list and becoming the new head

    # One the snakes moves, the tail is removed, unless it eats an apple
    def remove_tail(self) -> None: 
        self.body.pop(0) # deletes the first elemnt of the list

    # Returns true if the head of the snake is on the same position as any part of the rest of the body
    def is_snake_crossing_itself(self) -> bool:
        return self.head() in self.body[:-1]

