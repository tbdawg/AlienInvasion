import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


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
        # Add bullets
        self.bullets = pygame.sprite.Group()
        # Add aliens
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

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
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

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

    def _update_bullets(self):
        """Update position of bullets, get rid of old bullets"""
        # Update bullet positions
        self.bullets.update()
        # Get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _draw_bullets_to_screen(self):
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

    def _update_screen(self):
        # Update images on the screen and flip to the new screen
        self.screen.fill(self.settings.bg_color)
        self.ship.blit_me()
        self._draw_bullets_to_screen()
        self.aliens.draw(self.screen)
        pygame.display.flip()

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _create_fleet(self):
        """Create the fleet of aliens"""
        # Create an alien and find the number of aliens in a row
        # Spacing between each alien is one alien width
        alien = Alien(self)
        alien_width = alien.rect.width
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_of_aliens = available_space_x // (2 * alien_width)

        # Create the first row of aliens
        for alien_number in range(number_of_aliens):
            # Create an alien and place it in the row
            alien = Alien(self)
            alien.x = alien_width + 2 * alien_width * alien_number
            alien.rect.x = alien.x
            self.aliens.add(alien)


if __name__ == '__main__':
    """Make a game instance and run the game."""
    ai = AlienInvasion()
    ai.run_game()
