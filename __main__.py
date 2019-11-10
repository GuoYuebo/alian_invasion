import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()

    api_settings = Settings()

    screen = pygame.display.set_mode((api_settings.screen_width, api_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(api_settings, screen)
    bullets = Group()

    # 开始游戏的主循环
    while True:
        gf.check_events(api_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(api_settings, screen, ship, bullets)


if __name__ == "__main__":
    run_game()
