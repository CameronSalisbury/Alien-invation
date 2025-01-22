import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A Class to manage bullets fired froms ship"""

    def __init__(self, ai_game):
        """Create a bullet object at the ships current position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #Create le bullet at 0, 0 and then the correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop + ai_game.ship.rect.midtop

        #Store the bullets position as a float
        self.y = float(self.rect.y)
    
    def update(self):
        """move bullet across screen"""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y
    
    def draw_bullet(self):
        """Draw bullet on screen"""
        print("we are drawing bullet")
        pygame.draw.rect(self.screen, self.color, self.rect)