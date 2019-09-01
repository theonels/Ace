from Object import *

class Setting():

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((620, 700))
        self.background = pygame.image.load(r"rescource\back(1).png")
        pygame.display.set_caption('Ace')
        self.possible = 50
        #Bird class variable
        self.bird_image = r"rescource\bird.png"
        self.pig_image = r"rescource\pig.png"
        self.bird_speed = 10
        self.pig_speed = 8
        self.pig_extend = 1
        self.pig_harm = 1
        self.bird_extend = 1
        self.bird_harm = 1
        #pig_catapult class variable
        self.general_image = r"rescource\boss.png"
        self.catapult_image = r"rescource\catapult.png"
        self.catapult_speed = 10
        self.general_speed = 8
        self.general_hp = '1'
        self.general_score = 0
        self.catapult_hp = '1'
        self.catapult_score = 0
        #
        self.general_gap = 20
        self.raws = 2
        self.cols = 3


    def get_pig_harm(self):
        return self.pig_harm

    def set_pig_harm(self,num):
        self.pig_harm = num

    def get_bird_harm(self):
        return self.bird_harm

    def set_bird_harm(self,num):
        self.bird_harm = num

    def get_pig_extend(self):
        return self.pig_extend

    def set_pig_extend(self,num):
        self.pig_extend = num

    def get_bird_extend(self):
        return self.bird_extend

    def set_bird_extend(self,num):
        self.bird_extend = num

    def get_pig_image(self):
        return self.pig_image

    def set_pig_image(self,str):
        self.pig_image = str

    def get_pig_speed(self):
        return self.pig_speed

    def set_pig_speed(self,num):
        self.pig_speed = num

    def get_bird_speed(self):
        return self.bird_speed

    def set_bird_speed(self,num):
        self.bird_speed = num

    def get_bird_image(self):
        return self.bird_image

    def set_bird_image(self,str):
        self.bird_image = str

    def get_general_image(self):
        return self.general_image

    def set_general_image(self, str):
        self.general_image = str

    def get_general_speed(self):
        return self.general_speed

    def set_general_speed(self, num):
        self.general_speed = num

    def get_catapult_speed(self):
        return self.catapult_speed

    def set_catapult_speed(self, num):
        self.catapult_speed = num

    def get_catapult_image(self):
        return self.catapult_image

    def set_catapult_image(self, str):
        self.catapult_image = str

    def get_general_score(self):
        return self.general_score

    def set_general_score(self, str):
        self.general_score = str

    def get_general_hp(self):
        return self.general_hp

    def set_general_hp(self, num):
        self.general_hp = num

    def get_catapult_score(self):
        return self.catapult_score

    def set_catapult_score(self, num):
        self.catapult_score = num

    def get_catapult_hp(self):
        return self.catapult_hp

    def set_catapult_hp(self, str):
        self.catapult_hp = str

    def get_game_level(self):
        return self.possible

    def set_game_level(self,level):
        self.possible = level*10

    def get_screen(self):
        return self.screen

    def get_screenW(self):
        return self.screen.get_rect()[2]

    def get_screenH(self):
        return self.screen.get_rect()[3]

    def draw_background(self):
        self.screen.blit(self.background, (-60, 0))  # 对齐的坐标

