import tkinter as tk
from tkinter import ttk
from os import path

import vlc
import urllib
import pafy

from hackathon_a11y.youtube_controller import YoutubeController
from hackathon_a11y.view import View
from hackathon_a11y.main_view import MainView


class YoutubeView(View):
    """
    Class representing a window of YouTube app

    Static attribute:
        controller : YouTubeController
    """
    controller = YoutubeController()

    def display(self):
        self.create_vlc_instance()

        self.video_panel = ttk.Frame(self.window)
        # self.video_panel.pack(fill=tk.BOTH, expand=True)
        self.play_film("https://youtu.be/dzsuE5ugxf4") # DEBUG
        self.video_panel.place(relheight=0.8, relwidth=1.0, relx=0.0, rely=0.0, anchor="nw")

        resources_path = path.join(path.dirname(__file__), "../images/")

        b = self.add_image(resources_path + "strzalka.png", 0.2, 1.0, 2, 2, "s")
        self.register(b, lambda x : self.change_view(MainView))
        b = self.add_image(resources_path + "przod.png", 0.4, 1.0, 4, 4, "s")
        self.register(b, lambda x : self.stop())
        b = self.add_image(resources_path + "pauza.png", 0.6, 1.0, 4, 4, "s")
        self.register(b, lambda x : self.pause())
        b = self.add_image(resources_path + "start.png", 0.8, 1.0, 4, 4, "s")
        self.register(b, lambda x : self.play())

        self.mainloop()

    def create_vlc_instance(self):
        self.vlc_instance = vlc.Instance()
        self.vlc_player = self.vlc_instance.media_player_new()
        self.window.update()

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

        if file.startswith("http"):
            if "yout" in file:
                v = pafy.new(file)
                v = v.getbest()
                file = urllib.parse.unquote(v.url)
            elif "spotify" in file:
                file = urllib.parse.unquote(file)

        self.Media = self.vlc_instance.media_new(file)
        self.vlc_player.set_media(self.Media)
        self.vlc_player.set_xwindow(self.get_handle())
        self.play()


if __name__ == "__main__":
    youtube_view = YoutubeView()
    youtube_view.display()
