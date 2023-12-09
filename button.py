import pygame.font 
class Button: 
    def __init__(self, ai_game, msg): # msg接受文字
        """初始化按钮的属性。""" 
        self.screen = ai_game.screen # 获取窗口
        self.screen_rect = self.screen.get_rect() # 窗口参数
        # 设置按钮的尺寸和其他属性。
        self.width, self.height = 200, 50 # 尺寸
        self.button_color = (0, 255, 0) # 颜色
        self.text_color = (255, 255, 255) # 文字颜色
        self.font = pygame.font.SysFont(None, 48) # 字体大小
        # 创建居中的位置参数
        self.rect = pygame.Rect(0, 0, self.width, self.height) # 现在0，0位置创建一个
        self.rect.center = self.screen_rect.center  # 居中放置
        # 接受文字并创建文字图片
        self._prep_msg(msg) 
    
    # 接受文字，并制成图片，显示出来
    def _prep_msg(self, msg): 
        """将 msg 渲染为图像，并使其在按钮上居中。"""  
        #                                     抗锯齿开关
        self.msg_image = self.font.render(msg, True, self.text_color,
        self.button_color)  # render是转为图片，并赋值给msg_image，不设置颜色就是透明
        self.msg_image_rect = self.msg_image.get_rect() # 获取图片参数
        self.msg_image_rect.center = self.rect.center # 和先前创建的居中参数对其

    # 显示按钮
    def draw_button(self):
        #  绘制按按钮，并添加上文本
        self.screen.fill(self.button_color,  self.rect) # 画矩形
        self.screen.blit(self.msg_image, self.msg_image_rect) # 画文字图片