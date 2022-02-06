#!/usr/bin/env python
# coding: utf-8

# In[17]:


import random
import string
import keyboard
from time import sleep


lowerletters = string.ascii_lowercase

# printing uppercase
Upperletters = string.ascii_uppercase

# printing letters
Uplowletters = string.ascii_letters

def start():
    while True:  # making a loop
            if keyboard.is_pressed('shift') and keyboard.is_pressed('ctrl') and keyboard.is_pressed('s'):
                keyboard.write(''.join(random.choice(Uplowletters) for i in range(30)) )
                sleep(0.5)

            
            elif keyboard.is_pressed('shift') and keyboard.is_pressed('alt') and keyboard.is_pressed('s'):
                keyboard.write( ''.join(random.choice(Upperletters) for i in range(30)) )
                sleep(0.5)

                
            elif keyboard.is_pressed('shift') and keyboard.is_pressed('s'):  # if key 'q' is pressed 
                keyboard.write( ''.join(random.choice(lowerletters) for i in range(30)))
                sleep(0.5)
            elif keyboard.is_pressed('shift') and keyboard.is_pressed('alt') and keyboard.is_pressed('w'):
                break


start()

