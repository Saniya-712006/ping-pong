import pygame
from game.game_engine import GameEngine
import sys

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

def replay_menu():
    font = pygame.font.SysFont("Arial", 40)
    options = ["Best of 3", "Best of 5", "Best of 7", "Exit"]
    selected = 0
    while True:
        SCREEN.fill(BLACK)
        title = font.render("Play Again?", True, WHITE)
        SCREEN.blit(title, (WIDTH // 2 - title.get_width() // 2, 100))
        for i, option in enumerate(options):
            color = WHITE if i == selected else (100, 100, 100)
            text = font.render(option, True, color)
            SCREEN.blit(text, (WIDTH // 2 - text.get_width() // 2, 200 + i * 60))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    if selected == 0:
                        return 2  # Best of 3
                    elif selected == 1:
                        return 3  # Best of 5
                    elif selected == 2:
                        return 4  # Best of 7
                    else:
                        pygame.quit()
                        sys.exit()

def main():
    running = True
    best_of = replay_menu()  # Ask for best of X at start
    wins_needed = best_of
    player_wins = 0
    ai_wins = 0

    while running:
        # Create a new game engine for each match in the series
        engine = GameEngine(WIDTH, HEIGHT)  # <-- NEW: re-initialize engine for each match

        # Play a single match until game over
        while not engine.game_over:
            SCREEN.fill(BLACK)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
            engine.handle_input()
            engine.update()
            engine.render(SCREEN)
            pygame.display.flip()
            clock.tick(FPS)

        # Show winner screen after each match
        font = pygame.font.SysFont("Arial", 50)
        winner_text = f"{engine.winner} Wins!"
        text_surface = font.render(winner_text, True, WHITE)
        SCREEN.blit(text_surface, (WIDTH // 2 - text_surface.get_width() // 2, HEIGHT // 2 - text_surface.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(2000)  # <-- CHANGED: shorter wait after each match

        # Track series wins
        if engine.winner == "Player":
            player_wins += 1
        else:
            ai_wins += 1

        # Check if someone has won the series
        if player_wins == wins_needed or ai_wins == wins_needed:
            SCREEN.fill(BLACK)
            final_text = f"{'Player' if player_wins == wins_needed else 'AI'} wins the series!"
            text_surface = font.render(final_text, True, WHITE)
            SCREEN.blit(text_surface, (WIDTH // 2 - text_surface.get_width() // 2, HEIGHT // 2 - text_surface.get_height() // 2))
            pygame.display.flip()
            pygame.time.wait(3000)

            # Replay menu after series ends
            best_of = replay_menu()  # <-- NEW: ask for replay or exit
            if best_of in [2, 3, 4]:
                wins_needed = best_of
                player_wins = 0
                ai_wins = 0
            else:
                running = False

    pygame.quit()

    
if __name__ == "__main__":
    main()
