import pygame

class Ship:
    """A class to manage ship"""

    def __init__(self, ai_game):
        """initialize the ship and set its starting position"""
        self.screen = ai_game.screen
        self.settings =  ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #Load the ship image and get rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #Start each new ship at the bottom center of screen
        self.rect.midbottom = self.screen_rect.midbottom

        #store a float for the ships exact horizontal position
        self.x = float (self.rect.x)

        #movement flag ship should not be moving
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """update ship position based on movement flags"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        #update rect object from self.x
        self.rect.x = self.x
                

    def blitme(self):
        """"draw the ship at its curent location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """center the ship on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)