#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 11:04:28 2019
#Purpose: Phone number and email address extractor 
@author: janicelove
#From AtBS book ch. 7: pattern matching with Regex
"""
#import packes
import pyperclip 
import re 
    
#Find all phone numbers and email addresses in text
phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))? 
(\s|-|\.)?
(\d{3})
(\s|-|\.)
(\d{4})
(\s*(ext|x|ext.)\s*(\d{2,5}))?
)''',re.VERBOSE)

#regex for email addresses 
emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+
@
[a-zA-Z0-9.-]+
(\.[a-zA-Z]{2,4})

)''', re.VERBOSE)
# Get text off clipboard
text = str(pyperclip.paste())
matches = [] #creates list to store matches 
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups [8] != '':
        phoneNum  += ' x' +groups[8]
    matches.append(phoneNum) #appends results in standard format 

for groups in emailRegex.findall(text):
    matches.append(groups[0])

#Paste results to clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print ('\n'.join(matches))
else:
    print ('No phone numbers or email addresses found.')