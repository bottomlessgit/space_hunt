from powerups import *
from random import randint, sample
import pygame


class PowerupManager():
    """Manages active powerups, and prints powerup info to screen"""

    def __init__(self, settings, screen, stats, new_powerup_group,
                 frame_counter, scoreboard):
        """Initializes powerupmanager object"""
        # Give access to settings for powerup creation and activation
        self.settings = settings
        # Set screen to print powerups and dashboard too
        self.screen = screen
        self.screen_rect = screen.get_rect()
        # Set stat item for powerup creation
        self.stats = stats
        # Give access to frame counter for powerup creation and expiration
        self.frame_counter = frame_counter
        # Give access to scoreboard for positioning dashboard
        self.scoreboard = scoreboard
        # Make list for randomization of powerups
        self.powerup_list = [
            DestroyoBullets,
            WidenedBullets,
            SuperspeedBullets,
            SuperspeedShip,
            UnlimitedBullets,
            AlienBulletShields,
            DoublePoints,
        ]
        # Give access to powerup group for producing powerups in-game
        self.new_powerup_group = new_powerup_group

        # Make dictionary to keep track of active powerups
        # Dictionary keys will be powerup name
        self.active_powerup_dict = {}

        # Now make powerup status board that prints which powerups are active
        self.create_powerup_board()

    def create_powerup_board(self):
        """Sets up powerup dashboard"""
        num_powerups = len(self.powerup_list)
        dashboard_width = self.settings.powerup_icon_width * \
            2 + self.settings.powerup_icon_x_dist
        dashboard_height = (self.settings.powerup_icon_height +
                            self.settings.powerup_icon_y_dist) * (num_powerups + 1) // 2
        self.dashboard_rect = pygame.Rect(
            self.screen_rect.left,
            self.scoreboard.lives_image_rect.bottom,
            dashboard_width, dashboard_height)
        current_top = self.dashboard_rect.top

        self.icon_dict = {}

        for powerup_num in range(num_powerups):
            new_powerup_class = self.powerup_list[powerup_num]
            new_powerup_icon = new_powerup_class(
                self.settings, self.screen, self.stats, self.frame_counter)
            self.icon_dict[new_powerup_icon.powerup_name] = new_powerup_icon
            new_powerup_icon.resize_to_icon()
            new_powerup_icon.rect.left = self.dashboard_rect.left + \
                (powerup_num % 2) * (self.settings.powerup_icon_width +
                                     self.settings.powerup_icon_x_dist)
            new_powerup_icon.rect.top = self.dashboard_rect.top + \
                (powerup_num // 2) * (self.settings.powerup_icon_height +
                                      self.settings.powerup_icon_y_dist)

    def draw_powerup_board(self):
        """Draws powerup dashboard to screen"""
        for key in self.active_powerup_dict.keys():
            self.icon_dict[key].draw()

    def reset(self):
        """Resets the powerup manager for a new game"""
        # Remove all falling powerups from screen
        self.new_powerup_group.empty()
        # Deactivate all active powerups
        for key, powerup in self.active_powerup_dict.items():
            powerup.deactivate_powerup()
        # Clear out all active powerups from active powerup dictionary
        self.active_powerup_dict.clear()

    def add_powerup(self, powerup):
        """Adds a powerup to active list if new, resets timer if already active"""
        key = powerup.powerup_name
        # If powerup is already active just reset timer
        if key in self.active_powerup_dict:
            self.active_powerup_dict[key].set_expiration_time()
        else:
            powerup.activate_powerup()
            self.active_powerup_dict[key] = powerup

    def remove_expired_powerups(self):
        """Removes powerups that have expired"""
        expired_list = []  # List of expired powerup keys
        for key, powerup in self.active_powerup_dict.items():
            if powerup.is_expired():
                print("REMOVING: " + powerup.powerup_name)  # TEST!!!
                powerup.deactivate_powerup()
                expired_list.append(key)

        for key in expired_list:
            del self.active_powerup_dict[key]

    def remove_dead_powerups(self):
        """Removes powerups that have gone off screen"""
        for powerup in self.new_powerup_group:
            if powerup.off_screen():
                self.new_powerup_group.remove(powerup)

    def launch_powerups(self):
        """Adds a random number of powerups to the game if any"""
        if randint(1, self.settings.powerup_launch_frequency) == 1:
            # Use randint twice to make lower numbers substantially more likely
            num_powerups_added = randint(1, randint(
                1, self.settings.max_powerups_launched))
            # Use sample to take random sampling of distinct elements from powerup_list
            new_powerups = sample(self.powerup_list, num_powerups_added)
            # Now instantiate and add each powerup from the list of classes
            for new_powerup in new_powerups:
                self.new_powerup_group.add(new_powerup(
                    self.settings, self.screen, self.stats, self.frame_counter))

    def handle_powerups(self):
        """Removes all redundant powerups"""
        self.remove_dead_powerups()
        self.remove_expired_powerups()
