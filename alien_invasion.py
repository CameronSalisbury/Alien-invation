import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button


class AlienInvasion:
    """Overall Class to manage game assets and behavior"""

    def __init__(self):
        """Initialise the game, and create assets and behavior"""
        pygame.init()
        #start alien invasion in active state
        self.game_active = False

        #initiate variable to control frames
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        #Commented out because I need to make a setting for fullscreen or not
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        #self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        #self.settings.screen_width = self.screen.get_rect().width
        #self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")

        #create instance to store game stats
        #and create a score board
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        #make play button
        self.play_button = Button(self, "Play")


        self._create_fleet()

        #setbackground color
        self.screen.fill(self.settings.bg_color)

    def _create_fleet(self):
        """create fleet of aliens"""
        #Keep adding aliens until there is no room
        #Spacing between aliens is one alien width and one alien height
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                print(current_x)
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width        
            print(current_y)
            #finished row reset x value and increment y
            current_x = alien_width
            current_y += 2 * alien_height
        
    def _create_alien(self, x_position, y_position):
        """Create an alien and place it in the row"""    
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        """Responds when an alien has reached the edges"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the fleet down a level and ridcule them because they deserve it (they are so mean :( )"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
    
    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            
            self._update_screen()
            #60 fps because we arnt running a nvidia series 1 billion :(
            self.clock.tick(60)

    
    def _check_events(self):
        """watch for keyboard and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_play_button(self, mouse_pos):
        """start a new game when player clicks play"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            #reset game
            self.settings.initialize_dynamic_settings()

            self.stats.reset_stats()
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            self.game_active = True

            self.bullets.empty()
            self.aliens.empty()

            #create a new fleet and center
            self._create_fleet()
            self.ship.center_ship()

            #hide cursor
            pygame.mouse.set_visible(False)


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
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """update the position of the bullets"""
        self.bullets.update()
        #get rid of bullets
        for bullets in self.bullets.copy():
            if bullets.rect.bottom <= 0:
                self.bullets.remove(bullets)
        
        self._check_bullet_alien_collision()


    def _check_bullet_alien_collision(self):
        """now we check for bullet collision"""
        collision = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if collision:
            for aliens in collision.values():
                self.stats.score += self.settings.alien_points + len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            #destroy existing bullets and create new fleet.
            #aliens have been cleared out
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            #increase level
            self.stats.level += 1
            self.sb.prep_level()
        

    def _update_aliens(self):
        """Update the positions of all aliens in the fleet."""
        self._check_fleet_edges()
        self.aliens.update()

        #look for alien ship collision
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        #check for aliens hitting bottom
        self._check_aliens_bottom()
    
    def _ship_hit(self):
        """Respond to ship getting hit"""
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            #get rid of everything on screen
            self.bullets.empty()
            self.aliens.empty()

            #create new fleet
            self._create_fleet()
            self.ship.center_ship()
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

        #pause
        sleep(.5)

    def _check_aliens_bottom(self):
        """Check if aliens hit the bottom of the screen"""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                #treat it like ship got it
                self._ship_hit()
                break
    
    def _update_screen(self):
        """drawin'n stuff for background"""
        self.screen.fill(self.settings.bg_color)
        for bullets in self.bullets.sprites():
            bullets.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)

        #draw score information
        self.sb.show_score()

        #draw the play button
        if not self.game_active:
            self.play_button.draw_button()

        #make most recent drawn screen visibile
        pygame.display.flip()

   
if __name__ == '__main__':
    """"make game instance, and run the game"""
    ai = AlienInvasion()
    ai.run_game()