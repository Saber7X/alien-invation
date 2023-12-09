import pygame, sys
from settings import settings
from ship import Ship
from bullet import Bullet2, Bullet
from Alien import Alien 
from time import sleep
from game_stats import GameStats
from button import Button 
from scoreboard import Scoreboard 

class AlienInvasion: 
    """管理游戏资源和行为的类""" 
    def __init__(self): 
        """初始化游戏并创建游戏资源。""" 
        pygame.init()
        # self.screen = pygame.display.set_mode((1200, 800))
        # self.bg_color = (250, 230, 230)

        # 运行控制
        self.running = True


        # 窗口参数
        self.settings = settings() 
            # 这让 Pygame 生成一个覆盖整个显示器的屏幕。由于无法预先知道屏幕的宽度和高度，要在创建屏幕后更新这些设置（见）：使用屏幕的 rect 的属性 width 和 height 来更新对象 settings
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        # 根据屏幕大小设置窗口的大小
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        
        pygame.display.set_caption("Alien Invasion")

        # 图片
        self.ship = Ship(self)

        # 子弹 p244
        # 这个可以存储类
        self.bullets = pygame.sprite.Group() # 作为group,作用应该就是可以一起操作,
        # 存储的全是一个个实例化的类,可以同时调用存储的所有类的功能
        # 如self.bullets.update(),这样就可以实现所有的子弹一起移动

        # 持续开火
        self.if_fire_bullets = False
        # 记录开火距离
        self.fire_sp = 0

        # 新建外星人组
        self.aliens = pygame.sprite.Group()
        self._create_fleet() # 创建外星人群

        # 创建一个用于存储游戏统计信息的实例。
        self.stats = GameStats(self) 

        # 创建 Play 按钮。
        self.play_button = Button(self, "Play")

        # 创建记分牌。
        self.sb = Scoreboard(self) 

    # 监视键盘按下事件
    def _check_keydown_events(self, event):
    # 移动图片---------------------------------------------（待优化帧率） 已优化
        if event.key == pygame.K_w: # w
            self.ship.moving_top = True # 开始持续移动
        elif event.key == pygame.K_a: # a 
            self.ship.moving_left = True # 开始持续移动
        elif event.key == pygame.K_s: # s
            self.ship.moving_bottom = True # 开始持续移动
        elif event.key == pygame.K_d: # d
            self.ship.moving_right = True # 开始持续移动
        elif event.key == pygame.K_q: # 按Q退出
             self.running = False
        elif event.key == pygame.K_SPACE: # 按空格开火
            self.if_fire_bullets = True
            self._fire_bullet()


    # 监视键盘松开事件
    def _check_keyup_events(self, event):
            if event.key == pygame.K_w: # w
                self.ship.moving_top = False # 关闭持续移动
            elif event.key == pygame.K_a: # a
                self.ship.moving_left = False # 关闭持续移动
            elif event.key == pygame.K_s: # s
                self.ship.moving_bottom = False # 关闭持续移动
            elif event.key == pygame.K_d: # d
                self.ship.moving_right = False # 关闭持续移动
            elif event.key == pygame.K_SPACE: # space
                self.if_fire_bullets = False # 关闭持续开火

    def _fire_bullet(self):
        # 判断持续开火  和   已经出现的子弹数量小于 储存子弹数量
        if self.if_fire_bullets and len(self.bullets) < self.settings.bullets_allowed:
            try:
                new_bullet = Bullet(self)
                a = self.bullets.sprites()[-1]
                # for bullet in self.bullets.sprites():
                #      a = bullet
                # print(new_bullet.x, a.x, new_bullet.y, a.y)
                if abs(new_bullet.x - a.x) + abs(new_bullet.y - a.y) > self.settings.bullet_fire_speed: 
                    self.bullets.add(new_bullet)
                # print(1)
            except IndexError:
                #  创建一颗子弹并加入编组
                new_bullet = Bullet(self)
                self.bullets.add(new_bullet)


     # 监视键鼠事件。
    def _check_events(self):
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:  # 点击X
                self.running = False # 退出循环
            # 监视键盘按下事件    
            elif event.type == pygame.KEYDOWN: # 识别键盘事件
                    self._check_keydown_events(event)
            # 监视键盘松开事件
            elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN: # 鼠标单击事件
                mouse_pos = pygame.mouse.get_pos()  # 点击坐标
                self._check_play_button(mouse_pos) # 检测是否点击在按钮上面
    # 单击play时开始游戏
    def _check_play_button(self, mouse_pos):
        if self.play_button.rect.collidepoint(mouse_pos) and not self.stats.game_active: # 判断按钮元素是否碰到了指定坐标 同时要游戏处于关闭状态时才能有用
                self.stats.reset_stats() # 初始化游戏数据（剩余生命等）
                self.settings.initialize_dynamic_settings() # 初始化游戏设置参数
                self.sb.prep_score() # 重新绘制得分（因为已经更新了，不重绘的话，不能显示为0）
                self.sb.prep_level()  # 重新绘制等级
                self.sb.prep_ships()  # 绘制剩余飞船
                self.stats.game_active = True  # 开始游戏
                # 清空余下的外星人和子弹。
                self.aliens.empty() 
                self.bullets.empty() 
                # 创建一群新的外星人并让飞船居中。
                self._create_fleet() 
                self.ship.center_ship()
                # 隐藏鼠标光标。
                pygame.mouse.set_visible(False)

    def _update_screen(self):
        # 每次循环时都重绘屏幕。
        self.screen.fill(self.settings.bg_color) 
        self.ship.blitme()

        # 遍历group, 绘制所有子弹
        for bullet in self.bullets.sprites():
             bullet.draw_bullet()

        self.aliens.draw(self.screen)

        # 显示得分。
        self.sb.show_score()

        # 如果游戏处于非活动状态，就绘制 Play 按钮。
        if not self.stats.game_active: 
            self.play_button.draw_button()  # 最后绘制

        # 让最近绘制的屏幕可见。
        pygame.display.flip() # flip: 显示

    def _update_bullets(self):
            self.bullets.update() # 更新所有在组中的子弹的位置
            self._fire_bullet() # 持续开火
         # 删除消失的子弹。
            for bullet in self.bullets.copy():  # 因为遍历的列表要保持不变，所以遍历副本，然后在主列表中进行删除
                if bullet.rect.bottom <= 0: 
                    self.bullets.remove(bullet)  # 在列表中移除指定元素
                    # print(len(self.bullets)) 
             # 检测外星人与子弹相撞，然后就删除
            self._check_bullet_alien_collisions()
            # 同时进行
            
    

    def _check_aliens_bottom(self): 
        """检查是否有外星人到达了屏幕底端。""" 
        screen_rect = self.screen.get_rect() # 窗口参数
        for alien in self.aliens.sprites(): 
            if alien.rect.bottom >= screen_rect.bottom: 
                # 像飞船被撞到一样处理。
                self._ship_hit() # 清空外星人，重新创建，并退出循环
                break

    # 检测外星人与子弹相撞，然后就删除
    def _check_bullet_alien_collisions(self):
        # 检测的是当前组中的，可能有快慢，但一直是在计算的
        # 检查是否有子弹击中了外星人。通过遍历每个子弹来实现
        # 如果是，就删除相应的子弹和外星人。
        collisions = pygame.sprite.groupcollide(  # 这个函数就是用作检测碰撞，然后删除的，True:删除，False就不删除
            self.bullets, self.aliens, False, True) 
        # 得到的结果是一个元组，每个子弹是key，每个key里面的value就是删除的外星人，也许是一个对象，也许是一个列表
        if collisions: # collisions是字典，返回的是被删除的所有外星人
            # 如果一个子弹击中多个敌人，字典里会有多个值，所以用循环判断每个外星人
            for aliens in collisions.values(): # 遍历每颗子弹杀死的外星人组
                self.stats.score += self.settings.alien_points * len(aliens) # 计算出所有外星人的得分

            # st更新了，sc里面又获取了一遍st，原来是这样
            # 懂了
            #  ------------------------不太理解这里的更新原理？？？？？？？？？？？？？？？？？？？？？？？？？
            self.sb.prep_score() # 更新分数-----------------？？？？？？？？？？？？？？？？？
            self.sb.check_high_score() # 更新最高分
        # 生成新的外星人群
        if not self.aliens: # 如果外星人为空
            # 删除现有的子弹
            self.bullets.empty()
            # 创建新的外新人群
            self._create_fleet()
            self.settings.increase_speed() # 消灭一轮提升一级，增加速度
            # 提高等级。
            self.stats.level += 1 # 消灭一轮，等级+1
            self.sb.prep_level() 
        # print(collisions)

    def _create_fleet(self): 
        """创建外星人群。""" 
        # 创建一个外星人并计算一行容纳多少个外星人
        alien = Alien(self)   
         # 以元组形式赋值
        alien_width, alien_height = alien.rect.size
        # 减去头尾边距后的实际可放外星人的距离
        available_space_x = self.settings.screen_width - (2 * alien_width)
        # 外星人的间距为外星人宽度
        number_aliens_x = available_space_x // (2 * alien_width)  # //向下取整

        # 计算屏幕可容纳多少行外星人。
        ship_height = self.ship.rect.height # 飞船高度 
        # 最近的外星人距离飞船 3个外星人 + 1个飞船 的距离
        available_space_y = (self.settings.screen_height -(3 * alien_height) - ship_height) 
        number_rows = available_space_y // (2 * alien_height)  # 计算行数

        # 创建外星人群
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x ):
                # 创建一个外星人并将其加入当前行。
                self._create_alien(alien_number, row_number) 
            

    def _create_alien(self, alien_number, row_number): 
        """创建一个外星人并将其放在当前行。""" 
        alien = Alien(self) 
        alien_width, alien_height = alien.rect.size # 以元组形式赋值
        # 如下同理
        alien.x = alien_width + 2 * alien_width * alien_number 
        alien.rect.x = alien.x 
        #       距离边缘的1个外星人距离    算出第几行的y坐标
        alien.y = alien_height + 2 * alien_height * row_number
        alien.rect.y = alien.y
        self.aliens.add(alien)
    
    # 更新外星人群的位置
    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()

        # 检测外星人和飞船相撞
        #                 检测元素是否与精灵相撞吧，返回true/false
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            # print("ship hit！")
             self._ship_hit() # 相撞时调用响应

        # 检查是否有外星人到达了屏幕底端。
        self._check_aliens_bottom() 
        
         

    # 有外星人到达边缘时采取相应的措施。
    def _check_fleet_edges(self):
        for alien in self.aliens.sprites(): # 遍历所有外星人
            if alien.check_edges(): # 如果到达边缘
                self._change_fleet_direction() # 改变方向
                break
    
    # 将整群外星人下移，并改变它们的方向
    def _change_fleet_direction(self): 
        for alien in self.aliens.sprites(): 
            alien.rect.y += self.settings.fleet_drop_speed  # 向下移动 
        self.settings.fleet_direction *= -1  # 改变方向

    # 响应飞船被外星人撞到
    def _ship_hit(self):
        if self.stats.ships_left > 0 :
            self.stats.ships_left -= 1 # 剩余生命-1
            self.sb.prep_ships()  # 重绘剩余飞船
            #    清空余下的外星人和子弹
            self.aliens.empty()
            self.bullets.empty()
            # sleep(0.5)
            # 创建一群新的外星人
            self._create_fleet()
            self.ship.center_ship() # 把飞船放到屏幕底部中央
            # 暂停
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True) # 显示鼠标



    def run_game(self): 
        """开始游s戏的主循环""" 
        while self.running: 
            self._check_events()
            if self.stats.game_active: # 游戏是否处于激活状态
                self._update_bullets()
                self._update_aliens()
                # --??????????????????????--
                # 可能是因为已经继承重写了所以可以直接用， 可以直接调用组中类的函数，一起调用
                self.ship.update() # 更新图片坐标后再更新屏幕
            self._update_screen()

            

    def quit_game(self):
        pygame.quit

if __name__ == '__main__': 
# 创建游戏实例并运行游戏。
    ai = AlienInvasion() 
    ai.run_game() 
    ai.quit_game()
