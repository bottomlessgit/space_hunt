import pygame


class Alien(pygame.sprite.Sprite):
    """Class to represent cenemy alien game element"""

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
        self.image = pygame.image.load(settings.alien_filename)
        # Transform image to proper size
        self.image = pygame.transform.scale(
            self.image, settings.alien_dimensions)
        # Convert image (retaining alpha values) for better performance
        self.image = self.image.convert_alpha()
        # Create mask for precise bullet collisions
        self.mask = pygame.mask.from_surface(self.image)
        # Get rect for changing position
        self.rect = self.image.get_rect()
        # Set precise coordinate values to 0, coordinates will be initialized
        # by a broader function that initializes the alien fleet
        self.precise_x = 0.0
        self.precise_y = 0.0

    def update(self):
        """Updates the x position of alien"""
        self.precise_x += self.settings.alien_x_speed
        self.rect.x = int(self.precise_x)

    def move_down_screen(self):
        """Move alien down screen"""
        self.precise_y += self.settings.alien_y_speed
        self.rect.y = int(self.precise_y)

    def draw(self):
        """Draws ship onto screen object"""
        self.screen.blit(self.image, self.rect)

    def hit_side(self):
        """Returns True if alien hits either side of screen"""
        return (self.rect.right > self.screen_rect.right
                or self.rect.left < self.screen_rect.left)

    def hit_bottom(self):
        """Returns true if alien hits bottom of screen"""
        return self.rect.bottom > self.screen_rect.bottom
