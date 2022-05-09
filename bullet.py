import pygame


class Bullet(pygame.sprite.Sprite):
    """Class to represent bullets shootable by player ship"""

    def __init__(self, settings, screen, ship):
        """Initialize bullet object"""
        super().__init__()
        # Assign screen object
        self.screen = screen
        self.screen_rect = screen.get_rect()
        # Create mask for collisions
        self.mask = pygame.mask.Mask(settings.ship_bullet_dimensions)
        self.mask.fill()
        # Set speed and color from settings
        self.speed = settings.ship_bullet_speed
        self.color = settings.ship_bullet_color
        # Create rect and position based on ship position
        self.rect = pygame.Rect((0, 0), settings.ship_bullet_dimensions)
        self.rect.top = ship.rect.top
        self.rect.centerx = ship.rect.centerx
        # Create precise float value for precise movement speed
        self.precise_y = float(self.rect.y)

    def update(self):
        """Updates bullet position on screen"""
        self.precise_y -= self.speed
        self.rect.y = int(self.precise_y)

    def draw(self):
        """Draws bullet onto screen object"""
        pygame.draw.rect(self.screen, self.color, self.rect)

    def off_screen(self):
        """Returns true if bullet is off top of screen"""
        return self.rect.bottom < self.screen_rect.top
