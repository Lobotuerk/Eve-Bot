import cv2
import numpy as np
import win32gui, win32ui, win32con, win32api
from PIL import ImageGrab
from matplotlib import pyplot as plt

def grab_screen():
    hwin = win32gui.FindWindow(None, 'EVE - Lobo Lelouch')
    #win32gui.SetForegroundWindow(hwin)
    dimensions = win32gui.GetWindowRect(hwin)
    img = np.array(ImageGrab.grab(dimensions))
    return img
