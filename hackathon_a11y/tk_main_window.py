# -*- coding: utf-8 -*-

from tkinter import *

def add_image(window,filename,x,y,subsample_x,subsample_y,anchor):
    photo = PhotoImage(master = window, file = filename)
    photo = photo.subsample(subsample_x, subsample_y)
    button = Button(window, image = photo)
    button.place(relx=x, rely=y, anchor=anchor)
    window.smieci.append(photo)
    
def display():
    window = Tk()
    window.title("Odtwarzacz")
    window.configure(background="#FAE3B4")
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
     
    window.geometry(str(screen_width)+'x'+str(screen_height))
    window.smieci = []

    add_image(window, r"strzalka.png",0,0,2,2,'nw')
    add_image(window, r"spotify.png",0.2,0.5,2,2,CENTER)
    add_image(window, r"youtube.png",0.5,0.5,2,2,CENTER)
    add_image(window, r"rss.png",0.8,0.5,2,2,CENTER)

    window.mainloop()



display()
