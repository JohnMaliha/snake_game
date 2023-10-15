# Import pygame module
import pygame
import time
from popup_utils import draw_popup
from functions import *
from enums import *
from constants import *

# Initialize pygame
pygame.init()

# Define a boolean variable to control the main game loop
game = True

# Define the initial position and direction of the snake
snake_x = SCREEN_WIDTH // 2.5
snake_y = SCREEN_HEIGHT // 2.5
snake_dx = 0
snake_dy = 0

# Define a list to store the snake segments
snake_segments = []

# Define the initial length of the snake
snake_length = 1


status = GameStatus.Starting

# Define the size of the screen and create it
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the title of the window
pygame.display.set_caption(Messages.APP_NAME.value)

# Define a function to draw the snake on the screen
def draw_snake():
    # Loop through the snake segments and draw them as rectangles
    for segment in snake_segments:
        pygame.draw.rect(screen, GREEN, [segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE])


# Generate an initial food position
food_x, food_y = generate_food()

# Define a function to draw the food on the screen
def draw_food():
    # Draw the food as a red rectangle
    pygame.draw.rect(screen, RED, [food_x, food_y, SNAKE_SIZE, SNAKE_SIZE])

# Create a Rect object for the food
food_rect = pygame.Rect(food_x, food_y, SNAKE_SIZE, SNAKE_SIZE)

# Define a clock object to control the frame rate
clock = pygame.time.Clock()

while(game):
    print(status)

    for event in pygame.event.get():
        pygame.display.flip()

        if status == GameStatus.Exit:
            time.sleep(1)
            game = False

        if status == GameStatus.Starting:
            draw_popup(screen,Messages.WELCOME.value)
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                status = GameStatus.Running

        elif status == GameStatus.GameOver:
            draw_popup(screen, Messages.GAME_OVER.value)
            time.sleep(2)
            status = GameStatus.Stopping
    
        elif status == GameStatus.Stopping :
            draw_popup(screen, Messages.EXIT_MSG.value)
            status = GameStatus.Exit
            
        elif status == GameStatus.Running :

            if event.type == pygame.QUIT:
                status = GameStatus.Stopping
                
            if event.type == pygame.KEYUP and event.key == pygame.K_p:
                status = GameStatus.Pause

            if event.type == pygame.KEYUP and event.key == pygame.K_s:
                status = GameStatus.Running
                        
            # If the user presses a key, change the direction of the snake accordingly
            elif event.type == pygame.KEYDOWN:
                if event.key == Direction.LEFT.value:
                    snake_dx = -SNAKE_SPEED
                    snake_dy = 0
                elif event.key == Direction.RIGHT.value:
                    snake_dx = SNAKE_SPEED
                    snake_dy = 0
                elif event.key == Direction.UP.value:
                    snake_dx = 0
                    snake_dy = -SNAKE_SPEED
                elif event.key == Direction.DOWN.value:
                    snake_dx = 0
                    snake_dy = SNAKE_SPEED
        
    if status == GameStatus.Pause:
        draw_popup(screen,Messages.GAME_PAUSED.value)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            status = GameStatus.Running
         
    if status == GameStatus.Running:
        # Update the position of the snake head by adding the velocity to it
        snake_x += snake_dx
        snake_y += snake_dy
        if snake_x >= SCREEN_WIDTH:
                snake_dx = -SNAKE_SPEED
                snake_dy = 0
        elif snake_x <= 0:
                snake_dx = SNAKE_SPEED
                snake_dy = 0
        elif snake_y >= SCREEN_HEIGHT:
                snake_dx = 0
                snake_dy = -SNAKE_SPEED
        elif snake_y <= 0:
                snake_dx = 0
                snake_dy = SNAKE_SPEED

        snake_head_rect = pygame.Rect(snake_x, snake_y, SNAKE_SIZE, SNAKE_SIZE)
        # Check if the snake has eaten the food by checking for a collision between the head and the food
        if snake_head_rect.colliderect(food_rect):
            snake_length += 1
                # Generate a new food position and make sure it does not overlap with the snake body
            while True:
                food_x, food_y = generate_food()
                food_rect = pygame.Rect(food_x, food_y, SNAKE_SIZE, SNAKE_SIZE)  # Update food_rect with new coordinates
                if (food_x, food_y) not in snake_segments:
                    break


        # Add the new snake head position to the beginning of the list of segments 
        snake_segments.insert(0, (snake_x, snake_y))

            # Remove the last segment of the snake if it has reached its maximum length 
        if len(snake_segments) > snake_length:
            snake_segments.pop()

            # Check if the snake has collided with its own body by looking for repeated segments and end the game if so
        if len(snake_segments) != len(set(snake_segments)):
            status = GameStatus.GameOver

        # Fill the screen with black color
        screen.fill(BLACK)

            # Draw the snake and the food on the screen
        draw_snake()
        draw_food()

            # Update the display
        pygame.display.flip()

        # Set the frame rate to 10 frames per second
        clock.tick(FPS)
        
    
    pygame.display.flip()
pygame.quit()