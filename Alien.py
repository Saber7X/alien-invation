import pygame
from pygame.sprite import Sprite

# 表示外星人的类
class Alien(Sprite):
    def __init__(self, ai_game):
        # 初始化外星人并设置起始位置
        super().__init__()

        # # 帧率优化
        # self.clock = pygame.time.Clock()
        # self.dt = 0 

        # 设置参数
        self.screen = ai_game.screen
        self.settings = ai_game.settings # 移动速度

        # 加载外星人图像，并设置rect属性
        self.image = pygame.image.load('alien/images/alien.bmp') 
        self.rect = self.image.get_rect() 

        # 每个外星人最初都在屏幕左上角附近。
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的精确水平位置。
        self.x = float(self.rect.x)

    
    def update(self):
        # 向右或右移动外星人
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
    
    # 检查是否到达边缘
    def check_edges(self):
        screen_rect = self.screen.get_rect() 
        if self.rect.right >= screen_rect.right or self.rect.left <= 0: # 判断到边缘
            return True