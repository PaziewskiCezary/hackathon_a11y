# -*- coding: utf-8 -*-
from time import sleep
from tkinter import *

current = None

def add_image(window,filename,x,y,subsample_x,subsample_y,anchor, background, command=None):
    photo = PhotoImage(master = window, file = filename)
    photo = photo.subsample(subsample_x, subsample_y)
    button = Button(window, image = photo, background = background, command=command)
    button.place(relx=x, rely=y, anchor=anchor)
    window.smieci.append(photo)
    return button
    
def display():
    window = Tk()
    window.title("Odtwarzacz")
    window.configure(background="#FAE3B4")
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
     
    window.geometry(str(screen_width)+'x'+str(screen_height))
    window.smieci = []

    arrow = add_image(window, r"strzalka.png",0,0,2,2,'nw', "#FAE3B4")
    spotify = add_image(window, r"spotify.png",0.2,0.5,2,2,CENTER, "#FAE3B4")
    youtube = add_image(window, r"youtube.png",0.5,0.5,2,2,CENTER, "#FAE3B4")
    rss = add_image(window, r"rss.png",0.8,0.5,2,2,CENTER, "#FAE3B4")
    
    buttons_list = [arrow, spotify, youtube, rss]
    window.update_idletasks()
    window.update()
    n = 1
    
    funcs = [helloCallBack, helloCallBack2, helloCallBack3, helloCallBack4]
    
    while(n < 3):
        for butt, fu  in zip(buttons_list, funcs):
            current = butt
            breakpoint()
            butt.config(background = "black", command=fu)
            window.update_idletasks()
            window.update()
            sleep(2)
            butt.config(background = "#FAE3B4", command=None)
            window.update_idletasks()
            window.update()
        n += 1
    window.mainloop()
    
def helloCallBack():
    messagebox.showinfo("blabla")
    
def helloCallBack2():
    messagebox.showinfo("dupa")

def helloCallBack3():
    messagebox.showinfo("zupa")

def helloCallBack4():
    messagebox.showinfo("lulululu")
    
def pasik():
    pass

display()



    