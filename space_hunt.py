import sys
import pygame
from settings import Settings
from ship import Ship
from game_stats import GameStats
import game_functions as gf
from button import Button
from scoreboard import Scoreboard
from frame_counter import FrameCounter
from powerup_manager import PowerupManager


def run_game():
    """Function that runs the whole game"""
    # Initialize pygame library
    pygame.init()
    # Create settings object
    settings = Settings()
    # Create framecounter to keep game "time"
    frame_counter = FrameCounter()
    frame_counter.tick()  # So game doesn't start on frame zero
    frame_counter.tick()  # So game doesn't start on frame zero
    # Create  game statistics object for changing came level variables
    stats = GameStats(settings)
    # Create game screen
    screen = pygame.display.set_mode(settings.screen_dimensions)
    # Set caption to game title
    pygame.display.set_caption("Space Hunt")
    # Create controlable player ship
    ship = Ship(settings, screen)
    # Create player scoreboard
    scoreboard = Scoreboard(settings, screen, stats)
    # Create Sprite group to contain bullets shot by ship
    bullets = pygame.sprite.Group()
    # Create Sprite group to contain aliens shot at by ship
    aliens = pygame.sprite.Group()
    # Create group for alien bullets
    alien_bullets = pygame.sprite.Group()
    # Create group for powerups falling on screen
    new_powerup_group = pygame.sprite.Group()
    # Powerup Manager for managing launch and ativation of powerups
    powerup_manager = PowerupManager(
        settings, screen, stats, new_powerup_group, frame_counter, scoreboard)
    # Create game start button
    start_button = Button(settings, screen, settings.button_start_text)

    while True:
        for event in pygame.event.get():
            gf.check_game_event(event, settings, screen, ship, bullets, alien_bullets,
                                start_button, stats, aliens, scoreboard, frame_counter, powerup_manager)

        if stats.game_active:
            ship.update()
            bullets.update()
            alien_bullets.update()
            aliens.update()
            new_powerup_group.update()
            gf.check_powerup_collisions(ship, powerup_manager)
            powerup_manager.handle_powerups()
            gf.check_dead_bullets(bullets, alien_bullets)
            gf.check_alien_side_collisions(aliens, settings)
            gf.check_alien_bullet_collisions(
                aliens, bullets, alien_bullets, settings, screen, stats, scoreboard)
            gf.check_fleet_victory(
                aliens, bullets, alien_bullets, ship, settings, screen, stats, scoreboard)
            gf.do_repeated_timed_actions(
                settings, screen, powerup_manager, alien_bullets, aliens, frame_counter)
            frame_counter.tick()
        # Draws all relevant game elements to screen
        gf.update_screen(settings, screen, ship, bullets, alien_bullets,
                         aliens, start_button, stats, scoreboard, powerup_manager)


run_game()
