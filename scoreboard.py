import pygame


class Scoreboard():
    """Class to print game information onto screen"""

    def __init__(self, settings, screen, stats):
        """Initialize scoreboard object"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.stats = stats

        self.font = pygame.font.SysFont(None, settings.scoreboard_font_size)
        self.refresh_score_surface()

        self.refresh_high_score_surface()

        self.refresh_level_surface()

        ship_image = pygame.image.load(settings.ship_filename)
        self.life_emblem_image = pygame.transform.scale(
            ship_image, settings.life_emblem_dimensions)
        self.life_emblem_image = self.life_emblem_image.convert_alpha()
        self.refresh_lives_surface()

    def refresh_score_surface(self):
        """Creates new surface with score to draw to screen"""
        score = str(self.stats.score)
        self.score_image = self.font.render(
            score, True, self.settings.scoreboard_text_color)
        self.score_rect = self.score_image.get_rect()
        # Set coordinate of score image
        self.score_rect.top = self.screen_rect.top
        self.score_rect.right = self.screen_rect.right

    def refresh_high_score_surface(self):
        """Creates new surface with score to draw to screen"""
        high_score = str(self.stats.high_score)
        self.high_score_image = self.font.render(
            high_score, True, self.settings.scoreboard_text_color)
        self.high_score_rect = self.high_score_image.get_rect()
        # Set coordinate of score image
        self.high_score_rect.top = self.screen_rect.top
        self.high_score_rect.centerx = self.screen_rect.centerx

    def refresh_level_surface(self):
        """Creates a new surface with listed fleet level"""
        level = "lvl " + str(self.stats.level)
        self.level_image = self.font.render(
            level, True, self.settings.scoreboard_text_color)
        self.level_rect = self.level_image.get_rect()
        # Set coordinate of score image
        self.level_rect.top = self.score_rect.bottom
        self.level_rect.right = self.screen_rect.right

    def refresh_lives_surface(self):
        """Creates new surface with remaining lives printed out"""
        self.lives_image = pygame.Surface(
            (self.settings.life_emblem_width * self.stats.lives, self.settings.life_emblem_height))
        self.lives_image_rect = self.lives_image.get_rect()
        self.lives_image_rect.topleft = self.screen_rect.topleft
        emblem_rect = self.life_emblem_image.get_rect()
        emblem_rect.topleft = self.lives_image_rect.topleft
        for emblem in range(self.stats.lives):
            self.lives_image.blit(self.life_emblem_image, emblem_rect)
            emblem_rect.x += emblem_rect.width

    def draw(self):
        """Draw all scoreboard elements to screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.lives_image, self.lives_image_rect)

    def refresh(self):
        """Refreshes all scoreboard elements"""
        self.refresh_score_surface()
        self.refresh_high_score_surface()
        self.refresh_level_surface()
        self.refresh_lives_surface()
