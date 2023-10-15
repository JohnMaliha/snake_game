BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

SCREEN_WIDTH = 850
SCREEN_HEIGHT = 650

# Define the size and speed of the snake
SNAKE_SIZE = 15
SNAKE_SPEED = 5

# Define the initial position and direction of the snake
snake_x = SCREEN_WIDTH // 2.5
snake_y = SCREEN_HEIGHT // 2.5
snake_dx = 0
snake_dy = 0
show_popup_message = False

# Define a list to store the snake segments
snake_segments = []

# Define the initial length of the snake
snake_length = 1