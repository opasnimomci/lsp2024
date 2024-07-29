import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
FPS = 60
PLAYER_WIDTH, PLAYER_HEIGHT = 20, 100
SPELL_WIDTH, SPELL_HEIGHT = 10, 5
PLAYER_SPEED = 5
SPELL_SPEED = 7
GRAVITY = 0.5
JUMP_STRENGTH = -10

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Two-Player Spell Battle")

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Define the players
player1 = pygame.Rect(50, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
player2 = pygame.Rect(WIDTH - 50 - PLAYER_WIDTH, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
player1_vel_y = 0
player2_vel_y = 0
player1_on_ground = True
player2_on_ground = True

# Define the spells
spells = []

# Function to handle player movement
def move_player(player, up_key, down_key, vel_y, on_ground):
    keys = pygame.key.get_pressed()
    if keys[up_key] and on_ground:
        vel_y = JUMP_STRENGTH
        on_ground = False
    if keys[down_key]:
        player.y += PLAYER_SPEED

    player.y += vel_y
    if not on_ground:
        vel_y += GRAVITY

    if player.bottom >= HEIGHT:
        player.bottom = HEIGHT
        vel_y = 0
        on_ground = True

    return vel_y, on_ground

# Function to handle spell movement
def move_spells(spells):
    for spell in spells[:]:
        spell['rect'].x += spell['speed']
        if spell['rect'].x < 0 or spell['rect'].x > WIDTH:
            spells.remove(spell)

# Function to handle spell collision
def handle_collisions(spells, player):
    for spell in spells[:]:
        if player.colliderect(spell['rect']):
            spells.remove(spell)
            return True
    return False

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:  # Player 1 fires spell
                spell_rect = pygame.Rect(player1.right, player1.centery - SPELL_HEIGHT // 2, SPELL_WIDTH, SPELL_HEIGHT)
                spells.append({'rect': spell_rect, 'speed': SPELL_SPEED, 'color': RED})
            if event.key == pygame.K_w:  # Player 1 fires different spell
                spell_rect = pygame.Rect(player1.right, player1.centery - SPELL_HEIGHT // 2, SPELL_WIDTH, SPELL_HEIGHT)
                spells.append({'rect': spell_rect, 'speed': SPELL_SPEED, 'color': GREEN})
            if event.key == pygame.K_e:  # Player 1 fires another spell
                spell_rect = pygame.Rect(player1.right, player1.centery - SPELL_HEIGHT // 2, SPELL_WIDTH, SPELL_HEIGHT)
                spells.append({'rect': spell_rect, 'speed': SPELL_SPEED, 'color': YELLOW})
                
            if event.key == pygame.K_p:  # Player 2 fires spell
                spell_rect = pygame.Rect(player2.left - SPELL_WIDTH, player2.centery - SPELL_HEIGHT // 2, SPELL_WIDTH, SPELL_HEIGHT)
                spells.append({'rect': spell_rect, 'speed': -SPELL_SPEED, 'color': BLUE})
            if event.key == pygame.K_i:  # Player 2 fires different spell
                spell_rect = pygame.Rect(player2.left - SPELL_WIDTH, player2.centery - SPELL_HEIGHT // 2, SPELL_WIDTH, SPELL_HEIGHT)
                spells.append({'rect': spell_rect, 'speed': -SPELL_SPEED, 'color': GREEN})
            if event.key == pygame.K_o:  # Player 2 fires another spell
                spell_rect = pygame.Rect(player2.left - SPELL_WIDTH, player2.centery - SPELL_HEIGHT // 2, SPELL_WIDTH, SPELL_HEIGHT)
                spells.append({'rect': spell_rect, 'speed': -SPELL_SPEED, 'color': YELLOW})

    # Move players
    player1_vel_y, player1_on_ground = move_player(player1, pygame.K_a, pygame.K_s, player1_vel_y, player1_on_ground)
    player2_vel_y, player2_on_ground = move_player(player2, pygame.K_UP, pygame.K_DOWN, player2_vel_y, player2_on_ground)

    # Move spells
    move_spells(spells)

    # Handle collisions
    if handle_collisions(spells, player1):
        print("Player 2 hits Player 1!")
    if handle_collisions(spells, player2):
        print("Player 1 hits Player 2!")

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, RED, player1)
    pygame.draw.rect(screen, BLUE, player2)
    for spell in spells:
        pygame.draw.rect(screen, spell['color'], spell['rect'])

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
