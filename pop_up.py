import pygame
from constants import *


pygame.init()

font = pygame.font.SysFont(None, 36)

def draw_popup(screen, message):
    popup_width = 300
    popup_height = 150
    popup_x = (SCREEN_WIDTH - popup_width) / 2
    popup_y = (SCREEN_HEIGHT - popup_height) / 2
    
    # Draw the popup background
    pygame.draw.rect(screen, WHITE, (popup_x, popup_y, popup_width, popup_height))
    
    # Render the message and center it in the popup
    text_surface = font.render(message, True, BLACK)
    text_rect = text_surface.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    
    screen.blit(text_surface, text_rect)