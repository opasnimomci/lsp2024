import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 640, 480
FPS = 60

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arrow Key Sequence Game")

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
COLORS = [RED, GREEN, BLUE, YELLOW]

# Define the arrow keys and their names
ARROW_KEYS = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]
ARROW_KEY_NAMES = ['UP', 'DOWN', 'LEFT', 'RIGHT']

# Function to generate a random sequence of arrow keys
def generate_sequence(length):
    return [random.choice(ARROW_KEYS) for _ in range(length)]

# Function to draw the sequence on the screen
def draw_sequence(sequence):
    font = pygame.font.Font(None, 36)
    x, y = WIDTH // 2 - 50, HEIGHT // 4
    for key in sequence:
        key_name = ARROW_KEY_NAMES[ARROW_KEYS.index(key)]
        text = font.render(key_name, True, BLACK)
        screen.blit(text, (x, y))
        y += 40  # Move down for the next key

# Initial game setup
sequence = generate_sequence(4)
sequence_index = 0
background_color = WHITE

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(background_color)
    draw_sequence(sequence)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == sequence[sequence_index]:
                sequence_index += 1
                if sequence_index == len(sequence):
                    sequence = generate_sequence(4)
                    sequence_index = 0
                    background_color = random.choice(COLORS)
            else:
                sequence_index = 0  # Reset if wrong key is pressed

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
