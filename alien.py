import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self,screen,settings):
        super().__init__()
        self.screen = screen
        self.settings = settings
        #加载外星人图像，并设置其矩形边框
        self.image = pygame.image.load_basic("images/alien.bmp")
        self.rect = self.image.get_rect()

        #每个外星人的初始位置
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        #储存外星人的准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        #在指定位置绘制外星人
        self.screen.blit(self.image,self.rect)
        print(str(self.settings))

    def update(self):
        #向右移动外星人
        self.x += self.settings.enemy_speed * self.settings.fleet_direction
        self.rect.x = self.x

    #检查外星人是否碰到了屏幕边缘
    def is_reach_edge(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        else:
            return False
