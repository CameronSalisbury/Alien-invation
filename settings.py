class Settings:
    """A class to store all the settings for Alen Invasion"""
    def __init__(self):
        """initialize the game settings"""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        #bullet settings
        self.bullet_speed = 8.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0, 230, 230)
        self.bullets_allowed = 10
         
        # Alien Settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left. 
        self.fleet_direction = 1