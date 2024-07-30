import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 800  # Increased screen size
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Two Player Arena")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Fonts
font = pygame.font.Font(None, 54) 

# Character class
class Character:
    def __init__(self, HP, skin, spell, name):
        self.HP = HP
        self.skin = skin
        self.spell = spell
        self.name = name
    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.HP -=5
        if keys[pygame.K_RIGHT]:
            self.HP += 5
            

# Define two characters
player1 = Character(HP=100, skin=WHITE, spell="Fireball", name="Player 1")
player2 = Character(HP=100, skin=WHITE, spell="Ice Shard", name="Player 2")

# Player settings
PLAYER_WIDTH, PLAYER_HEIGHT = 75, 75  
PLAYER1_POS = (100, SCREEN_HEIGHT - PLAYER_HEIGHT)
PLAYER2_POS = (SCREEN_WIDTH - 100 - PLAYER_WIDTH, SCREEN_HEIGHT - PLAYER_HEIGHT)

# Health bar settings
BAR_WIDTH, BAR_HEIGHT = 320, 35 

# Game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    kontrole = pygame.key.get_pressed() #POSLE CE DA BUDE SENSOR DATA
    player1.update(kontrole)
    
    # Fill the screen with black
    screen.fill(BLACK)

    # Draw players
    pygame.draw.rect(screen, player1.skin, (*PLAYER1_POS, PLAYER_WIDTH, PLAYER_HEIGHT))
    pygame.draw.rect(screen, player2.skin, (*PLAYER2_POS, PLAYER_WIDTH, PLAYER_HEIGHT))

    # Draw health bars  TREBA CENTRIRATI ALI MRZI ME SAD
    pygame.draw.rect(screen, RED, (100, 70, BAR_WIDTH, BAR_HEIGHT))
    pygame.draw.rect(screen, GREEN, (100, 70, BAR_WIDTH * (player1.HP / 100), BAR_HEIGHT))
    pygame.draw.rect(screen, RED, (SCREEN_WIDTH - 400, 70, BAR_WIDTH, BAR_HEIGHT))
    pygame.draw.rect(screen, GREEN, (SCREEN_WIDTH - 400, 70, BAR_WIDTH * (player2.HP / 100), BAR_HEIGHT))

    # Display player names ISTO TREBA CENTRIRATI
    player1_name_text = font.render(player1.name, True, WHITE)
    player2_name_text = font.render(player2.name, True, WHITE)
    screen.blit(player1_name_text, (100, 20))  
    player2_text_width = player2_name_text.get_width()
    screen.blit(player2_name_text, (SCREEN_WIDTH - 400 + BAR_WIDTH - player2_text_width, 20))

    
    pygame.display.flip()
    clock.tick(30)

    #crkavanje
    if(player1.HP == 0 or player2.HP == 0):
        running = false

pygame.quit()
sys.exit()
