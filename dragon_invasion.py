import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from dragon import Dragon
# from soldier import Soldier
# from fireball import Fire
import game_functions as gf

settings = Settings()

def run_game():
    pygame.init()
    
    #스크린 세팅
    screen = pygame.display.set_mode((settings.screen_width,settings.screen_height))
    pygame.display.set_caption("Dragon Invasion")
    dragon = Dragon(settings, screen)
    # soldier = Soldier(settings, screen)

    fire = Group()
    soldier = Group()
    gf.create_troop(settings, screen, dragon, soldier)


    # 화면 키기
    while True:
        # 이벤트 처리
        gf.check_events(settings, screen, dragon, fire)
        dragon.update()
        
        #탄환 생성 및 제거
        gf.update_fire(fire)
        gf.update_soldiers(soldier)

        # 가장 최근에 그린 화면을 표시합니다.
        gf.update_screen(settings, screen, dragon,soldier, fire)


run_game()
