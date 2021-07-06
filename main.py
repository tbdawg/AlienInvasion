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
        self.screen = pygame.display.set_mode(self.settings.mode)
        pygame.display.set_caption("Alien Invasion")

        # Set the background color
        self.bg_color = (230, 230, 230)

        # Add the ship
        self.ship = Ship(self)

    def _check_events(self):
        # Respond to keyboard presses and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to key presses"""
        if event.key == pygame.K_RIGHT:
            # Move the ship to the right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Move the ship to the left
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_F11:
            self._toggle_fullscreen()

    def _check_keyup_events(self, event):
        """Respond to key releases"""
        if event.key == pygame.K_RIGHT:
            # Stop moving the ship to the right
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            # Stop moving the ship to the left
            self.ship.moving_left = False

    def _toggle_fullscreen(self):
        ship_x_ratio = self.ship.rect.x / self.settings.screen_width
        if not self.settings.fullscreen:
            self.screen = pygame.display.set_mode(self.settings.mode, pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
        else:
            self.screen = pygame.display.set_mode(self.settings.mode, pygame.SHOWN)
        self.settings.fullscreen = not self.settings.fullscreen
        self.ship.rect.x = self.settings.screen_width * ship_x_ratio
        self.ship.x = float(self.ship.rect.x)
        self.ship.rect.bottom = self.screen.get_rect().bottom
        self._update_screen()

    def _update_screen(self):
        # Update images on the screen and flip to the new screen
        self.screen.fill(self.settings.bg_color)
        self.ship.blit_me()
        pygame.display.flip()

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()


if __name__ == '__main__':
    """Make a game instance and run the game."""
    ai = AlienInvasion()
    ai.run_game()
