#宇宙飞船类

import pygame

class SpaceShip():
    def __init__(self,screen):
        #飞船初始化并设置其位置
        self.screen = screen
        #加载飞船图像并获取其外界矩形
        self.image = pygame.image.load_basic("image/spaceship.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        #在指定位置绘制飞船
        self.screen.blit(self.image,self.rect)