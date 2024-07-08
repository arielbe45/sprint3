import time

import pygame
import sys



def game(qr_count=1, loop_count=2):
    # Initialize Pygame
    pygame.init()

    # Screen dimensions and fullscreen setup
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
    pygame.display.set_caption("QR Game")

    background_image = pygame.image.load("game/qr0.png")
    background_image = pygame.transform.scale(background_image, (300, 300))
    background_rect = background_image.get_rect()
    background_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    # Colors
    WHITE = (255, 255, 255)
    LIGHT_RED = (255, 100, 100)
    BLACK = (0, 0, 0)

    # Player settings
    player_width = 50
    player_height = 60
    player_x = SCREEN_WIDTH // 2
    player_y = SCREEN_HEIGHT - player_height - 90  # Place player above the QR image by 90 pixels
    player_speed = 5
    jump_speed = 10
    gravity = 1
    player_direction = 1

    # Font settings for the title
    title_font = pygame.font.SysFont(None, 72)

    # Clock object to control the frame rate
    clock = pygame.time.Clock()

    # Load player sprite
    player_sprite = pygame.Surface((player_width, player_height))
    player_sprite.fill(LIGHT_RED)

    # Position the QR image in the center of the screen with a margin of 30 pixels

    # Player state
    is_jumping = False
    jump_velocity = jump_speed

    # Game loop
    start = time.time()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_SPACE and not is_jumping:
                    is_jumping = True
                    jump_velocity = jump_speed

        # Update player position
        player_x += player_speed * player_direction

        # Check for wall collisions
        if player_x <= 0 or player_x + player_width >= SCREEN_WIDTH:
            player_direction *= -1

        # Handle jumping
        if is_jumping:
            player_y -= jump_velocity
            jump_velocity -= gravity
            if jump_velocity < -jump_speed:
                is_jumping = False
                jump_velocity = jump_speed
        else:
            if player_y + player_height < SCREEN_HEIGHT - 10:  # Adjusted to ensure player is above the QR image
                player_y += gravity
            else:
                player_y = SCREEN_HEIGHT - player_height - 10

        # Fill the screen with white
        screen.fill(WHITE)

        screen.blit(background_image, background_rect.topleft)

        # Draw the player
        screen.blit(player_sprite, (player_x, player_y))

        # Draw the title
        title_surface = title_font.render("THE QR GAME!!!", True, BLACK)
        screen.blit(title_surface, (SCREEN_WIDTH//2 - title_surface.get_width()//2, 50))

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

game()
# Quit Pygame
pygame.quit()
sys.exit()
