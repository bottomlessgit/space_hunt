"""A module for functions game-level functions, handling user input,
sprite group interactions, and sprite collisions"""
import sys
import pygame
import random
from alien import Alien
from bullet import Bullet
from alien_bullet import AlienBullet
from powerups import Powerup


def check_game_event(event, settings, screen, ship, bullets, alien_bullets,
                     start_button, stats, aliens, scoreboard, frame_counter, powerup_manager):
    """Handles user input events"""
    # Handle pressing quit button
    if event.type == pygame.QUIT:
        quit_game(stats)
    # Handle user keypresses
    elif event.type == pygame.KEYDOWN:
        check_keydown_event(event, settings, screen, ship, bullets, alien_bullets,
                            stats, aliens, scoreboard, frame_counter, powerup_manager)
    # Handle user key releases
    elif event.type == pygame.KEYUP:
        check_keyup_events(event, ship)
    # Handle user mouseclicks
    elif event.type == pygame.MOUSEBUTTONDOWN:
        if not stats.game_active:
            check_button_clicked(event, start_button, stats, settings, screen, ship,
                                 bullets, alien_bullets, aliens, scoreboard, powerup_manager, frame_counter)


def check_keydown_event(event, settings, screen, ship, bullets, alien_bullets,
                        stats, aliens, scoreboard, frame_counter, powerup_manager):
    """Handles keydown events"""
    # Handle ship movement
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    # Handle bullet launches
    elif event.key == pygame.K_SPACE and stats.game_active:
        if len(bullets) < settings.bullet_limit or settings.unlimited_bullets:
            bullets.add(Bullet(settings, screen, ship))
    # Handle start of game using p key
    elif event.key == pygame.K_p and not stats.game_active:
        reset_game(settings, screen, ship, bullets, alien_bullets,
                   aliens, stats, scoreboard, powerup_manager, frame_counter)
        stats.game_active = True
    # Handle quitting using q key
    elif event.key == pygame.K_q:
        quit_game(stats)


def check_keyup_events(event, ship):
    """Handles keyup events"""
    # Handle stopping of ship movements
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_mousbuttondown_events(event, settings, screen, ship, bullets,
                                start_button, stats, aliens, scoreboard):
    """Handles mouseclickdown events"""
    if not stats.game_active:
        check_button_clicked(event, start_button, stats,
                             settings, screen, ship, bullets, aliens, scoreboard)


def create_fleet(settings, screen, aliens):
    """Creates new fleet of aliens positioned at top left corner of screen"""
    # Calculate total alien space in x and y axes and add to position for each loop
    alien_x = 0
    alien_y = 0
    total_alien_width = settings.alien_width + settings.alien_spacing_x
    total_alien_height = settings.alien_height + settings.alien_spacing_y
    for row in range(settings.num_rows_in_fleet):
        for col in range(settings.num_aliens_in_row):
            # Add alien to fleet group
            aliens.add(create_alien(settings, screen, alien_x, alien_y))
            # Change alien_x coordinate
            alien_x += total_alien_width
        # Change alien_y coordinate
        alien_y += total_alien_height
        # Reset alien_x coordinate for new row
        alien_x = 0


def create_alien(settings, screen, alien_x, alien_y):
    """Creates a new alien at the given coordinates"""
    # Create alien
    new_alien = Alien(settings, screen)
    # Set rect coordinates
    new_alien.rect.x = alien_x
    new_alien.rect.y = alien_y
    # Set precise coordinates
    new_alien.precise_x = float(new_alien.rect.x)
    new_alien.precise_y = float(new_alien.rect.y)
    return new_alien


def launch_alien_bullets(settings, screen, alien_bullets, aliens):
    """Launches random number of alien bullets from random aliens in fleet"""
    if random.randint(0, settings.alien_bullet_launch_frequency - 1) == 0:
        # Set number of bullets fired between 0 and max allowed
        num_bullets = random.randint(0, settings.max_alien_bullets)
        # Now choose random aliens to shoot bullets from
        alien_list = aliens.sprites()
        num_aliens = len(alien_list)
        for num_bullet in range(num_bullets):
            rand_alien = random.choice(alien_list)
            alien_bullets.add(AlienBullet(settings, screen, rand_alien))


def do_repeated_timed_actions(settings, screen, powerup_manager, alien_bullets,
                              aliens, frame_counter):
    """Launches alien bullets and powerups at regular intervals"""
    # First check if alien bullet launch required
    if frame_counter.counter % settings.frames_per_alien_bullet_launch == 0:
        launch_alien_bullets(settings, screen, alien_bullets, aliens)
    # Then check if Powerup launch required
    if frame_counter.counter % settings.frames_per_powerup_launch == 0:
        powerup_manager.launch_powerups()


def check_alien_side_collisions(aliens, settings):
    """Checks if any alien hits side of screen and reverses fleet direction
    and moves the fleet downwards if so"""
    for alien in aliens:
        if alien.hit_side():
            # Reverse direction
            settings.alien_x_speed *= -1
            # Move fleet down
            move_fleet_down(aliens)
            # Now break as not to repeat as one side collision is enough
            break


def move_fleet_down(aliens):
    """Moves fleet down the screen"""
    for alien in aliens:
        alien.move_down_screen()


def check_alien_bullet_collisions(aliens, bullets, alien_bullets, settings,
                                  screen, stats, scoreboard):
    """Checks for alien bullet collisions"""
    # Remove collided elements
    collisions = pygame.sprite.groupcollide(
        bullets, aliens, not settings.destroyo_bullets, True, pygame.sprite.collide_mask)
    # Increase score based on number of aliens killed
    if collisions:
        for alien_list in collisions.values():
            stats.score_increase(len(alien_list))
        scoreboard.refresh_score_surface()
    # If fleet is empty call function to load next level
    if len(aliens) == 0:
        fleet_defeat(aliens, bullets, alien_bullets,
                     settings, screen, stats, scoreboard)


def fleet_defeat(aliens, bullets, alien_bullets, settings, screen, stats,
                 scoreboard):
    """Starts the next level if fleet of aliens is defeated"""
    # Empty screen of ship bullets
    bullets.empty()
    # alien_bullets.empty()
    # Set up scoreboard and settings for next level
    settings.next_level()
    stats.level += 1
    scoreboard.refresh_level_surface()
    # Create a new fleet
    create_fleet(settings, screen, aliens)


def check_fleet_victory(aliens, bullets, alien_bullets, ship, settings, screen,
                        stats, scoreboard):
    """Checks if alien collided with ship or bottom of screen
    and responds accordingly"""
    if (fleet_bottom_collision(aliens)
        or pygame.sprite.spritecollide(ship, aliens, False, pygame.sprite.collide_mask)
        or (pygame.sprite.spritecollide(ship, alien_bullets, True, pygame.sprite.collide_mask)
            and not settings.alien_bullet_shields)):
        stats.lives -= 1
        scoreboard.refresh_lives_surface()
        # Check if game is over because all lives lost and stop game if so
        if stats.lives == 0:
            stats.game_active = False
            stats.set_high_score()
        # If game not over restart level
        else:
            bullets.empty()
            aliens.empty()
            alien_bullets.empty()
            create_fleet(settings, screen, aliens)


def fleet_bottom_collision(aliens):
    """Returns true if any alien hits the bottom of the screen"""
    for alien in aliens:
        if alien.hit_bottom():
            return True
    return False


def update_screen(settings, screen, ship, bullets, alien_bullets, aliens,
                  start_button, stats, scoreboard, powerup_manager):
    """Updates screen based on game state"""
    screen.fill(settings.screen_color)
    # Draw game elements
    ship.blitme()
    aliens.draw(screen)
    powerup_manager.new_powerup_group.draw(screen)
    for bullet in bullets:
        bullet.draw()
    for alien_bullet in alien_bullets:
        alien_bullet.draw()
    # Draw scoreboard and powerup dashboard
    scoreboard.draw()
    powerup_manager.draw_powerup_board()
    # If game inactive draw start button
    if not stats.game_active:
        start_button.blitme()
    # Load drawn screen from pygame buffer
    pygame.display.flip()


def check_button_clicked(event, start_button, stats, settings, screen, ship,
                         bullets, alien_bullets, aliens, scoreboard, powerup_manager, frame_counter):
    """Sets game_active to true if start button clicked"""
    if start_button.rect.collidepoint(event.pos):
        reset_game(settings, screen, ship, bullets, alien_bullets,
                   aliens, stats, scoreboard, powerup_manager, frame_counter)
        stats.game_active = True


def check_powerup_collisions(ship, powerup_manager):
    """Checks if ship gets powerups and activates given powerups"""
    new_powerup_list = pygame.sprite.spritecollide(
        ship, powerup_manager.new_powerup_group, True, pygame.sprite.collide_mask)
    for new_powerup in new_powerup_list:
        powerup_manager.add_powerup(new_powerup)


def check_dead_bullets(bullets, alien_bullets):
    """Removes bullets that have gone off screen"""
    # First remove ship bullets
    for bullet in bullets:
        if bullet.off_screen():
            bullets.remove(bullet)
    # Then remove alien bullets
    for alien_bullet in alien_bullets:
        if alien_bullet.off_screen():
            alien_bullets.remove(alien_bullet)


def reset_game(settings, screen, ship, bullets, alien_bullets, aliens, stats,
               scoreboard, powerup_manager, frame_counter):
    """Resets all game elements to starting positions and values"""
    ship.initialize_ship_position()
    stats.reset_stats()
    bullets.empty()
    aliens.empty()
    alien_bullets.empty()
    powerup_manager.reset()
    create_fleet(settings, screen, aliens)
    scoreboard.refresh()
    frame_counter.reset_counter()
    settings.set_default_settings()


def quit_game(stats):
    """Loads high score into file and quits game"""
    stats.set_high_score()
    stats.save_high_score()
    sys.exit()
