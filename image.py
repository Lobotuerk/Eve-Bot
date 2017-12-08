import cv2
import numpy as np
import win32gui, win32ui, win32con, win32api
from PIL import ImageGrab
from matplotlib import pyplot as plt
from capture import grab_screen

#img = grab_screen()
img = cv2.imread('Editing0.png')
plt.imshow(img)
plt.show()
