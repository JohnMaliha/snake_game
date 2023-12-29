
# Définir la fonction qui affiche le score
def show_score(text_font,window,text_color,score):
    # Créer une surface de texte avec le score
    text_surface = text_font.render("Score: " + str(score), True, text_color)
    # Obtenir le rectangle de la surface de texte
    text_rect = text_surface.get_rect()
    # Positionner le rectangle en haut à gauche de la fenêtre
    text_rect.topleft = (10, 10)
    # Dessiner la surface de texte sur la fenêtre
    window.blit(text_surface, text_rect)
