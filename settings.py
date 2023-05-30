import pygame
class Color():
    def __init__(self):
    # Store color scheme that I want to use
        self.lovely_purple = (183, 153, 255) #보라색
        self.evening_sky = (172, 188, 255)
        self.sky_blue = (174, 226, 255)
        self.baby_blue = (230, 255, 253)




class Settings():
    """설정을 모두 저장하는 클래스"""

    def __init__(self):
        # 스크린 정의
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = Color().lovely_purple
        self.GRADIENT_START = Color().lovely_purple 
        self.GRADIENT_END = Color().baby_blue
        self.dragon_speed = 5
        self.fire_speed =10
        self.fire_size =80
        self.soldier_size = 50
        self.soldier_frame = 200
        self.soldier_interval = 1.3
        self.soldier_num_in_y = 4
        self.soldier_speed = 1
        self.troop_drop_speed = 10
        self.troop_direction = 1



    def create_gradient_background(self):
        WIDTH = self.screen_width
        HEIGHT = self.screen_height
        surface = pygame.Surface((WIDTH, HEIGHT))
        for y in range(HEIGHT):
            # 수직 방향으로 보간하여 색상 계산
            r = int((self.GRADIENT_END[0] - self.GRADIENT_START[0]) * y / HEIGHT + self.GRADIENT_START[0])
            g = int((self.GRADIENT_END[1] - self.GRADIENT_START[1]) * y / HEIGHT + self.GRADIENT_START[1])
            b = int((self.GRADIENT_END[2] - self.GRADIENT_START[2]) * y / HEIGHT + self.GRADIENT_START[2])
            pygame.draw.line(surface, (r, g, b), (0, y), (WIDTH, y))
        return surface
    
