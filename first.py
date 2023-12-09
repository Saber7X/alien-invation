import pygame, sys
from settings import settings

class AlienInvasion: 
    """管理游戏资源和行为的类""" 
    def __init__(self): 
        """初始化游戏并创建游戏资源。""" 
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        self.bg_color = (250, 230, 230)
        self.running = True
        self.clock = pygame.time.Clock()
        self.dt = 0
         # 定义一个坐标可能是
        self.player_pos = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2)


    def run_game(self): 
        """开始游戏的主循环""" 
        while self.running: 

            # 监视键盘和鼠标事件。
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:  # 点击X
                    self.running = False # 退出循环

            self.screen.fill(self.bg_color) # 填充屏幕

           
            # 画一个圈                                              半径
            pygame.draw.circle(self.screen, "red", self.player_pos, 40)
            
            # 监听键盘事件
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.player_pos.y -= 300 * self.dt
            if keys[pygame.K_s]:
                self.player_pos.y += 300 * self.dt
            if keys[pygame.K_a]:
                self.player_pos.x -= 300 * self.dt
            if keys[pygame.K_d]:
                self.player_pos.x += 300 * self.dt
            # 让最近绘制的屏幕可见。
            pygame.display.flip() # flip: 显示

            self.dt = self.clock.tick(60) / 1000 # 限制帧率
    def quit_game(self):
        pygame.quit

if __name__ == '__main__': 
# 创建游戏实例并运行游戏。
    ai = AlienInvasion() 
    ai.run_game() 
    ai.quit_game()
