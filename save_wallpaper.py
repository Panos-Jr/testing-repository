import ctypes

def get_wallpaper_path():
    SPI_GETDESKWALLPAPER = 0x0073
    MAX_PATH = 260
    wallpaper_path = ctypes.create_unicode_buffer(MAX_PATH)
    ctypes.windll.user32.SystemParametersInfoW(SPI_GETDESKWALLPAPER, MAX_PATH, wallpaper_path, 0)
    return wallpaper_path.value
    
def set_wallpaper(image_path):
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)

set_wallpaper(get_wallpaper_path())