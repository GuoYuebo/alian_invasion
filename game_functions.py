import sys
import pygame

from bullet import Bullet


def check_events(api_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_key_down_events(event, api_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_key_up_events(event, ship)


def check_key_down_events(event, api_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(bullets, api_settings, screen, ship)


def check_key_up_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_setting, screen, ship, bullets):
    screen.fill(ai_setting.bg_color)
    for bullet in bullets:
        bullet.draw_bullet()
    ship.draw_me()
    pygame.display.flip()


def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullets(bullets, api_settings, screen, ship):
    if len(bullets) < api_settings.bullets_allowed:
        new_bullet = Bullet(api_settings, screen, ship)
        bullets.add(new_bullet)

