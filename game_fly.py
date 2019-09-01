from Object import *
import Controller
from Setting import Setting

def run_game():

    set = Setting()
    catapult = Controller.create_catapult(set)
    generals = Controller.create_general(set)

    while True:
        Controller.update_window(catapult,generals,set)


run_game()