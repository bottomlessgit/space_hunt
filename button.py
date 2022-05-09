import pygame


class Button():
    """Class to represent clickable buttons"""

    def __init__(self, settings, screen, text):
        """Initializes button object"""
        # Assign screen for drawing to
        self.screen = screen
        self.screen_rect = screen.get_rect()
        # Assign font object
        self.font = pygame.font.SysFont(None, settings.button_text_size, True)
        self.text = text
        # Render text image
        self.text_image = self.font.render(
            text, True, settings.button_text_color)
        self.text_rect = self.text_image.get_rect()
        # Create surface on which to draw text
        self.image = pygame.Surface(settings.button_dimensions)
        self.image.fill(settings.button_color)
        self.rect = self.image.get_rect()
        # Draw text onto button surface
        self.text_rect.center = self.rect.center
        self.image.blit(self.text_image, self.text_rect)
        # Now set Rect to center of screen
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw button to screen"""
        self.screen.blit(self.image, self.rect)
