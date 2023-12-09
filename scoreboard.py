import pygame.font 
from pygame.sprite import Group 
from ship import Ship 
# 记分牌
class Scoreboard: 
    """显示得分信息的类。""" 
    def __init__(self, ai_game):
        """初始化显示得分涉及的属性。""" 
        
        self.ai_game = ai_game 

        self.screen = ai_game.screen  # 窗口
        self.screen_rect = self.screen.get_rect()  # 窗口参数
        self.settings = ai_game.settings  # 设置参数
        self.stats = ai_game.stats  # 游戏数据
        # 显示得分信息时使用的字体设置。
        self.text_color = (30, 30, 30) # 字体颜色
        self.font = pygame.font.SysFont(None, 48)  # 字体大小
        # 准备初始得分图像。
        self.prep_score() 
        # 准备最高分图像
        self.prep_high_score()
        # 准备等级图像
        self.prep_level()
        # 绘制剩余飞船
        self.prep_ships()
    def prep_score(self): 
        """将得分转换为一幅渲染的图像。""" 
        # 获取更新的分数
        rounded_score = round(self.stats.score, -1) # 保留到小数点后-1为，即十位
        score_str = "{:,}".format(rounded_score) # 固定格式，数字转字符串时加入逗号
        self.score_image = self.font.render(score_str, True,
            self.text_color, self.settings.bg_color)  # 创建文字图片
        # 在屏幕右上角显示得分。
        self.score_rect = self.score_image.get_rect() # 获取上图的参数
        self.score_rect.right = self.screen_rect.right - 20 # 指定位置，距离右边20
        self.score_rect.top = 20 # 距离上面20

    # 绘制最高分图像
    def prep_high_score(self): 
        """将得分转换为一幅渲染的图像。""" 
        # 获取更新的分数
        high_score = round(self.stats.high_score, -1) # 保留到小数点后-1为，即十位
        high_score_str = "{:,}".format(high_score) # 固定格式，数字转字符串时加入逗号
        self.high_score_image = self.font.render(high_score_str, True,
            self.text_color, self.settings.bg_color)  # 创建文字图片
        # 在屏幕顶部中央显示得分。
        self.high_score_rect = self.high_score_image.get_rect() # 获取上图的参数
        self.high_score_rect.midtop = self.screen_rect.midtop # 指定位置，距离右边20  
    
    def check_high_score(self): 
        """检查是否诞生了新的最高得分。""" 
        if self.stats.score > self.stats.high_score: 
            self.stats.high_score = self.stats.score 
            self.prep_high_score() # 不断更新

    def show_score(self): 
        """在屏幕上显示得分。""" 
        self.screen.blit(self.score_image, self.score_rect) # 画图片
        self.screen.blit(self.high_score_image, self.high_score_rect)# 画最高分图片
        self.screen.blit(self.level_image, self.level_rect)  # 画等级
        self.ships.draw(self.screen) 

    def prep_level(self): 
        """将等级转换为渲染的图像。""" 
        level_str = str(self.stats.level) # 获取等级
        self.level_image = self.font.render(level_str, True,
        self.text_color, self.settings.bg_color)  # 转为图像
        # 将等级放在得分下方。
        self.level_rect = self.level_image.get_rect() # 获取图像大小
        self.level_rect.right = self.score_rect.right # 放在得分下面
        self.level_rect.top = self.score_rect.bottom + 10 
    
    def prep_ships(self): 
        """显示还余下多少艘飞船。""" 
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game) 
            ship.rect.x = 10 + ship_number * ship.rect.width 
            ship.rect.y = 10 
            self.ships.add(ship) 