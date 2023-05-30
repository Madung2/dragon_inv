import pygame
from pygame.sprite import Sprite

class Soldier(Sprite):
    def __init__(self, settings, screen):
        super(Soldier, self).__init__()
        self.screen = screen
        self.settings = settings
        
        #이미지 설정
        self.width = settings.soldier_size
        self.height = settings.soldier_size
        self.image = pygame.transform.scale(pygame.image.load(f'images/s3.png'), (self.width, self.height))
        self.images = [pygame.transform.scale(pygame.image.load(f'images/s{i}.png'), (self.width, self.height)) for i in range(1, 5)]
        self.rect = pygame.Rect(0,0, self.width, self.height)
        
        # 위치 설정
        self.rect.x = self.width
        self.rect.y = self.height

        self.x = float(self.rect.x)

        # 변경 시간
        self.current_image = 0
        self.last_update = pygame.time.get_ticks()  # 마지막으로 이미지가 바뀐 시각
        self.frame_rate = settings.soldier_frame  # 이미지가 바뀌는 빈도 (밀리초 단위)

    def check_edge(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left<=0:
            return True

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:  # 마지막으로 이미지가 바뀐 후 frame_rate 이상의 시간이 경과했다면
            self.last_update = now  # 마지막으로 이미지가 바뀐 시각을 현재 시각으로 업데이트
            # 이미지 순환
            self.current_image = (self.current_image + 1) % len(self.images)
            self.image = self.images[self.current_image]
        # self.x +=self.settings.soldier_speed * self.settings.troop_direction
        # self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.images[self.current_image], self.rect)