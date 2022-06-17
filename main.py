import os
import datetime
import pyautogui

directory = os.getcwd()

def folder():
    if not os.path.exists('screenshot'):
        folder = os.path.join(directory, 'screenshot')
        os.mkdir(folder)
        print('created folder')

def screenshot():
    folder()
    image = pyautogui.screenshot()
    name = str(datetime.datetime.now())
    image.save('{}/screenshot/{}.png'.format(directory, name))
    print('Save screenshot: \'{}.png\''.format(name))

screenshot()