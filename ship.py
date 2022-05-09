import pygame


class Ship(pygame.sprite.Sprite):
    """Class to represent controllable player ship"""

    def __init__(self, settings, screen):
        """Initializes player ship element"""
        # Initialize Sprite superclass
        super().__init__()
        # Give access to changing settings
        self.settings = settings
        # Set screen and get screen rect for blitting and positioning
        self.screen = screen
        self.screen_rect = screen.get_rect()
        # Load image
        self.image = pygame.image.load(settings.ship_filename)
        # Transform image to proper size
        self.image = pygame.transform.scale(
            self.image, settings.ship_dimensions)
        # Convert image (retaining alpha values) for better performance
        self.image = self.image.convert_alpha()
        # Create mask for precise bullet collisions
        self.mask = pygame.mask.from_surface(self.image)
        # Get rect for changing position
        self.rect = self.image.get_rect()
        # Set moving flags
        self.moving_right = False
        self.moving_left = False
        # Initialize position
        self.initialize_ship_position()

    def initialize_ship_position(self):
        """Initializes ship position at bottom center of screen"""
        # Set ship position to bottom-center of screen
        self.rect.bottom = self.screen_rect.bottom
        self.rect.centerx = self.screen_rect.centerx
        # Create precise (float) value for x for precise speeded movement
        self.precise_x = float(self.rect.x)

    def update(self):
        """Updates the position of ship on screen"""
        # Update precise value of x based on movement flags and screen position
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.precise_x += self.settings.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.precise_x -= self.settings.ship_speed
        # Update rect position using precise_x value
        self.rect.x = int(self.precise_x)

    def blitme(self):
        """Draws ship onto screen object"""
        self.screen.blit(self.image, self.rect)
