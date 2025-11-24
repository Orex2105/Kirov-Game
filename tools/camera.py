from settings import Settings


class Camera():
    x = 0
    y = 0

    @classmethod
    def move(cls, mouse_rel):
        mouse_dx, mouse_dy = mouse_rel

        cls.x -= mouse_dx * Settings.MOUSE_SENSITIVITY
        cls.y -= mouse_dy * Settings.MOUSE_SENSITIVITY

    @classmethod
    def check_screen_bezels(cls):
        cls.x = max(0, min(cls.x, Settings.WORLD_WIDTH - Settings.MONITOR_WIDTH))
        cls.y = max(0, min(cls.y, Settings.WORLD_HEIGHT - Settings.MONITOR_HEIGHT))