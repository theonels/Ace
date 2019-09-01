from Object import *
import sys
from Setting import Setting

def create_general(set):
    general = pig_catapult(set.get_screen(),0,set)
    col_max = set.get_screen().get_rect()[2]//(general.get_rect()[2]+set.general_gap)
    if set.cols > col_max:
        set.cols = col_max
    del general

    generals = []
    for raw in range(set.raws):
        general_raw = []
        for col in range(set.cols):
            general = pig_catapult(set.get_screen(),0,set)
            general.change_pos(set.general_gap//2 + (general.get_rect()[2] + set.general_gap) * col, set.general_gap//2 + (general.get_rect()[3] + set.general_gap) * raw)
            general_raw.append(general)
        generals.append(general_raw)

    return generals

def draw_genaral(generals,set):
    for general_raw in generals:
        for general in general_raw:
            general.auto_move()
            general.fire(set)
            general.draw()

def create_catapult(set):
    return pig_catapult(set.get_screen(),1,set)

def OnEvent(catapult,set):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            KeyDownEvent(event, catapult,set)
        elif event.type == pygame.KEYUP:
            KeyUpEvent(event, catapult,set)

    pygame.display.flip()

def KeyUpEvent(event,catapult,set):
    if event.key == pygame.K_RIGHT:
        catapult.is_moving_right = False
    elif event.key == pygame.K_LEFT:
        catapult.is_moving_left = False
    elif event.key == pygame.K_UP:
        catapult.is_moving_up = False
    elif event.key == pygame.K_DOWN:
        catapult.is_moving_down = False

def KeyDownEvent(event,catapult,set):
    if event.key == pygame.K_RIGHT:
        catapult.is_moving_right = True
    elif event.key == pygame.K_LEFT:
        catapult.is_moving_left = True
    elif event.key == pygame.K_UP:
        catapult.is_moving_up = True
    elif event.key == pygame.K_DOWN:
        catapult.is_moving_down = True
    elif event.key == pygame.K_SPACE:
        catapult.fire(set)

def update_window(catapult,generals,set):
    set.draw_background()
    catapult.draw()
    draw_genaral(generals, set)
    OnEvent(catapult, set)