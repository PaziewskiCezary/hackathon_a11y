from tkinter import ttk
from os import path

import vlc
import urllib
import pafy

from hackathon_a11y.view import View


class YoutubeView(View):
    """
    Class representing a window of YouTube app

    Static attribute:
        controller : YouTubeController
    """
    def __init__(self, video_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.video_id = video_id

    def display(self):
        self.create_vlc_instance()

        self.video_panel = ttk.Frame(self.window)
        # self.video_panel.pack(fill=tk.BOTH, expand=True)
        self.play_film("https://youtu.be/" + self.video_id)
        self.video_panel.place(relheight=0.8, relwidth=1.0, relx=0.0, rely=0.0, anchor="nw")

        resources_path = path.join(path.dirname(__file__), "../images/")

        b = self.add_image(resources_path + "strzalka.png", 0.1, 1.0, 2, 2, "s")
        self.register(b, lambda x : self.change_view(self.parent_controller.views["YoutubeList"]))
        b = self.add_image(resources_path + "pauza.png", 0.3, 1.0, 4, 4, "s")
        self.register(b, lambda x : self.pause())
        b = self.add_image(resources_path + "start.png", 0.5, 1.0, 4, 4, "s")
        self.register(b, lambda x : self.play())
        b = self.add_image(resources_path + "przod.png", 0.7, 1.0, 4, 4, "s")
        self.register(b, lambda x : self.forward())
        b = self.add_image(resources_path + "tyl.png", 0.9, 1.0, 4, 4, "s")
        self.register(b, lambda x: self.back())

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

    def back(self):
        """Move 30s back in time"""
        self.vlc_player.set_time(self.vlc_player.get_time() - 30 * 1000)

    def forward(self):
        """Move 30s forward in time"""
        self.vlc_player.set_time(self.vlc_player.get_time() + 30 * 1000)

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
    youtube_view = YoutubeView("axVvZrDz60k", None)
    youtube_view.display()
