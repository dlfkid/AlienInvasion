import sys
import pygame
from space_ship import SpaceShip
from game_setting import Settings
import space_ship

def run_game():
    #创建setting对象，使用默认参数
    settingCenter = Settings()
    #声明一个元组获取屏幕参数
    screen_size = (settingCenter.screen_width,settingCenter.screen_height)
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Alien Invasion")

    #设置背景颜色
    bg_color = settingCenter.bg_color

    #绘制一艘飞船
    ship = SpaceShip(screen)


    #开始游戏的主循环
    while True:
        #监控键盘和鼠标
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("QUIT command detected.")
                sys.exit()

        #每次循环都重绘屏幕
        screen.fill(bg_color)
        ship.blitme()
        #让绘制的屏幕可见®
        pygame.display.flip()

run_game()

