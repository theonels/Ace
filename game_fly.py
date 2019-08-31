import sys
from Object import *

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((620,700))
    # bg_color = (205,205,205) # 背景颜色
    background = pygame.image.load(r"rescource\back(1).png")   # 图片位置
    pygame.display.set_caption('Ace')
    catapult = pig_catapult(screen)
    bird = Bird(screen)
    while True:
        for event in pygame.event.get():
            # screen.fill(background)
            screen.blit(background, (-60,0))  # 对齐的坐标
            catapult.draw()
            bird.draw()
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.flip()

run_game()