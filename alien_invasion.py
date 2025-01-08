import sys

import pygame
class AlienInvasion:
    """Overall Class to manage game assets and behavior"""

    def ___init__(self):
        """Initialise the game, and create assets and behavior"""
        pygame.init()

        self.screen = pygame.display.set((1200, 800))
        pygame.display.set_caption("Alien Invasion")
    
    def run_game(self):
        """Start the main loop for the game"""

        while True:
            #watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                #make most recent drawn screen visibile
                pygame.display.flip()
    
    if __name__ == '__main__':
        #make game instance, and run the game
        ai = AlienInvasion()
        ai.run_game()