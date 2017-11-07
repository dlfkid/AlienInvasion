import sys
import pygame
from space_ship import SpaceShip
from game_setting import Settings
import game_functions as GAMEFUNCTION
from pygame.sprite import Group
from alien import Alien

def run_game():
    #创建setting对象，使用默认参数
    settingCenter = Settings()
    #声明一个元组获取屏幕参数
    screen_size = (settingCenter.screen_width,settingCenter.screen_height)
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Alien Invasion")

    #绘制一艘飞船
    ship = SpaceShip(screen,settingCenter)
    #创建一个用于储存子弹的编组
    bullets = Group()
    #创建一个用于储存外星人的编组
    aliens = Group()

    #创建一个外星人舰队
    GAMEFUNCTION.create_alien_fleet(settings=settingCenter,screen=screen,aliens=aliens,ship=ship)

    #开始游戏的主循环
    while True:
        #监控键盘和鼠标
        GAMEFUNCTION.check_events(ship=ship,settings=settingCenter,bullets=bullets,screen=screen)
        #更新飞船移动状态
        ship.update_move_state()
        #更新子弹位置
        GAMEFUNCTION.update_bullets(bullets = bullets)
        #更新外星人位置
        GAMEFUNCTION.update_aliens(aliens = aliens)
        #更新屏幕
        GAMEFUNCTION.update_screen(settingCenter,screen,ship,bullets,aliens)



run_game()

