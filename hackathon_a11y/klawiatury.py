# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 07:03:58 2019

@author: Dell
"""

from tkinter import *
from tkinter import font

keyboard = Tk()

digits_and_freqsym = ['\u2b8c', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
                      '\u2b8c', '-', '/', ':', ';', '(', ')', '$', '&', '@', '\"',
                      '\u2b8c', '.', ',', '?', '!', '\'', '*', '#', 'ABC', 'COFNIJ'
                      '\u2b8c', 'SPACJA', 'COFNIJ']

uppercased = ['\u2b8c', 'Q', 'W', 'E', 'Ę', 'R', 'T', 'Y', 'U', 'I', 'O', 'Ó', 'P',  
              '\u2b8c', 'A', 'Ą', 'S', 'Ś', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Ł',    
              '\u2b8c', 'Z', 'Ź', 'Ż', 'X', 'C', 'Ć', 'V', 'B', 'N', 'Ń', 'M', '123', 
               '\u2b8c', 'SPACJA', 'COFNIJ']    

keyboard_row = 0
keyboard_col = 0

helv30 = font.Font(family='Helvetica', size=30, weight='bold')

for but in uppercased:
    
    if but not in ['SPACJA', 'COFNIJ']:
        Button(keyboard, text=but, width = 4, height = 1, bg="#fae3b4", fg = "#1e4147", font=helv30).grid(row=keyboard_row, column=keyboard_col)  
        keyboard_col +=1
    
    elif but == 'SPACJA':
        Button(keyboard, text=but, width = 26, height = 1, bg="#fae3b4", fg = "#1e4147", font=helv30).grid(row=keyboard_row, column=keyboard_col, columnspan=6) 
        keyboard_col +=6
    elif but == 'COFNIJ':
        Button(keyboard, text=but, width = 13, height = 1, bg="#fae3b4", fg = "#1e4147", font=helv30).grid(row=keyboard_row, column=keyboard_col, columnspan=3) 
        keyboard_col +=1
        
    if keyboard_col == 13:
        keyboard_col = 0
        keyboard_row += 1
    
keyboard.mainloop()


keyboard_row = 0
keyboard_col = 0

keyboard = Tk()

for but in digits_and_freqsym:
    
    if but not in ['SPACJA', 'COFNIJ']:
        Button(keyboard, text=but, width = 4, height = 1, bg="#fae3b4", fg = "#1e4147", font=helv30).grid(row=keyboard_row, column=keyboard_col)  
        keyboard_col +=1
    
    elif but == 'SPACJA':
        Button(keyboard, text=but, width = 26, height = 1, bg="#fae3b4", fg = "#1e4147", font=helv30).grid(row=keyboard_row, column=keyboard_col, columnspan=6) 
        keyboard_col +=6
    elif but == 'COFNIJ':
        Button(keyboard, text=but, width = 13, height = 1, bg="#fae3b4", fg = "#1e4147", font=helv30).grid(row=keyboard_row, column=keyboard_col, columnspan=3) 
        keyboard_col +=3
        
    if keyboard_col == 11:
        keyboard_col = 0
        keyboard_row += 1
    
keyboard.mainloop()