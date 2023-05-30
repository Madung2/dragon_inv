import sys
import pygame
from fireball import Fire
from soldier import Soldier

def check_keydown_events(event,settings, screen, dragon, fire):
    if event.key  == pygame.K_RIGHT:
        dragon.moving_right = True
    elif event.key ==pygame.K_LEFT:
        dragon.moving_left = True
    elif event.key == pygame.K_UP:
        dragon.moving_up = True
    elif event.key == pygame.K_DOWN:
        dragon.moving_down = True
    elif event.key == pygame.K_SPACE:
        new_fire = Fire(settings, screen, dragon)
        fire.add(new_fire)


def check_keyup_events(event,settings, screen, dragon, fire):
    if event.key  == pygame.K_RIGHT:
        dragon.moving_right = False
    elif event.key ==pygame.K_LEFT:
        dragon.moving_left = False
    elif event.key == pygame.K_UP:
        dragon.moving_up = False
    elif event.key == pygame.K_DOWN:
        dragon.moving_down = False


def check_events(settings, screen, dragon, fire):
    """키보드와 마우스의 이벤트에 응답합니다"""
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            sys.exit()
            
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,settings, screen, dragon, fire)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event,settings, screen, dragon, fire)


def update_screen(settings, screen, dragon,soldier, fire):
    """화면에 있는 이미지를 업데이트하고 새화면 그림"""
    screen.blit(settings.create_gradient_background(), (0, 0))
    for f in fire.sprites():
        f.draw_fire()
    dragon.blitme()
    soldier.draw(screen)
    # soldier.blitme()
    
    pygame.display.flip() 

def update_fire(fire):
    fire.update()
    for f in fire.copy():
        if f.rect.bottom<= 0 :
            fire.remove(f)
def update_soldiers(soldier):
    soldier.update()

def get_soldier_num_in_x(settings, width):
    available_space_x = settings.screen_width - width
    soldier_num_in_x = int(available_space_x/(width)*0.7)
    return soldier_num_in_x

def get_soldier_num_in_y(settings, dragon_height, height):
    available_space_y = settings.screen_height - (3*height) - dragon_height
    soldier_num_in_y =int(available_space_y/(1.7*height))
    return soldier_num_in_y

def create_one_soldier(settings, screen, soldier, x_num, y_num, width, height):
    sol = Soldier(settings, screen)
    sol.x = width + width * x_num
    sol.rect.x = sol.x
    sol.rect.y = (height*1.7*y_num) +height
    soldier.add(sol)

def create_troop(settings, screen, dragon,  soldier):
    s = Soldier(settings, screen)
    width = settings.soldier_interval * s.rect.width
    height = s.rect.width
    soldier_num_in_x = get_soldier_num_in_x (settings, width)
    # soldier_num_in_y = get_soldier_num_in_y(settings, dragon.rect.height, height)
    soldier_num_in_y = settings.soldier_num_in_y
   
    for y_num in range(soldier_num_in_y):
        for x_num in range(soldier_num_in_x):
            create_one_soldier(settings, screen, soldier, x_num, y_num, width, height)

