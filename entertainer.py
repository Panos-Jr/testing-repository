import ctypes
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import numpy as np
import os
import sys
from playsound import playsound
import pygame
import shutil
from tkinter import *
from tkinter import messagebox
import winsound


def show_warning_popup():
    root = Tk()
    root.withdraw()
    messagebox.showwarning("Warning", "Please wear headphones!")

def show_info():
    messagebox.showinfo('Enjoy the joke?', 'Let me fix that wallpaper for you, just press \'OK\'')

def set_wallpaper(image_path):
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)

def volume(desired_vol):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    vol_range = volume.GetVolumeRange()
    min_vol = vol_range[0]
    max_vol = vol_range[1]
    desired_vol_db = np.interp(desired_vol, [0, 100], [min_vol, max_vol])
    volume.SetMasterVolumeLevelScalar(desired_vol / 100, None)

def get_wallpaper_path():
    SPI_GETDESKWALLPAPER = 0x0073
    MAX_PATH = 260
    wallpaper_path = ctypes.create_unicode_buffer(MAX_PATH)
    ctypes.windll.user32.SystemParametersInfoW(SPI_GETDESKWALLPAPER, MAX_PATH, wallpaper_path, 0)
    return wallpaper_path.value

def play_mp3(mp3_path):
    volume(100)
    winsound.PlaySound(mp3_path, winsound.SND_FILENAME)

if getattr(sys, 'frozen', False):
    script_directory = sys._MEIPASS
else:
    script_directory = os.path.dirname(os.path.abspath(__file__))

show_warning_popup()
wallpaper_path = get_wallpaper_path()
image_path = os.path.join(script_directory, "wallpaper.jpg")
set_wallpaper(image_path)
mp3_path = os.path.join(script_directory, 'output.wav')
play_mp3(mp3_path)
show_info()
set_wallpaper(wallpaper_path)
volume(60)