import pygame
import random



class Dragon():
    def __init__(self, settings, screen):
        self.screen = screen
        
        #우주선의 이미지를 볼러오고 이미지의 rect 객체를 설정합니다
        self.image_url=['images/blue.png', 'images/green.png', 'images/purple.png', 'images/pink.png', 'images/white.png']
        self.image = pygame.image.load(random.choice(self.image_url))
        self.height = 200
        self.width = self.height * 1.8

        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
 


        #우주선을 새로 만들때는 항상 화면 아래 중앙에 만든다.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #이동 플래그
        self.speed = settings.dragon_speed
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        """우주선의 현재 위치에 우주선을 그린다"""
        self.screen.blit(self.image, self.rect)
        
    def update(self):
        """이동 플래그에 따라 위치를 업데이트 합니다"""
        # if self.rect.left<0 or self.rect.right>self.screen_rect.right:
        #     print( "더 이상 갈 수 없습니다")
        # elif self.rect.top<0 or self.rect.bottom>self.screen_rect.bottom:
        #     print( "더 이상 갈 수 없습니다")
        # else:
        if self.moving_right and self.rect.centerx<self.screen_rect.right:
            self.rect.centerx +=self.speed
        if self.moving_left and self.rect.centerx>0:
            self.rect.centerx -=self.speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery +=self.speed
        if self.moving_up and self.rect.top>0:
            self.rect.centery -=self.speed
    