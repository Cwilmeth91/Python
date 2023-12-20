import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PLAYER_SIZE = 50
GROUND_HEIGHT = 100
FPS = 60
COIN_SIZE = 30
COIN_COUNT = 10  # Adjust as needed

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Platformer")

# Load images
player_image = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE))
player_image.fill(BLUE)

# Set up player
player = pygame.Rect(50, HEIGHT - GROUND_HEIGHT - PLAYER_SIZE, PLAYER_SIZE, PLAYER_SIZE)
player_speed = 5
jump_height = -15
gravity = 1
is_jumping = False

# Set up ground
ground = pygame.Rect(0, HEIGHT - GROUND_HEIGHT, WIDTH, GROUND_HEIGHT)

# Set up coins
coins = []
for _ in range(COIN_COUNT):
    coin = pygame.Rect(random.randint(0, WIDTH - COIN_SIZE), random.randint(0, HEIGHT - GROUND_HEIGHT - COIN_SIZE), COIN_SIZE, COIN_SIZE)
    coins.append(coin)

# Set up player score
score = 0
font = pygame.font.Font(None, 36)

# Clock to control the frame rate
clock = pygame.time.Clock()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Move player
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.x += player_speed

    # Jumping mechanics
    if not is_jumping:
        if keys[pygame.K_SPACE]:
            is_jumping = True
    else:
        if jump_height < 0:
            player.y += jump_height
            jump_height += gravity
        else:
            is_jumping = False
            jump_height = -15

    # Apply gravity
    if player.y < HEIGHT - GROUND_HEIGHT - PLAYER_SIZE:
        player.y += gravity

    # Check for collisions with the ground
    if player.colliderect(ground):
        player.y = HEIGHT - GROUND_HEIGHT - PLAYER_SIZE

    # Check for collisions with coins
    for coin in coins:
        if player.colliderect(coin):
            coins.remove(coin)
            score += 1

    # Clear the screen
    screen.fill(WHITE)

    # Draw player, ground, and coins
    pygame.draw.rect(screen, BLUE, player)
    pygame.draw.rect(screen, BLUE, ground)

    for coin in coins:
        pygame.draw.rect(screen, (255, 255, 0), coin)  # Yellow color for coins

    # Draw score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)