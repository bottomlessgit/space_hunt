class Settings():
    """Class made to keep track of and access static and changing game settings"""

    # First static settings are listed grouped by game element:

    # Screen settings
    def __init__(self):
        """Initialize settings object"""
        # Default bullet dimensions
        self.default_bullet_dimensions = (
            self.bullet_width, self.bullet_height) = (4, 20)
        # Screen settings
        self.screen_dimensions = self.screen_width, self.screen_height = 1400, 800
        self.screen_color = (0, 0, 0)
        # Ship settings
        self.ship_filename = "images/ship.bmp"
        self.ship_dimensions = (self.ship_width, self.ship_height) = (60, 100)
        # Ship Bullet settings
        self.default_ship_bullet_color = (150, 0, 0)
        self.ship_bullet_dimensions = self.default_bullet_dimensions
        self.ship_bullet_color = self.default_ship_bullet_color
        # Alien settings
        self.alien_filename = "images/alien.bmp"
        self.alien_dimensions = (
            self.alien_width, self.alien_height) = (40, 40)
        self.alien_bullet_color = (0, 200, 150)
        self.alien_bullet_dimensions = self.default_bullet_dimensions
        self.max_alien_bullets = 7
        # Alien fleet settings
        self.alien_spacing_x = 30
        self.alien_spacing_y = 30
        self.alien_start_space_x = 400  # Initial space between screen right and alien fleet
        # Initial space between screen bottom and alien fleet
        self.alien_start_space_y = 400
        self.num_aliens_in_row = self.calculate_num_aliens_in_row()
        self.num_rows_in_fleet = self.calculate_num_rows_in_fleet()
        # Button settings
        self.button_dimensions = (
            self.button_width, self.button_height) = (300, 250)
        self.button_color = (120, 140, 120)
        self.button_text_color = (20, 0, 20)
        self.button_text_size = 60
        self.button_start_text = "START"
        # Scoreboard settings
        self.scoreboard_font_size = 40
        self.scoreboard_text_color = (100, 200, 100)
        self.life_emblem_dimensions = (
            self.life_emblem_width, self.life_emblem_height) = (30, 50)
        # Powerup settings
        self.powerup_dimensions = (
            self.powerup_width, self.powerup_height) = (60, 60)

        # General game settings
        self.lives = 3  # Number of lives
        self.starting_alien_points = 1000

        # Set starting and maximum values for Settings that change every level:
        # Ship settings
        self.starting_ship_speed = 1.7
        self.maximum_ship_speed = self.ship_width / \
            2  # Can't go more than halfway off screen
        # Bullet setting
        self.starting_bullet_speed = 2.5
        self.maximum_ship_bullet_speed = self.alien_height - 1  # Can't skip alien
        # Alien settings
        self.starting_alien_x_speed = 0.5
        self.maximum_alien_x_speed = self.alien_width - 1  # Can't go off screen
        self.starting_alien_y_speed = 6.0
        self.maximum_alien_y_speed = self.ship_height - 1  # Can't skip ship
        self.starting_alien_points = 100
        self.starting_alien_bullet_speed = -.8
        self.maximum_alien_bullet_speed = -1 * self.ship_height - 1  # Can't skip ship
        # Powerup object settings
        self.starting_powerup_speed = .7
        self.maximum_alien_y_speed = self.ship_height - 1  # Can't skip ship
        self.starting_destroyo_bullets = False
        # Powerup dashboard settings
        self.powerup_icon_dimensions = (
            self.powerup_icon_width, self.powerup_icon_height) = (80, 80)
        self.powerup_icon_x_dist = 5
        self.powerup_icon_y_dist = 5

        # Fleet defeat settings changes
        self.ship_speed_increase_factor = 1.05
        self.ship_bullet_speed_increase_factor = 1.05
        self.alien_x_speed_increase_factor = 1.03
        self.alien_y_speed_increase_factor = 1.05
        self.alien_points_increase_factor = 1.1
        self.alien_bullet_speed_increase_factor = 1.02
        self.powerup_speed_increase_factor = 1.03

        # Powerup settings and default values for settings changed by powerups:
        self.standard_powerup_duration = 5000
        self.max_powerups_launched = 3

        # Powerup 1 : Deathless "destroyo" bullets
        self.destroyo_bullets_color = (200, 0, 200)
        self.destroyo_bullets_duration = self.standard_powerup_duration

        # Powerup 2: Widened bullets
        self.widened_bullets_width = 400
        self.widened_bullets_dimensions = (
            self.widened_bullets_width, self.bullet_height)
        self.widened_bullets_duration = self.standard_powerup_duration

        # Powerup 3: Super-speed bullets (can't be greater speed than alien height)
        self.superspeed_bullets = False
        self.bullet_superspeed = self.alien_height - 1
        self.superspeed_bullets_duration = self.standard_powerup_duration
        self.bullet_speed_upgrade_counter = 0

        # Powerup 4: Unlimited bullets
        self.bullet_limit = 4
        self.unlimited_bullets = False  # Needs to be reinitialized
        self.unlimited_bullets_duration = self.standard_powerup_duration

        # Powerup 5: Super-speed ship
        self.superspeed_ship = False
        self.ship_superspeed = self.maximum_ship_speed / 4
        self.superspeed_ship_duration = self.standard_powerup_duration
        # Counter to count upgrades missed while powerup in effect
        self.ship_speed_upgrade_counter = 0

        # Powerup 6: Alien bullet Shields
        self.alien_bullet_shields = False
        self.alien_bullet_shields_duration = self.standard_powerup_duration

        # Powerup 7: Double points
        self.double_points = False
        self.double_points_duration = self.standard_powerup_duration
        self.alien_points_upgrade_counter = 0

        # Powerup 8: Extra life
        # IMPLEMENT LATER

        # Event frame waittimes
        # How many frames until alien bullet launch
        self.frames_per_alien_bullet_launch = 500
        self.frames_per_powerup_launch = 800  # How many frames until powerup launch
        # Event fractional probability denominators
        self.alien_bullet_launch_frequency = 2
        self.powerup_launch_frequency = 3

        # Now initialize default values for non-static settings
        self.set_default_settings()

    # Assistive functions

    def calculate_num_aliens_in_row(self):
        """Function to calculate initial number of columns of aliens in fleet"""
        alien_row_space = self.screen_width - \
            self.alien_start_space_x + self.alien_spacing_x
        width_per_alien = self.alien_width + self.alien_spacing_x
        num_aliens_in_row = alien_row_space // width_per_alien
        return num_aliens_in_row

    def calculate_num_rows_in_fleet(self):
        """Function to calculate initial number of rows of aliens in fleet"""
        alien_col_space = self.screen_height - self.alien_start_space_y
        height_per_alien = self.alien_height + self.alien_spacing_y
        num_rows_in_fleet = alien_col_space // height_per_alien
        return num_rows_in_fleet

    # Functions for resetting and changing non-static settings:

    def set_default_settings(self):
        """Initializes and reinitializes default values for settings that 
        change during gameplay"""
        # Ship settings
        self.ship_speed = self.starting_ship_speed
        # Bullet setting
        self.ship_bullet_speed = self.starting_bullet_speed
        # Alien settings
        self.alien_x_speed = self.starting_alien_x_speed
        self.alien_y_speed = self.starting_alien_y_speed
        self.alien_points = self.starting_alien_points
        self.alien_bullet_speed = self.starting_alien_bullet_speed
        # Powerup settings
        self.powerup_speed = self.starting_powerup_speed

        self.destroyo_bullets = False

    def next_level(self):
        """Changes changing game settings in response to fleet defeat"""
        # Only level up ship movement speed if superspeed powerup not active
        if self.superspeed_ship:
            self.ship_speed_upgrade_counter += 1
        else:
            self.level_up_ship_speed()
        # Only level up ship bullet speed if superspeed powerup not active
        if self.superspeed_bullets:
            self.bullet_speed_upgrade_counter += 1
        else:
            self.level_up_ship_bullet_speed()
        # Level up alien movement and shooting speed
        self.level_up_alien_x_speed()
        self.level_up_alien_y_speed()
        self.level_up_alien_bullet_speed()
        # Only level up points if double_points powerup not active
        if self.double_points:
            self.alien_points_upgrade_counter += 1
        else:
            self.level_up_alien_points()

    """Split each level upgrade into a distinct function so if they're locked
    by a powerup they can be updated once the powerup loses effect"""

    def level_up_ship_speed(self):
        """Levels up ship_speed if appropriate"""
        if (self.ship_speed * self.ship_speed_increase_factor
                < self.maximum_ship_speed):
            self.ship_speed *= self.ship_speed_increase_factor

    def level_up_ship_bullet_speed(self):
        """Levels up ship_bullet_speed if appropriate"""
        if (self.ship_bullet_speed * self.ship_bullet_speed_increase_factor
                < self.maximum_ship_bullet_speed):
            self.ship_bullet_speed *= self.ship_bullet_speed_increase_factor

    def level_up_alien_x_speed(self):
        """Levels up alien_x_speed if appropriate"""
        if (self.alien_x_speed * self.alien_x_speed_increase_factor
                < self.maximum_alien_x_speed):
            self.alien_x_speed *= self.alien_x_speed_increase_factor

    def level_up_alien_y_speed(self):
        """Levels up alien_y_speed if appropriate"""
        if (self.alien_y_speed * self.alien_y_speed_increase_factor
                < self.maximum_alien_y_speed):
            self.alien_y_speed *= self.alien_y_speed_increase_factor

    def level_up_alien_points(self):
        """Levels up alien_points if appropriate"""
        self.alien_points = int(
            self.alien_points * self.alien_points_increase_factor) + 1

    def level_up_alien_bullet_speed(self):
        """Levels up alien_bullet_speed if appropriate"""
        if (self.alien_bullet_speed * self.alien_bullet_speed_increase_factor
                > self.maximum_alien_bullet_speed):
            self.alien_bullet_speed *= self.alien_bullet_speed_increase_factor
