import pygame
from pygame.sprite import Sprite # 可以同时操作很多元素

# 继承Sprite
class Bullet(Sprite):
    # 管理子弹

    def __init__(self, ai_game):
        super().__init__() # 我想继承它的作用应该就是为了方便存储在他的group里面
        # 在飞船的位置创建一个子弹对象
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # 在(0,0)处创建一个表示子弹的矩形，再设置正确的位置。
        # 感觉是直接创建了一个rect对象,由于是自建,所以无需get
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop # 与飞机顶部中间对齐
        
        # 存储用小数表示的子弹位置。
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

        
   
    def update(self):
        # 向上移动子弹
        # 更新子弹坐标
        self.y -= self.settings.bullet_speed
    # 更新为浮点数
        self.rect.y = self.y
    
    def draw_bullet(self):
        # 绘制子弹
        pygame.draw.rect(self.screen, self.color, self.rect)
    

class Bullet2(Sprite):
    # 管理子弹

    def __init__(self, ai_game):
        super().__init__() # 我想继承它的作用应该就是为了方便存储在他的group里面
        # 在飞船的位置创建一个子弹对象
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # 在(0,0)处创建一个表示子弹的矩形，再设置正确的位置。
        # 感觉是直接创建了一个rect对象,由于是自建,所以无需get
        self.rect1 = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height) # 上
        self.rect2 = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)# 下

        # 左右
        self.rect3 = pygame.Rect(0, 0, self.settings.bullet_height, self.settings.bullet_width)
        self.rect4 = pygame.Rect(0, 0, self.settings.bullet_height, self.settings.bullet_width)

        self.rect1.midtop = ai_game.ship.rect.midtop # 与飞机顶部中间对齐
        self.rect2.midtop = ai_game.ship.rect.midbottom # 与飞机顶部中间对齐
        self.rect3.midtop = ai_game.ship.rect.midleft # 与飞机顶部中间对齐
        self.rect4.midtop = ai_game.ship.rect.midright # 与飞机顶部中间对齐
        
        # 存储用小数表示的子弹位置。
        self.y1 = float(self.rect1.y)
        self.x1 = float(self.rect1.x)

        self.y2 = float(self.rect2.y)
        self.x2 = float(self.rect2.x)

        self.y3 = float(self.rect3.y)
        self.x3 = float(self.rect3.x)

        self.y4 = float(self.rect4.y)
        self.x4 = float(self.rect4.x)

        
   
    def update(self):
        # 向上移动子弹
        # 更新子弹坐标
        self.y1 -= self.settings.bullet_speed
    # 更新为浮点数
        self.rect1.y = self.y1

        self.y2 += self.settings.bullet_speed
    # 更新为浮点数
        self.rect2.y = self.y2

        self.x3 -= self.settings.bullet_speed
    # 更新为浮点数
        self.rect3.x = self.x3

        self.x4 += self.settings.bullet_speed
    # 更新为浮点数
        self.rect4.x = self.x4
    
    def draw_bullet(self):
        # 绘制子弹
        pygame.draw.rect(self.screen, self.color, self.rect1)
        pygame.draw.rect(self.screen, self.color, self.rect2)
        pygame.draw.rect(self.screen, self.color, self.rect3)
        pygame.draw.rect(self.screen, self.color, self.rect4)