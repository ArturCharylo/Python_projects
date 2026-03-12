import pygame
import random
import time

# Defined colors as constants for better maintainability
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class Snake:
    """Handles snake movement, body growth, and direction logic."""
    def __init__(self):
        self.position = [100, 50]
        self.body = [[100, 50], [90, 50], [80, 50]]
        self.direction = "RIGHT"
    
    def change_direction(self, new_direction):       
        # Preventing the snake from moving directly backward
        if new_direction == "UP" and self.direction != "DOWN":
            self.direction = "UP"
        elif new_direction == "DOWN" and self.direction != "UP":
            self.direction = "DOWN"
        elif new_direction == "LEFT" and self.direction != "RIGHT":
            self.direction = "LEFT"
        elif new_direction == "RIGHT" and self.direction != "LEFT":
            self.direction = "RIGHT"
    
    def move(self, grow=False):
        """Moves the snake and handles body updates."""
        if self.direction == "UP":
            self.position[1] -= 10
        elif self.direction == "DOWN":
            self.position[1] += 10
        elif self.direction == "LEFT":
            self.position[0] -= 10
        elif self.direction == "RIGHT":
            self.position[0] += 10
        
        # Add new head position
        self.body.insert(0, list(self.position))
        
        # If snake didn't eat food, remove the last tail segment
        if not grow:
            self.body.pop()


class Food: 
    """Handles food spawning logic."""
    def __init__(self, width, height):
        self.position = [0, 0]
        self.spawn_food(width, height)

    def spawn_food(self, width, height):
        """Spawns food at a random position aligned with the 10px grid."""
        self.position = [
            random.randrange(1, (width // 10)) * 10, 
            random.randrange(1, (height // 10)) * 10
        ]
    
class Game:
    """Main game engine handling rendering, collisions, and the game loop."""
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snake Game - Object Oriented")
        
        self.clock = pygame.time.Clock()
        self.font_style = pygame.font.SysFont(None, 40)
        
        self.snake = Snake()
        self.food = Food(width, height)
        self.score = 0
        self.game_speed = 15
        self.speed_increment = 2
    
    def check_collisions(self):
        """Checks for wall and self-collision."""
        # Wall collision
        if (self.snake.position[0] < 0 or self.snake.position[0] >= self.width or 
            self.snake.position[1] < 0 or self.snake.position[1] >= self.height):
            return "wall"

        # Self-collision
        if self.snake.position in self.snake.body[1:]:
            return "self"

        return None

    def check_food_collision(self):
        """Checks if snake head reached the food."""
        if self.snake.position == self.food.position:
            self.score += 1
            # Increase speed every 2 points
            if self.score % 2 == 0:
                self.game_speed += self.speed_increment
            return True
        return False
    
    def display_score(self):
        score_text = self.font_style.render(f"Score: {self.score}", True, GREEN)
        self.window.blit(score_text, [10, 10])
    
    def display_message(self, message):
        message_text = self.font_style.render(message, True, GREEN)
        self.window.blit(
            message_text, 
            [self.width // 2 - message_text.get_width() // 2, 
             self.height // 2 - message_text.get_height() // 2]
        )
        pygame.display.update()
        time.sleep(2)

    def run(self):
        """Starts the main game loop."""
        game_over = False
        while not game_over:
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    # Mapping Pygame constants to direction strings
                    if event.key == pygame.K_w: self.snake.change_direction("UP")
                    elif event.key == pygame.K_s: self.snake.change_direction("DOWN")
                    elif event.key == pygame.K_a: self.snake.change_direction("LEFT")
                    elif event.key == pygame.K_d: self.snake.change_direction("RIGHT")

            # Check if snake eats food BEFORE moving or while moving
            ate_food = self.check_food_collision()
            if ate_food:
                self.food.spawn_food(self.width, self.height)

            # Move snake (pass grow=True if it ate food)
            self.snake.move(grow=ate_food)

            # Check for death
            collision = self.check_collisions()
            if collision:
                msg = "hit the wall" if collision == "wall" else "hit yourself"
                self.display_message(f"Game Over! You {msg}")
                game_over = True

            # Rendering
            self.window.fill(BLACK)
            
            # Draw Snake
            for pos in self.snake.body:
                pygame.draw.rect(self.window, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))
            
            # Draw Food
            pygame.draw.rect(self.window, RED, pygame.Rect(self.food.position[0], self.food.position[1], 10, 10))
            
            self.display_score()
            pygame.display.update()
            self.clock.tick(self.game_speed)

        pygame.quit()

if __name__ == "__main__":
    game = Game(800, 600)
    game.run()