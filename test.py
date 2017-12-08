import numpy as np
from capture import grab_screen
from PIL import ImageGrab
import cv2
import time
from directkeys import PressKey, W, A, S, D
import threading
import os
from matplotlib import pyplot as plt

def process_img(image):
    original_image = image
    # convert to gray
    processed_img = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    # edge detection
    processed_img =  cv2.Canny(processed_img, threshold1 = 500, threshold2=200)
    return processed_img



def main():
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)
    o = 0
    last_time = time.time()
    while True:
        #PressKey(W)
        screen =  grab_screen()
        last_time = time.time()
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
        #new_screen = process_img(screen)
        #cv2.imshow('window', screen)
        cv2.imshow('window',screen)
        print('Frame took {} seconds'.format(time.time()-last_time))
        if cv2.waitKey(5) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
        elif cv2.waitKey(5) & 0xFF == ord('s'):
            cv2.imwrite('Editing{}.png'.format(o),screen)
            o = o + 1

main()
