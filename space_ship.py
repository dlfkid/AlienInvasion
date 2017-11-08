#宇宙飞船类

import pygame

class SpaceShip():
    def __init__(self,screen,settings):
        #飞船初始化并设置其位置
        self.screen = screen
        #加载飞船图像并获取其外界矩形
        self.image = pygame.image.load_basic("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.center = float(self.rect.centerx)
        self.middle = float(self.rect.centery)

        #移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_forward = False
        self.moving_backward = False

        #将每艘新飞船放在屏幕底部中央
        self.rect.centerx = int(settings.screen_width/2)
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        #在指定位置绘制飞船
        self.screen.blit(self.image,self.rect)

    def update_move_state(self):
        #更新飞船移动状态
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.settings.ship_speed_factor
        if self.moving_forward and self.rect.top > 0:
            self.middle -= self.settings.ship_speed_factor
        if self.moving_backward and self.rect.bottom < self.screen_rect.bottom:
            self.middle += self.settings.ship_speed_factor
        #根据center更新rect对象
        self.rect.centerx = self.center
        self.rect.centery = self.middle

    def replace_space_ship(self):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom