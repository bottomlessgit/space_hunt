from random import randint
import pygame


class Powerup(pygame.sprite.Sprite):
    """A class to represent powerups that give player ship temporary advantages
    It is a base class for the different powerup, and thus is never meant
    to be instantiated"""

    def __init__(self, settings, screen, stats, frame_counter):
        """Initializes random powerup"""
        # Initialize Sprite superclass
        super().__init__()
        # Give access to settings for changing speeds
        self.settings = settings
        # Give access to stats (just for extra lives)
        self.stats = stats
        # Give access to framecounter for setting expiration time
        self.frame_counter = frame_counter
        # Assign screen to print to
        self.screen = screen
        self.screen_rect = screen.get_rect()
        # Get rect of proper size
        self.rect = pygame.Rect((0, 0), settings.powerup_dimensions)
        # Create precise value for y for precise float precision movement
        self.precise_y = 0.0
        # Randomize position on screen
        self.randomize_position()

    def draw(self):
        """Draws powerup to screen"""
        self.screen.blit(self.image, self.rect)

    def set_image(self):
        """Sets image based on the powerup's name string"""
        # Load image
        self.image = pygame.image.load(self.powerup_name + ".bmp")
        # Resize image based on settings
        self.image = pygame.transform.scale(
            self.image, self.settings.powerup_dimensions)
        # Convert image to most efficient format
        self.image = self.image.convert_alpha()

    def resize_to_icon(self):
        """Resizes powerup to icon for use in powerup dashboard"""
        # Resize image based on settings
        self.image = pygame.transform.scale(
            self.image, self.settings.powerup_icon_dimensions)
        # Convert image to most efficient format
        self.image = self.image.convert_alpha()

    def randomize_position(self):
        """Randmoizes powerup position in top portion of screen"""
        self.rect.left = randint(
            0, self.screen_rect.right - self.settings.powerup_width)
        self.rect.top = randint(0, self.settings.alien_start_space_y)
        self.precise_y = float(self.rect.y)

    def update(self):
        """Updates powerup position on screen"""
        self.precise_y += self.settings.powerup_speed
        self.rect.y = int(self.precise_y)

    def off_screen(self):
        """Returns true only if powerup has fallen off bottom of screen"""
        return self.rect.top > self.screen_rect.bottom

    def set_expiration_time(self):
        """Sets expiration time for powerup based on current time and powerup duration"""
        self.expiration_time = self.frame_counter.counter + self.duration

    def is_expired(self):
        """Returns true if game frame-time is greater than powerup expiration frame-time"""
        return self.frame_counter.counter > self.expiration_time


"""All powerups wiill be distinct classes inheriting from the powerup class
with their own defined functions to activate and dectivate their powerups"""


class DestroyoBullets(Powerup):
    """Class to represent destroyo_bullet powerup that allows ship to launch invincible bullets
    that are not removed on collision with aliens"""

    def __init__(self, settings, screen, stats, frame_counter):
        """Initializes destroyo_bullets object and powerup superclass"""
        # Initialize superclass
        super().__init__(settings, screen, stats, frame_counter)
        # Set powerupname which will act as key for powerup manager dictionary
        self.powerup_name = "destroyo_bullets"
        # Set and format proper image
        self.set_image()
        # Set duration
        self.duration = settings.destroyo_bullets_duration
        # Set expiration time
        self.set_expiration_time()

    def activate_powerup(self):
        """Activates destroyo_bullets"""
        # Set destroyo_bullet flag to true so bullets aren't removed on collision with aliens
        self.settings.destroyo_bullets = True
        # Change color of ship bullets to destroyo bullet color
        self.settings.ship_bullet_color = self.settings.destroyo_bullets_color

    def deactivate_powerup(self):
        """Deactivates destroyo_bullets"""
        # Set destroyo_bullet flag to false so bullets are removed on collision with aliens
        self.settings.destroyo_bullets = False
        # Change color of ship bullets to default
        self.settings.ship_bullet_color = self.settings.default_ship_bullet_color


class WidenedBullets(Powerup):
    """Class to represent powerup that makes bullets wider to hit more aliens"""

    def __init__(self, settings, screen, stats, frame_counter):
        """Initializes widened_bullets object and powerup superclass"""
        # Initialize superclass
        super().__init__(settings, screen, stats, frame_counter)
        # Set powerupname which will act as key for powerup manager dictionary
        self.powerup_name = "widened_bullets"
        # Set and format proper image
        self.set_image()
        # Set duration
        self.duration = settings.widened_bullets_duration
        # Set expiration time
        self.set_expiration_time()

    def activate_powerup(self):
        """Activates widened_bullets"""
        self.settings.ship_bullet_dimensions = self.settings.widened_bullets_dimensions

    def deactivate_powerup(self):
        """Deactivates widened_bullets"""
        self.settings.ship_bullet_dimensions = self.settings.default_bullet_dimensions


class SuperspeedBullets(Powerup):
    """Class to represent powerup that makes ship bullets super fast"""

    def __init__(self, settings, screen, stats, frame_counter):
        """Initializes superspeed_bullets object and powerup superclass"""
        # Initialize superclass
        super().__init__(settings, screen, stats, frame_counter)
        # Set powerupname which will act as key for powerup manager dictionary
        self.powerup_name = "superspeed_bullets"
        # Set and format proper image
        self.set_image()
        # Set duration
        self.duration = settings.superspeed_bullets_duration
        # Set expiration time
        self.set_expiration_time()

    def activate_powerup(self):
        """Activates superspeed_bullets"""
        # Activate flag so game knows to pause level_ups
        self.settings.superspeed_bullets = True
        # Create variable to hold current ship speed for when powerup finishes
        self.current_ship_bullet_speed = self.settings.ship_bullet_speed
        # Set bullet speed to super_speed
        self.settings.ship_bullet_speed = self.settings.bullet_superspeed

    def deactivate_powerup(self):
        """Deactivates superspeed_bullets"""
        # Deactivate flag so game knows to continue level_ups
        self.settings.superspeed_bullets = False
        # Set ship bullet speed back to what it was before powerup
        self.settings.ship_bullet_speed = self.current_ship_bullet_speed
        # Update all missed level ups that happened while powerup was active
        while self.settings.bullet_speed_upgrade_counter > 0:
            self.settings.level_up_ship_bullet_speed()
            self.settings.bullet_speed_upgrade_counter -= 1


class SuperspeedShip(Powerup):
    """Class to represent powerup that makes ship movement super fast"""

    def __init__(self, settings, screen, stats, frame_counter):
        """Initializes superspeed_ship object and powerup superclass"""
        # Initialize superclass
        super().__init__(settings, screen, stats, frame_counter)
        # Set powerupname which will act as key for powerup manager dictionary
        self.powerup_name = "superspeed_ship"
        # Set and format proper image
        self.set_image()
        # Set duration
        self.duration = settings.superspeed_ship_duration
        # Set expiration time
        self.set_expiration_time()

    def activate_powerup(self):
        """Activates superspeed_ship"""
        # Activate flag so game knows to pause level_ups
        self.settings.superspeed_ship = True
        # Create variable to hold current ship speed for when powerup finishes
        self.current_ship_speed = self.settings.ship_speed
        # Set ship speed to super_speed
        self.settings.ship_speed = self.settings.ship_superspeed

    def deactivate_powerup(self):
        """Deactivates superspeed_ship"""
        # Deactivate flag so game knows to continue level_ups
        self.settings.superspeed_ship = False
        # Set ship speed back to what it was before powerup
        self.settings.ship_speed = self.current_ship_speed
        # Update all missed level ups that happened while powerup was active
        while self.settings.ship_speed_upgrade_counter > 0:
            self.settings.level_up_ship_speed()
            self.settings.ship_speed_upgrade_counter -= 1


class UnlimitedBullets(Powerup):
    """Class to represent powerup that removes bullet firing limit"""

    def __init__(self, settings, screen, stats, frame_counter):
        """Initializes unlimited_bullets object and powerup superclass"""
        # Initialize superclass
        super().__init__(settings, screen, stats, frame_counter)
        # Set powerupname which will act as key for powerup manager dictionary
        self.powerup_name = "unlimited_bullets"
        # Set and format proper image
        self.set_image()
        # Set duration
        self.duration = settings.unlimited_bullets_duration
        # Set expiration time
        self.set_expiration_time()

    def activate_powerup(self):
        """Activates unlimited_bullets"""
        self.settings.unlimited_bullets = True

    def deactivate_powerup(self):
        """Deactivates unlimited_bullets"""
        self.settings.unlimited_bullets = False


class AlienBulletShields(Powerup):
    """Class to represent powerup that makes ship immune to alien bullets"""

    def __init__(self, settings, screen, stats, frame_counter):
        """Initializes alien_bullet_shields object and powerup superclass"""
        # Initialize superclass
        super().__init__(settings, screen, stats, frame_counter)
        # Set powerupname which will act as key for powerup manager dictionary
        self.powerup_name = "alien_bullet_shields"
        # Set and format proper image
        self.set_image()
        # Set duration
        self.duration = settings.alien_bullet_shields_duration
        # Set expiration time
        self.set_expiration_time()

    def activate_powerup(self):
        """Activates alien_bullet_shields"""
        self.settings.alien_bullet_shields = True

    def deactivate_powerup(self):
        """Deactivates alien_bullet_shields"""
        self.settings.alien_bullet_shields = False


class DoublePoints(Powerup):
    """Class to represent powerup that doubles point gains"""

    def __init__(self, settings, screen, stats, frame_counter):
        """Initializes double_points object and powerup superclass"""
        # Initialize superclass
        super().__init__(settings, screen, stats, frame_counter)
        # Set powerupname which will act as key for powerup manager dictionary
        self.powerup_name = "double_points"
        # Set and format proper image
        self.set_image()
        # Set duration
        self.duration = settings.double_points_duration
        # Set expiration time
        self.set_expiration_time()

    def activate_powerup(self):
        """Activates double_points"""
        # Activate flag so game knows to pause level_ups
        self.settings.double_points = True
        # Create variable to hold current ship speed for when powerup finishes
        self.current_alien_points = self.settings.alien_points
        # Set ship speed to super_speed
        self.settings.alien_points *= 2

    def deactivate_powerup(self):
        """Deactivates superspeed_ship"""
        # Deactivate flag so game knows to continue level_ups
        self.settings.double_points = False
        # Set ship speed back to what it was before powerup
        self.settings.alien_points = self.current_alien_points
        # Update all missed level ups that happened while powerup was active
        while self.settings.alien_points_upgrade_counter > 0:
            self.settings.level_up_alien_points()
            self.settings.alien_points_upgrade_counter -= 1
