import pygame
from settings import Settings
from tools.assets import Textures
from tools.sprites import Cloud

class Menu():
    def __init__(self):
        self.clouds = pygame.sprite.Group()
        self.background = Textures.load_menu_background()
        self.background = pygame.transform.scale(self.background, (Settings.MONITOR_WIDTH, Settings.MONITOR_HEIGHT))
        self.create_clouds()

    def create_clouds(self):
        for i in range(4):
            cloud = Cloud(0)
            self.clouds.add(cloud)
        
        for i in range(4):
            cloud = Cloud(1)
            self.clouds.add(cloud)

    def draw_clouds(self, screen):
        screen.blit(self.background, (0, 0))
        self.clouds.draw(screen)

    def update(self):
        self.clouds.update()