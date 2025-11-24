import pygame
from settings import Settings
from pathlib import Path
from random import shuffle


class Textures():
    assets_dir = Settings.root_dir / 'assets'
    system_assets_dir = assets_dir / 'system'
    gfx_dir = assets_dir / 'gfx'

    @classmethod
    def load_icon(cls):
        return pygame.image.load(cls.system_assets_dir / 'icon.png').convert_alpha()

    @classmethod
    def load_cursor(cls):
        return pygame.image.load(cls.system_assets_dir / 'cursor.png').convert_alpha()

    @classmethod
    def load_house(cls, index: int):
        return pygame.image.load(cls.gfx_dir / f'house_{index}.png').convert_alpha()

    @classmethod
    def load_powerbox(cls):
        return pygame.image.load(cls.gfx_dir / 'powerbox.png').convert_alpha()
    
    @classmethod
    def load_menu_background(cls):
        return pygame.image.load(cls.gfx_dir / 'background_menu.png').convert_alpha()

    @classmethod
    def load_moon(cls):
        return pygame.image.load(cls.gfx_dir / 'moon.png').convert_alpha()

    @classmethod
    def load_clouds(cls):
        clouds_list = []
        clouds_list.append(pygame.image.load(cls.gfx_dir / 'clouds_1.png').convert_alpha())
        clouds_list.append(pygame.image.load(cls.gfx_dir / 'clouds_2.png').convert_alpha())
        return clouds_list


class UI():
    ui_dir = Textures.gfx_dir / 'UI'

    @classmethod
    def load_button(cls):
        return pygame.image.load(cls.ui_dir / 'button.png').convert_alpha()