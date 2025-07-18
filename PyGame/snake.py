import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Define colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up the game clock
clock = pygame.time.Clock()

# Set up the initial position and direction of the snake
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
direction = "RIGHT"

# Set up the initial position of the food
food_position = [random.randrange(
    1, (width // 10)) * 10, random.randrange(1, (height // 10)) * 10]
food_spawned = True

# Set up the initial score
score = 0
font_style = pygame.font.SysFont(None, 40)

# Set up the initial game speed and speed increment
game_speed = 15
speed_increment = 2

# Function to display the score


def display_score():
    score_text = font_style.render("Score: " + str(score), True, GREEN)
    window.blit(score_text, [10, 10])

# Function to display the snake


def display_snake():
    for position in snake_body:
        pygame.draw.rect(window, GREEN, pygame.Rect(
            position[0], position[1], 10, 10))

# Function to display a message popup


def display_message(message):
    message_text = font_style.render(message, True, GREEN)
    window.blit(message_text, [width // 2 - message_text.get_width() //
                2, height // 2 - message_text.get_height() // 2])
    pygame.display.update()
    time.sleep(2)


# Main game loop
game_over = False
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and direction != "DOWN":
                direction = "UP"
            elif event.key == pygame.K_s and direction != "UP":
                direction = "DOWN"
            elif event.key == pygame.K_a and direction != "RIGHT":
                direction = "LEFT"
            elif event.key == pygame.K_d and direction != "LEFT":
                direction = "RIGHT"

    # Move the snake
    if direction == "UP":
        snake_position[1] -= 10
    elif direction == "DOWN":
        snake_position[1] += 10
    elif direction == "LEFT":
        snake_position[0] -= 10
    elif direction == "RIGHT":
        snake_position[0] += 10

    # Check for collision with the wall
    if snake_position[0] < 0 or snake_position[0] >= width or snake_position[1] < 0 or snake_position[1] >= height:
        display_message("Game Over! You hit the wall")
        game_over = True

    # Check for collision with the food
    if snake_position == food_position:
        score += 1
        food_spawned = False

        # Increase game speed after every 2 red points
        if score % 2 == 0:
            game_speed += speed_increment

    # Update the snake body
    snake_body.insert(0, list(snake_position))
    if not food_spawned:
        food_position = [random.randrange(
            1, (width // 10)) * 10, random.randrange(1, (height // 10)) * 10]
        food_spawned = True
    else:
        snake_body.pop()

    # Check for collision with the snake itself
    if snake_position in snake_body[1:]:
        display_message("Game Over! You hit yourself")
        game_over = True

    # Refresh the game window
    window.fill(BLACK)
    display_snake()
    pygame.draw.rect(window, RED, pygame.Rect(
        food_position[0], food_position[1], 10, 10))
    display_score()
    pygame.display.update()

    # Set the game speed
    clock.tick(game_speed)

# Quit Pygame
pygame.quit()
