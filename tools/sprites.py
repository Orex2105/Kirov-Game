import pygame
import random
from tools.assets import Textures
from settings import Settings


class House(pygame.sprite.Sprite):
    def __init__(self, index: int = 0, pos=(0, 0)):
        super().__init__()
        self.index = index
        self.image = Textures.load_house(index)
        self.rect = self.image.get_rect(bottomleft=pos)
        self.mask = pygame.mask.from_surface(self.image)

    def check_click(self, mouse_pos):
        offset = (mouse_pos[0] - self.rect.x, mouse_pos[1] - self.rect.y)
        return self.mask.get_at(offset)
    
    def scale(self):
        pass


class Cloud(pygame.sprite.Sprite):
    def __init__(self, index: int = 0, pos=(0, 0)):
        super().__init__()
        self.index = index
        self.original_image = Textures.load_clouds()[index]
        self.image = self.original_image
        self.scale()
        self.rect = self.image.get_rect(bottomleft=pos)
        
        self.speed = Settings.ClOUDS_SPEED
        self.pos_x = pos[0]
        
        self.cloud_width = self.image.get_width()
        self.cloud_height = self.image.get_height()
        self.mask = pygame.mask.from_surface(self.image)
        
        self.respawn_timer = 0
        self.respawn_delay = 0
        self.is_waiting_respawn = False

        self.visible = False

    def set_random_start_position(self):
        max_y = Settings.MONITOR_HEIGHT // 3
        random_y = random.randint(self.cloud_height // 2, max_y)
        
        if self.index == 0: # Облако, движущееся вправо
            self.pos_x = -self.cloud_width - random.randint(0, self.cloud_width)
        else: # Облако, движущееся влево
            self.pos_x = Settings.MONITOR_WIDTH + random.randint(0, self.cloud_width)
        
        self.pos_y = random_y
        self.rect = self.image.get_rect(bottomleft=(int(self.pos_x), int(self.pos_y)))

    def update(self):
        if not self.visible:
            self.set_random_start_position()
            self.visible = True
            return
        
        if not self.is_waiting_respawn:
            if self.index == 0:
                self.pos_x += self.speed
            else:
                self.pos_x -= self.speed
            
            if self.index == 0:  # Облако, движущееся вправо
                if self.pos_x > Settings.MONITOR_WIDTH:
                    self.start_respawn_delay()
            else:  # Облако, движущееся влево
                if self.pos_x < -self.cloud_width:
                    self.start_respawn_delay()
        else:
            self.respawn_timer += 1
            if self.respawn_timer >= self.respawn_delay:
                self.respawn()
        
        self.rect.x = int(self.pos_x)
    
    def start_respawn_delay(self):
        self.is_waiting_respawn = True
        self.respawn_timer = 0
        self.respawn_delay = random.randint(6, 600)
    
    def respawn(self):
        self.is_waiting_respawn = False
        
        max_y = Settings.MONITOR_HEIGHT // 3
        random_y = random.randint(self.cloud_height // 2, max_y)
        
        if self.index == 0:  # Движется вправо
            self.pos_x = -self.cloud_width
        else:  # Движется влево
            self.pos_x = Settings.MONITOR_WIDTH
        
        self.rect.x = int(self.pos_x)
        self.rect.y = random_y - self.cloud_height

    def scale(self):
        target_width = Settings.MONITOR_WIDTH
        original_width = self.original_image.get_width()
        original_height = self.original_image.get_height()
        
        scale_factor = target_width / original_width
        new_width = int(original_width * scale_factor)
        new_height = int(original_height * scale_factor)
        
        self.image = pygame.transform.scale(self.original_image, (new_width, new_height))