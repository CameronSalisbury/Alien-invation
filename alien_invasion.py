import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall Class to manage game assets and behavior"""

    def __init__(self):
        """Initialise the game, and create assets and behavior"""
        pygame.init()

        #initiate variable to control frames
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        #setbackground color
        self.screen.fill(self.settings.bg_color)


    
    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self._update_screen()
            self.ship.update()
            #60 fps because we arnt running a nvidia series 1 billion :(
            self.clock.tick(60)
    
    def _check_events(self):
        #watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    #move the ship to the right
                    self.ship.moving_right = True
                elif event.type == pygame.K_LEFT:
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    #move the ship to the right
                    self.ship.moving_right = False
                elif event.type == pygame.K_LEFT:
                    self.ship.moving_left = False
    
    def _update_screen(self):
        #drawin'n stuff for background
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        #make most recent drawn screen visibile
        pygame.display.flip()

   
if __name__ == '__main__':
    #make game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()