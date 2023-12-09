import pygame
from pygame.sprite import Sprite 

# ai_game：屏幕参数
# get_rect()：获取面积， rect对象， 具有center、centerx 或 centery；要让游戏元素与屏幕边缘对齐，可使用属性 top、bottom、left 或 right。也可以组合使用
class Ship(Sprite):
    # 管理飞船的类
    def __init__(self, ai_game):
        super().__init__()
        # 优化帧率
        self.clock = pygame.time.Clock()
        self.dt = 0 

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像并获取其外接矩形。
        self.image = pygame.image.load('alien/images/ship.bmp') 
        self.rect = self.image.get_rect() 

        # 对于每艘新飞船，都将其放在屏幕底部的中央。
        self.rect.midbottom = self.screen_rect.midbottom 

        # 图片移动的状态
        self.moving_top = False
        self.moving_left = False
        self.moving_bottom = False
        self.moving_right = False

        # 窗口参数
        self.setting = ai_game.settings

        # 坐标？浮点数格式
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
    
    def update(self):
        # 根据移动标志调整飞船位置  并 判断坐标不出框
        if self.moving_top and self.rect.top > 0:
            self.y -= self.setting.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.setting.ship_speed 
        if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.setting.ship_speed 
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.setting.ship_speed
        self.rect.x = self.x 
        self.rect.y = self.y 
        # self.dt = self.clock.tick(1680) # 限制帧率




    def blitme(self):
        # 在指定位置绘制飞船   图像     位置
        self.screen.blit(self.image, self.rect) 

    # 将飞船放到屏幕底部中央
    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom 
        self.x = float(self.rect.x) # 更新一下自定义坐标
        self.y =  float(self.rect.x) 
        self.rect.x = self.x 
        self.rect.y = self.y 
        # print(self.rect.x, self.rect.y)