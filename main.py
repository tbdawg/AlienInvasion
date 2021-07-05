import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize game and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # Set the background color
        self.bg_color = (230, 230, 230)

        # Add the ship
        self.ship = Ship(self)

    @staticmethod
    def _check_events():
        # Respond to keyboard presses and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        # Update images on the screen and flip to the new screen
        self.screen.fill(self.settings.bg_color)
        self.ship.blit_me()
        pygame.display.flip()

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self._update_screen()


if __name__ == '__main__':
    """Make a game instance and run the game."""
    ai = AlienInvasion()
    ai.run_game()
