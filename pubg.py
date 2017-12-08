import numpy as np
from grabscreen import grab_screen
from PIL import ImageGrab
import cv2
import time
from directkeys import PressKey, W, A, S, D
import threading
import os

t = 0
tsave = False

def printit():
    global tsave
    threading.Timer(5.0, printit).start()
    tsave = True
    print('saved')

def process_img(image):
    original_image = image
    # convert to gray
    processed_img = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    # edge detection
    processed_img =  cv2.Canny(processed_img, threshold1 = 500, threshold2=200)
    return processed_img

file_name = 'training_data.npy'

if os.path.isfile(file_name):
    print('File exists, loading previous data!')
    training_data = list(np.load(file_name))
else:
    print('File does not exist, starting fresh!')
    training_data = []



def main():
    global t
    global tsave
    printit()
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)

    last_time = time.time()
    while True:
        #PressKey(W)
        screen =  grab_screen(region=(0,40,1280,760))
        last_time = time.time()
        new_screen = process_img(screen)
        cv2.imshow('window', new_screen)
        print('Frame took {} seconds'.format(time.time()-last_time))
        #cv2.imshow('window',cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        if tsave:
            print('Saved state')
            datascreen = cv2.resize(new_screen, (160,120))
            training_data.append([datascreen,t])
            ImageGrab.grab(bbox=(0,40,1280,760)).save("n{}.jpeg".format(t),"JPEG")
            np.save(file_name,training_data)
            t = t + 1
            tsave = False
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

main()
