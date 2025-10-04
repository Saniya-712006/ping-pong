import pygame
import random

class Ball:
    def __init__(self, x, y, width, height, screen_width, screen_height):
        self.original_x = x
        self.original_y = y
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.velocity_x = random.choice([-5, 5])
        self.velocity_y = random.choice([-3, 3])

    def move(self, player, ai):
    # Sub-step movement for collision accuracy
        steps = max(abs(self.velocity_x), abs(self.velocity_y))
        dx = self.velocity_x / steps
        dy = self.velocity_y / steps
        for _ in range(int(steps)):
            self.x += dx
            self.y += dy
            # Wall collision
            if self.y <= 0 or self.y + self.height >= self.screen_height:
                self.velocity_y *= -1
                self.y = max(0, min(self.y, self.screen_height - self.height))
                break
            # Paddle collision
            if self.rect().colliderect(player.rect()) or self.rect().colliderect(ai.rect()):
                self.velocity_x *= -1
                # Move ball outside paddle to prevent sticking
                if self.rect().colliderect(player.rect()):
                    self.x = player.x + player.width
                else:
                    self.x = ai.x - self.width
                break
    def check_collision(self, player, ai):
        # if self.rect().colliderect(player.rect()) or self.rect().colliderect(ai.rect()):
        #     self.velocity_x *= -1
        pass

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        self.velocity_x *= -1
        self.velocity_y = random.choice([-3, 3])

    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
