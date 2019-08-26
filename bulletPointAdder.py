#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 09:02:16 2019
#bulletPointAdder.py -Adds Wikipedia bullet points to the start of each line of text
@author: janicelove
"""

import pyperclip #installation issues: https://stackoverflow.com/questions/41247045/how-to-install-pyperclip-to-anaconda
text = pyperclip.paste()

# Separate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)):     #loop through all indexes in 'lines' list
    lines[i] = '*' + lines[i] #add star to each string in 'lines' list
    text = '\n'.join(lines)
pyperclip.copy(text)
