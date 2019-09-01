import pygame
import random

class Object():
    def __init__(self,screen,image):
        """初始化并设置其初始位置"""
        self.screen = screen
        # 加载图像并获取其外接矩形
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        # 放在屏幕底部中央
        self.rect.centerx = self.screen.get_rect().centerx
        self.rect.bottom = self.screen.get_rect().bottom

    def get_rect(self):
        return self.rect

    def draw(self):
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
        self.auto_start = False
        self.is_moving_left = False
        self.is_moving_right = False
        self.is_moving_up = False
        self.is_moving_down = False

    def move(self):
        if self.in_screen():
            if self.is_moving_left:
                self.rect.centerx -= self.speed
            if self.is_moving_right:
                self.rect.centerx += self.speed
            if self.is_moving_up:
                self.rect.bottom -= self.speed
            if self.is_moving_down:
                self.rect.bottom += self.speed

    def in_screen(self):
        # return True
        if self.rect[0] > self.screen.get_rect()[2] - self.rect[2]:
            self.rect[0] -=1
            return False
        elif self.rect[0] < 0 :
            self.rect[0] += 1
            return False
        elif self.rect[1] > self.screen.get_rect()[3]:
            self.rect[1] -= 1
            return False
        elif self.rect[1] < 0:
            self.rect[1] += 1
            return False
        else:
            return True

    def auto_move(self):
        if not self.auto_start:
            self.is_moving_right = True
            self.auto_start = True
        if self.is_left_boundary():
            self.is_moving_left = False
            self.is_moving_right = True
        if self.is_right_boundary():
            self.is_moving_right = False
            self.is_moving_left = True
        self.move()

    def change_pos(self,x,y):
        self.rect[0] = x
        self.rect[1] = y

    def is_right_boundary(self):
        if self.rect[0]>= self.screen.get_rect()[2]-self.rect[2]:
            return True

    def is_left_boundary(self):
        if self.rect[0] <= 10:
            return True

    def is_bottom_boundary(self):
        if self.rect[1]>= self.screen.get_rect()[3]-self.rect[3]:
            self.change_pos(self.rect[0],self.rect[1]+self.speed)

    def is_up_boundary(self):
        if self.rect[1]< 0:
            return True

    def draw(self):
        self.move()
        self.screen.blit(self.image, self.rect)

    def speed_up(self):
        pass

class Bird(Moves):
    def __init__(self,screen,belong_to,set):
        if belong_to.role == 0:
            super().__init__(screen,set.get_pig_image(),set.get_pig_speed())
            self.extend = set.get_pig_extend()
            self.harm = set.get_pig_harm()
        elif belong_to.role == 1:
            super().__init__(screen,set.get_bird_image(),set.get_bird_speed())
            self.extend = set.get_bird_extend()
            self.harm = set.get_bird_harm()
        self.belong_to = belong_to
        self.rect[0] = self.belong_to.get_rect()[0]+25
        self.rect[1] = self.belong_to.get_rect()[1]+50

    def move(self):
        self.rect[1] -= self.speed

    def reverse_fly(self):
        self.rect[1] += self.speed

    def draw(self):
        if self.belong_to.role == 0:
            self.reverse_fly()
            self.screen.blit(self.image, self.rect)
        elif self.belong_to.role == 1:
            self.move()
            self.screen.blit(self.image, self.rect)

class pig_catapult(Moves):

    def __init__(self,screen,role,set):
        if role == 0:
            super().__init__(screen,set.get_general_image(),set.get_general_speed())
            self.hp = set.get_general_hp()
            self.score = set.get_general_score()
        elif role == 1:
            super().__init__(screen,set.get_catapult_image(),set.get_catapult_speed())
            self.hp = set.get_catapult_hp()
            self.score = set.get_catapult_score()
        self.role = role
        self.birds = []

    def fire(self,set):
        if self.role == 0:
            if(random.randint(0,set.get_game_level())==1):
                pig = Bird(self.screen, self,set)
                pig.reverse_fly()
                self.birds.append(pig)
        elif self.role == 1:
            self.birds.append(Bird(self.screen,self,set))

    def draw(self):
        super().draw()
        for bird in self.birds:
            if bird.in_screen():
                bird.draw()
            else:
                self.birds.remove(bird)

    def reduce_hp(self):
        pass






