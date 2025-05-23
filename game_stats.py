class GameStats:
    """Track game stats for Alien Invaion"""

    def __init__(self, ai_game):
        """initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

        #high score should never be reset
        self.high_score = 0

    def reset_stats(self):
        """initialize stats that change during the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
