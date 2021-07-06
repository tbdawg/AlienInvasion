
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

