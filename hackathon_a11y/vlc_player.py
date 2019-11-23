import time
import pathlib

import vlc
import tkinter as tk
from tkinter import ttk

import urllib
import pafy

__all__ = ['VLCplayer']

class VLCplayer(tk.Frame):
    def __init__(self, container, container_instance, title=None):
        
        tk.Frame.__init__(self, container_instance)

        self.container = container
        self.container_instance = container_instance

        self.vlc_instance, self.vlc_player = self.create_vlc_instance()
        self.vlc_instance.log_set(log_callback, None)

        self.video_panel = ttk.Frame(self.container_instance)
        self.canvas = tk.Canvas(self.video_panel, background='black')
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.video_panel.pack(fill=tk.BOTH, expand=True)

    def create_vlc_instance(self):
        vlc_instance = vlc.Instance()
        vlc_player = vlc_instance.media_player_new()
        self.container_instance.update()
        return vlc_instance, vlc_player

    def get_handle(self):
        return self.video_panel.winfo_id()

    def play(self):
        """Plays currnet file."""
        if not self.vlc_player.get_media():
            raise ValueError("No media set")
        else:
            if self.vlc_player.play() == -1:
                pass

    def pause(self):
        """Pause the player."""
        self.vlc_player.pause()

    def stop(self):
        """Stop the player."""
        self.vlc_player.stop()

    def play_film(self, file):
        """Plays a file"""
        if file.startswith('http'):

            v = pafy.new(file)
            v = v.getbest()
            file = urllib.parse.unquote(v.url)

        self.Media = self.vlc_instance.media_new(file)
        self.vlc_player.set_media(self.Media)
        self.vlc_player.set_xwindow(self.get_handle())
        self.play()


@vlc.CallbackDecorators.LogCb
def log_callback(data, level, ctx, fmt, args):
    # with open('debug.txt', 'a') as f:
    #     f.writelines(f"{data}, {level}, {ctx}, {fmt}, {args}\n")
    # print(data, level, ctx, fmt, args)
    pass

class RootContainer:
    def __init__(self):
        self.tk_instance = tk.Tk()
        self.tk_instance.title("main")
        self.tk_instance.geometry("1280x720")

if __name__ == '__main__':

    root = RootContainer()
    player = VLCplayer(root, root.tk_instance, title="VLCplayer")

    player.play_film("http://youtu.be/SDTZ7iX4vTQ")

    root.tk_instance.mainloop()
