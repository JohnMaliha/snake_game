# Import pygame module
import pygame
import random

# Initialize pygame
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Define the size of the screen and create it
SCREEN_WIDTH = 850
SCREEN_HEIGHT = 650
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the title of the window
pygame.display.set_caption("Snake Game")

# Define the size and speed of the snake
SNAKE_SIZE = 20
SNAKE_SPEED = 8

# Define the initial position and direction of the snake
snake_x = SCREEN_WIDTH // 2.5
snake_y = SCREEN_HEIGHT // 2.5
snake_dx = 0
snake_dy = 0

# Define a list to store the snake segments
snake_segments = []

# Define the initial length of the snake
snake_length = 1

# Define a function to draw the snake on the screen
def draw_snake():
    # Loop through the snake segments and draw them as rectangles
    for segment in snake_segments:
        pygame.draw.rect(screen, GREEN, [segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE])

# Define a function to generate a random position for the food
def generate_food():
    # Choose a random x and y coordinate within the screen boundaries
    food_x = SNAKE_SIZE * (random.randint(0, SCREEN_WIDTH // SNAKE_SIZE - 1))
    food_y = SNAKE_SIZE * (random.randint(0, SCREEN_HEIGHT // SNAKE_SIZE - 1))
    # Return the food position as a tuple
    return (food_x, food_y)

# Generate an initial food position
food_x, food_y = generate_food()

# Define a function to draw the food on the screen
def draw_food():
    # Draw the food as a red rectangle
    pygame.draw.rect(screen, RED, [food_x, food_y, SNAKE_SIZE, SNAKE_SIZE])

# Define a boolean variable to control the main game loop
running = True

# Define a clock object to control the frame rate
clock = pygame.time.Clock()

# Start the main game loop
while running:
    # Handle the events in the game window
    for event in pygame.event.get():
        # If the user clicks the close button, exit the game loop
        if event.type == pygame.QUIT:
            print(event.type)
            running = False
        # If the user presses a key, change the direction of the snake accordingly
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_dx = -SNAKE_SPEED
                snake_dy = 0
            elif event.key == pygame.K_RIGHT:
                snake_dx = SNAKE_SPEED
                snake_dy = 0
            elif event.key == pygame.K_UP:
                snake_dx = 0
                snake_dy = -SNAKE_SPEED
            elif event.key == pygame.K_DOWN:
                snake_dx = 0
                snake_dy = SNAKE_SPEED

    # Update the position of the snake head by adding the velocity to it
    snake_x += snake_dx
    snake_y += snake_dy

    # Check if the snake has gone out of the screen boundaries and end the game if so
    if snake_x < 0 or snake_x >= SCREEN_WIDTH or snake_y < 0 or snake_y >= SCREEN_HEIGHT:
        running = False

    # Check if the snake has eaten the food by comparing their positions and increase its length if so
    if snake_x == food_x and snake_y == food_y:
        snake_length += 1
        # Generate a new food position and make sure it does not overlap with the snake body
        while True:
            food_x, food_y = generate_food()
            if (food_x, food_y) not in snake_segments:
                break

    # Add the new snake head position to the beginning of the list of segments 
    snake_segments.insert(0, (snake_x, snake_y))

    # Remove the last segment of the snake if it has reached its maximum length 
    if len(snake_segments) > snake_length:
        snake_segments.pop()

    # Check if the snake has collided with its own body by looking for repeated segments and end the game if so
    if len(snake_segments) != len(set(snake_segments)):
        running = False

    # Fill the screen with black color
    screen.fill(BLACK)

    # Draw the snake and the food on the screen
    draw_snake()
    draw_food()

    # Update the display
    pygame.display.flip()

    # Set the frame rate to 10 frames per second
    clock.tick(10)

# Quit pygame
pygame.quit()
