import pygame
class Object():
    def __init__(self,screen,image):
        """初始化并设置其初始位置"""
        self.screen = screen
        # 加载图像并获取其外接矩形
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()

    def get_rect(self):
        return self.rect

    def draw(self):
        # 放在屏幕底部中央
        self.rect.centerx = self.screen.get_rect().centerx
        self.rect.bottom = self.screen.get_rect().bottom
        self.screen.blit(self.image, self.rect)

class stablale(Object):
    def __init__(self,screen,image,t):
        super().__init__(screen,image)
        self.last = t

class Moves(Object):
    def __init__(self,screen,image,speed=1):
        super().__init__(screen,image)
        self.is_alive = True
        self.speed = speed

    def move_l(self):
        pass

    def move_r(self):
        pass

    def move_u(self):
        pass

    def move_d(self):
        pass

    def speed_up(self):
        pass

class Bird(Moves):
    def __init__(self,screen,image=r"rescource\bird.png",speed=1,extend = 1,harm = 1):
        super().__init__(screen,image,speed)
        self.extend = extend
        self.harm = harm

class pig_catapult(Moves):

    def __init__(self,screen,image=r"rescource\catapult.png",speed=1,hp = '1',score = 0):
        super().__init__(screen,image,speed)
        self.hp = hp
        self.bird = Bird(screen)
        self.score = score

    def reduce_hp(self):
        pass




