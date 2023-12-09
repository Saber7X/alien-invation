
#  跟踪游戏统计信息
class GameStats:
    def __init__(self, ai_game):
        # 初始化统计信息
        self.settings = ai_game.settings 
        self.reset_stats() 
        # 游戏刚启动时处于活动状态。
        self.game_active = False
        # 任何情况下都不应重置最高得分。 
        self.high_score = 0 
        # 等级
        self.level = 1

    def reset_stats(self):
        # 初始化游戏运行期间的可变信息
        self.ships_left = self.settings.ship_limit # 飞船数量（数量）
        self.score = 0 # 初始化得分为0
        self.level = 1 # 等级为1
