
class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the games settings"""
        # Screen settings
        self.screen_width = 1280
        self.screen_height = 720
        self.mode = self.screen_width, self.screen_height
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5
        self.fullscreen = False

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # Fleet direction of 1 = right, -1 = left
        self.fleet_direction = 1
