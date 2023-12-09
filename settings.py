class settings:
    def __init__(self):
        """初始化游戏的设置。""" 
        # 记分
        self.alien_points = 50 # 一个外星人多少分
        self.score_scale = 1.5# 外星人分数的提高速度。

        # 屏幕设置
        self.screen_width = 0 
        self.screen_height = 0 
        self.bg_color = (230, 230, 230) 

        # 飞船设置
        self.ship_speed = 1.1 # 速度
        self.ship_limit = 3 # 飞船数量（生命）

        # 子弹设置  
        self.bullet_fire_speed = 50.0 # 子弹间隔距离,越大越疏,小小越密
        self.bullet_speed = 1.5  # 速度
        self.bullet_width = 3  # 长度
        self.bullet_height = 15 # 高度
        self.bullet_color = (60, 60, 60) # 颜色
        self.bullets_allowed = 30 # 存储子弹的数量

        # 外星人设置
        self.alien_speed = 1.0 
        self.fleet_drop_speed = 5 # 撞墙后向下的移动速度
        self.fleet_direction = 1 # 方向：1 表示向右移，为-1 表示向左移。
        

        # 加快游戏节奏的速度。
        self.speedup_scale = 1.1 # 玩家每升一级后提升的难度
        self.initialize_dynamic_settings() # 初始化游戏参数



    def initialize_dynamic_settings(self): 
        """初始化随游戏进行而变化的设置。""" 
        self.ship_speed = 1.5 
        self.bullet_speed = 3.0 
        self.alien_speed = 1.0 
        # fleet_direction 为 1 表示向右，为-1 表示向左。
        self.fleet_direction = 1

    def increase_speed(self): 
        """提高速度设置""" 
        self.ship_speed *= self.speedup_scale  # 增加指定参数
        self.bullet_speed *= self.speedup_scale 
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale) # 随着难度提升，外星人的分数也越来越高
        # print(self.alien_points) 