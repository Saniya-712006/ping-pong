import pygame
from game.game_engine import GameEngine

# Initialize pygame/Start application
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong - Pygame Version")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Game loop
engine = GameEngine(WIDTH, HEIGHT)

def main():
    running = True
    while running:
        SCREEN.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if not engine.game_over:
            engine.handle_input()
            engine.update()
            engine.render(SCREEN)
        else:
            # Show winner screen
            font = pygame.font.SysFont("Arial", 50)
            winner_text = f"{engine.winner} Wins!"
            text_surface = font.render(winner_text, True, WHITE)
            SCREEN.blit(text_surface, (WIDTH // 2 - text_surface.get_width() // 2, HEIGHT // 2 - text_surface.get_height() // 2))
            pygame.display.flip()
            # Wait for 3 seconds then exit
            pygame.time.wait(3000)
            running = False

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    
if __name__ == "__main__":
    main()
