import pygame
from pygame.sprite import Group, Sprite

class Fire(Sprite):
    def __init__(self, settings, screen, dragon):
        super(Fire, self).__init__()
        self.screen = screen
        self.width = settings.fire_size
        self.height = settings.fire_size
        self.images = [pygame.transform.scale(pygame.image.load(f'images/f{i}.png'), (self.width, self.height)) for i in range(1, 7)]
        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.centerx = dragon.rect.centerx
        self.rect.top = dragon.rect.top 

        # 탄환의 위치는 계속 바뀐다
        self.y = float(self.rect.y)
        self.current_image = 0
        self.speed = settings.fire_speed

    def update(self):
        """화면위의 탄환을 움직인다"""
        self.y -= self.speed
        self.rect.y = self.y 

        # 이미지 순환
        self.current_image = (self.current_image + 1) % len(self.images)



    def draw_fire(self):
        """현재 파이어볼 이미지를 화면에 그린다"""
        self.screen.blit(self.images[self.current_image], self.rect)