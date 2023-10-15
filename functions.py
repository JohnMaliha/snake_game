from constants import *
import random

# Define a function to generate a random position for the food
def generate_food():
    # Choose a random x and y coordinate within the screen boundaries
    food_x = SNAKE_SIZE * (random.randint(0, SCREEN_WIDTH // SNAKE_SIZE - 1))
    food_y = SNAKE_SIZE * (random.randint(0, SCREEN_HEIGHT // SNAKE_SIZE - 1))
    # Return the food position as a tuple
    return (food_x, food_y)

