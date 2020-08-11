# -*- coding: utf-8 -*-

#install opencv-python

import shlex
import subprocess
import os
import keyboard
from time import sleep
from collections import OrderedDict

input_method=dict()
input_method['ja_JP'] = 'ibus engine kkc'

def enable_IM(lang):
    '''Enables the input method '''
    ibus_engine = '%s' %(input_method[lang]) 
    command = ibus_engine
    command = shlex.split(command)
    subprocess.call(command)

def input_data(lang):
    if lang == 'ja_JP':
         keyboard.write("aeuaeu")
         sleep(2)
         keyboard.write("aeuaeu")
         keyboard.press_and_release('Enter')
         keyboard.press_and_release('Enter')

def enable_en():
    ibus_engine = "ibus engine xkb:us::eng"
    command = ibus_engine
    command = shlex.split(command)
    subprocess.call(command)
    sleep(2)

def ibus_kkc_package_check():
    try:
        output = subprocess.check_output("rpm -q ibus-kkc", shell=True)
    except subprocess.CalledProcessError as e:
        print('ibus kkc is not installed')
    else:
        print('ibus kkc is installed')

def set_engine():
    try:
        subprocess.check_call("ibus engine kkc", shell=True) 
    except subprocess.CalledProcessError as error:
        print('kkc engine is set')
    subprocess.check_call("ibus engine xkb:us::eng", shell=True)


for lang in input_method.keys():

    ibus_kkc_package_check()
    set_engine()
    #enable_IM(lang)
    #input_data(lang)
    #sleep (5)
    #enable_en()
