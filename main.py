import pygame as pg
from settings import Settings
from tools.managers import MusicManager, WindowManager
from tools.camera import Camera
from scenes.menu import Menu
pg.init()


# ЭКРАН
screen = WindowManager.initialization()

# МУЗЫКА
MusicManager.start()

menu = Menu()

running = True
clock = pg.time.Clock()

while running:
    for event in pg.event.get():
        # ВЫХОД ИЗ ПРОГРАММЫ
        if event.type == pg.QUIT:
            running = False

        # ИВЕНТЫ КЛАВИАТУРЫ
        if event.type == pg.KEYDOWN:
            # НАЖАТИЕ ESC
            if event.key == pg.K_ESCAPE:
                running = False

            # ИВЕНТ НАЖАТИЯ M
            if event.key == pg.K_m:
                if pg.mixer.music.get_volume() > 0:
                    pg.mixer.music.set_volume(0)
                else:
                    pg.mixer.music.set_volume(Settings.VOLUME)

            # ИВЕНТ НАЖАТИЯ СТРЕЛКИ ВПРАВО
            if event.key == pg.K_RIGHT:
                MusicManager.play_next()

            # ИВЕНТ НАЖАТИЯ СТРЕЛКИ ВЛЕВО
            if event.key == pg.K_LEFT:
                MusicManager.play_back()

            # ИВЕНТ НАЖАТИЯ СТРЕЛКИ ВВЕРХ
            if event.key == pg.K_UP:
                Settings.set_volume(Settings.VOLUME + 0.05)

            # ИВЕНТ НАЖАТИЯ СТРЕЛКИ ВНИЗ
            if event.key == pg.K_DOWN:
                Settings.set_volume(Settings.VOLUME - 0.05)

        # ИВЕНТЫ МЫШИ
        if event.type == pg.MOUSEBUTTONDOWN:
            # НАЖАТИЕ ПКМ (СБРОС ДЕЛЬТЫ МЫШИ)
            if event.button == 3:
                pg.mouse.get_rel()

        # ИВЕНТ ОКОНЧАНИЯ МУЗЫКИ
        if event.type == pg.USEREVENT + 1:
            pg.mixer.music.fadeout(1200)
            MusicManager.play_next()

    # ПЕРЕДВИЖЕНИЕ КАМЕРЫ
    if pg.mouse.get_pressed()[2]:
        Camera.move(pg.mouse.get_rel())

    # ПРОВЕРКА НА ВХОЖДЕНИЕ В РАЗМЕР КАРТЫ
    Camera.check_screen_bezels()

    screen.fill((0, 0, 0))

    # ПОТОМ ПЕРЕДЕЛАЮ, ПОКА ЧТО ПРОСТО ОТЛАДКА
    font = pg.font.Font(None, 36)
    camera_position = font.render(f"Камера: X: {int(Camera.x)}; Y: {int(Camera.y)}", True, (255, 255, 255))
    volume = font.render(f'Громкость: {pg.mixer.music.get_volume()}', True, (255, 255, 255))
    current_track = font.render(f'Трек: {MusicManager.current_track()}', True, (255, 255, 255))

    menu.update()
    menu.draw_clouds(screen)

    screen.blit(camera_position, (10, 10))
    screen.blit(volume, (10, 46))
    screen.blit(current_track, (10, 82))

    pg.display.flip()
    clock.tick(60)

pg.quit()