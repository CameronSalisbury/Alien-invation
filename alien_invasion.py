import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """Overall Class to manage game assets and behavior"""

    def __init__(self):
        """Initialise the game, and create assets and behavior"""
        pygame.init()

        #initiate variable to control frames
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        #Commented out because I need to make a setting for fullscreen or not
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        #self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        #self.settings.screen_width = self.screen.get_rect().width
        #self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

        #setbackground color
        self.screen.fill(self.settings.bg_color)


    
    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_screen()
            #60 fps because we arnt running a nvidia series 1 billion :(
            self.clock.tick(60)
    
    def _check_events(self):
        """watch for keyboard and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses"""
        if event.key == pygame.K_RIGHT:
            #move the ship to the right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """respond to key release"""
        if event.key == pygame.K_RIGHT:
            #move the ship to the right
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullet group"""
        print("your in bullets")
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_screen(self):
        """drawin'n stuff for background"""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            print("drawing bullet")
            bullet.draw_bullet()
        self.ship.blitme()
        #make most recent drawn screen visibile
        pygame.display.flip()

   
if __name__ == '__main__':
    """"make game instance, and run the game"""
    ai = AlienInvasion()
    ai.run_game()