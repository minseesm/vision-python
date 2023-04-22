from PIL import Image
import pyautogui as pag
import time

time.sleep(3) 

filepath = '/Users/vision/academy/python/Python_JJM/Screenshot/images'

for i in range(1, 9):
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    pag.screenshot(f"{filepath}/image{curr_time}.png")
    time.sleep(2)