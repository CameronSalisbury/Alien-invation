class Settings:
    """A class to store all the settings for Alen Invasion"""
    def __init__(self):
        """initialize the game settings"""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #ship settings
        self.ship_limit = 3

        #bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0, 230, 230)
        self.bullets_allowed = 10
         
        # Alien Settings
        self.fleet_drop_speed = 10

        #how quickly the game speeds up
        self.speedup_scale = 1.1

        #how quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """initialize settings that change through out the game"""
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.alien_speed = 1.0

        # fleet_direction of 1 represents right; -1 represents left. 
        self.fleet_direction = 1
        # base score for alien
        self.alien_points = 50

    def increase_speed(self):
        """Increase the speed settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        
        

        