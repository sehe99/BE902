DOWN = (0,1)
UP = (0,-1)
LEFT = (-1,0)
RIGHT = (1,0)

# Help debug direction, send in a direction and get a human readable description
def readable_direction(direction: tuple):
    if direction == DOWN:
        return "DOWN"
    if direction == UP:
        return "UP"
    if direction == LEFT:
        return "LEFT"
    if direction == RIGHT:
        return "RIGHT"
    return "UNKNOWN DIRECTION"
