from bullet import Bullet
import pygame


class AlienBullet(Bullet):
    """Class to represent bullets fired by aliens"""

    def __init__(self, settings, screen, alien):
        """Initializes alien bullet object"""
        super().__init__(settings, screen, alien)
        # Set alien speed and color for bullet
        self.speed = settings.alien_bullet_speed
        self.color = settings.alien_bullet_color
        self.rect = pygame.Rect((0, 0), settings.alien_bullet_dimensions)
        # Set starting position to center of given alien
        self.rect.center = alien.rect.center
        # Create a mask for checking collisions
        self.mask = pygame.mask.Mask(settings.alien_bullet_dimensions)
        self.mask.fill()

    def off_screen(self):
        """Returns True if bullet hits bottom of screen"""
        return self.rect.bottom > self.screen_rect.bottom
