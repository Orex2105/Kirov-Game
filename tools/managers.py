import pygame
from pathlib import Path
from random import shuffle
from settings import Settings
from tools.assets import Textures


class WindowManager():
    @classmethod
    def initialization(cls):
        screen = pygame.display.set_mode((Settings.MONITOR_WIDTH, Settings.MONITOR_HEIGHT), pygame.FULLSCREEN)
        pygame.display.set_icon(Textures.load_icon())
        pygame.display.set_caption(Settings.CAPTION)
        cursor = pygame.cursors.Cursor((0, 0), Textures.load_cursor())
        pygame.mouse.set_cursor(cursor)

        return screen

class MusicManager:
    assets_dir = Settings.root_dir / 'assets'
    music_dir = assets_dir / 'music'
    tracks = []
    current = 0

    @classmethod
    def load_background_music(cls) -> list[str]:
        if not cls.music_dir.exists():
            return []

        cls.tracks = []
        for file in cls.music_dir.iterdir():
            if file.suffix.lower() in {".ogg", ".mp3", ".wav"}:
                cls.tracks.append(str(file))

        shuffle(cls.tracks)
        return cls.tracks.copy()

    @classmethod
    def play_next(cls):
        if not cls.tracks:
            return
        cls.current = (cls.current + 1) % len(cls.tracks)
        pygame.mixer.music.load(cls.tracks[cls.current])
        pygame.mixer.music.play()

    @classmethod
    def play_back(cls):
        if not cls.tracks:
            return
        cls.current = (cls.current - 1) % len(cls.tracks)
        pygame.mixer.music.load(cls.tracks[cls.current])
        pygame.mixer.music.play()

    @classmethod
    def current_track(cls) -> str:
        return Path(cls.tracks[cls.current]).name

    @classmethod
    def start(cls):
        MusicManager.load_background_music()
        pygame.mixer.music.set_volume(Settings.VOLUME)
        
        cls.current = 0
        if cls.tracks:
            pygame.mixer.music.load(cls.tracks[cls.current])
            pygame.mixer.music.play()
            pygame.mixer.music.set_endevent(pygame.USEREVENT + 1)

    @classmethod
    def pause(cls):
        pygame.mixer.music.pause()

    @classmethod
    def unpause(cls):
        pygame.mixer.music.unpause()