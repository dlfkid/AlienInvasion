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
        self.x += self.settings.enemy_speed
        self.rect.x = self.x