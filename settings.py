import pygame
import screeninfo
from pathlib import Path
from configparser import ConfigParser


monitor_w, monitor_h = 0, 0
for monitor in screeninfo.get_monitors():
    monitor_w, monitor_h = monitor.width, monitor.height


class Settings():
    root_dir = Path(__file__).parent
    config = ConfigParser()
    config.read(root_dir / "settings.ini", encoding='utf-8')

    CAPTION = config.get('default', 'caption')

    MONITOR_WIDTH = monitor_w
    MONITOR_HEIGHT = monitor_h

    MOUSE_SENSITIVITY = config.getint('default', 'mouse_sensitivity')

    WORLD_WIDTH = config.getint('default', 'world_width')
    WORLD_HEIGHT = config.getint('default', 'world_height')

    VOLUME = config.getfloat('default', 'volume')

    ClOUDS_SPEED = config.getfloat('default', 'clouds_speed')

    @classmethod
    def set_volume(cls, volume):
        cls.VOLUME = max(0, min(1, volume))
        pygame.mixer.music.set_volume(cls.VOLUME)