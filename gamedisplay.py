import pygame, board

# This class draws the actual graphics of the game
# Without much understanding of the actual mechanics
# 

# Colors (Red, Green, Blue)
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)
BLUE = pygame.Color(0, 0, 255)
FONT = 'consolas'

class GameDisplay:
    def __init__(self, game_board: board.Board, game_resolution_x: int,  game_resolution_y: int) -> None:
        self.game_board = game_board
        # game resolution
        self.game_resolution_x = game_resolution_x
        self.game_resolution_y = game_resolution_y

        self.x_conversion = self.game_resolution_x / self.game_board.board_size_x
        self.y_conversion = self.game_resolution_y / self.game_board.board_size_y
        # Initialise game window
        self.game_window = pygame.display.set_mode((self.game_resolution_x, self.game_resolution_y))
        pygame.display.set_caption('Snake for Business')

    def draw(self) -> None:
        self.game_window.fill(BLACK)
        self._draw_snake()
        self._draw_apple()
        self._draw_score()
        pygame.display.update()

    def draw_game_over(self) -> None:
        my_font = pygame.font.SysFont(FONT, 90)
        game_over_surface = my_font.render('YOU DIED', True, RED)
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (self.game_resolution_x/2, self.game_resolution_y/4)
        self.game_window.blit(game_over_surface, game_over_rect)
        pygame.display.flip()
        pygame.display.update()

    def _calc_window_position(self, board_position: tuple) -> tuple:
        new_x = board_position[0] * (self.x_conversion)
        new_y = board_position[1] * (self.y_conversion)
        return (new_x, new_y)

    def _draw_snake(self) -> None:
        for pos in self.game_board.snake.body[:-1]:
            window_position = self._calc_window_position(pos)
            pygame.draw.rect(self.game_window, GREEN, pygame.Rect(window_position[0], window_position[1], self.x_conversion, self.y_conversion))
        # Draw the snakes head in red, so to see there it's going
        head = self.game_board.snake.body[-1]
        window_position = self._calc_window_position(head)
        pygame.draw.rect(self.game_window, RED, pygame.Rect(window_position[0], window_position[1], self.x_conversion, self.y_conversion))

    def _draw_apple(self) -> None:
        # Snake food
        window_position = self._calc_window_position(self.game_board.apple)
        pygame.draw.rect(self.game_window, WHITE, pygame.Rect(window_position[0], window_position[1] , self.x_conversion, self.y_conversion))

    def _draw_score(self) -> None:
        score_font = pygame.font.SysFont(FONT, 20)
        score_surface = score_font.render('Score : ' + str(self.game_board.get_score()), True, WHITE)
        score_rect = score_surface.get_rect()
        # Please the position of the score text in the top right corner
        score_rect.midtop = (self.game_resolution_x/10, 15)    
        self.game_window.blit(score_surface, score_rect)
        