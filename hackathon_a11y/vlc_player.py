import vlc
import tkinter as tk
from tkinter import ttk

import urllib
import pafy

from hackathon_a11y.youtube_view import YoutubeView

__all__ = ['VLCplayer']

class VLCplayer(tk.Frame):
    def __init__(self, container):
        tk.Frame.__init__(self, container)
        self.container = container

        self.vlc_instance, self.vlc_player = self.create_vlc_instance()

        self.video_panel = ttk.Frame(self.container)
        self.canvas = tk.Canvas(self.video_panel, background='black')
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.video_panel.pack(fill=tk.BOTH, expand=True)

    def create_vlc_instance(self):
        vlc_instance = vlc.Instance()
        vlc_player = vlc_instance.media_player_new()
        self.container.update()
        return vlc_instance, vlc_player

    def get_handle(self):
        return self.video_panel.winfo_id()

    def play(self):
        """Plays current file."""

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


if __name__ == '__main__':
    root = YoutubeView()
    player = VLCplayer(root.window)

    player.play_film("http://youtu.be/SDTZ7iX4vTQ")

    root.window.mainloop()
