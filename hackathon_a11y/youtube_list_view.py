import tempfile
import time
import tkinter as tk
import urllib.request
from os import path

from PIL import Image

from hackathon_a11y.view import View
from hackathon_a11y.youtube_controller import YoutubeController

class YoutubeListView(View):

    controller = YoutubeController()
    tempdir = tempfile.gettempdir()
    timer = time.time()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.videos = [] # List of pairs (Video descriptor : dictionary, its tk GUI Element)

    def reset_list(self):
        for v, l in self.videos:
            self.unregister(l)
            l.destroy()
        self.videos = []

    def show_video(self, video_desc):
        """
        Adds a video description to the shown list

        :param video_desc: element of the "items" list from YT API v3 JSON response
        :return: None
        """
        print(video_desc)

        gui = tk.Frame(self.window)
        gui.grid(row=len(self.videos) + 1, sticky="w") # 1 for search bar

        # Thumbnail
        thumbnail_url = video_desc["snippet"]["thumbnails"]["default"]["url"]
        filename = path.join(self.tempdir, "AAA.jpg")
        urllib.request.urlretrieve(thumbnail_url, filename)
        im = Image.open(filename)
        im.save(filename+".png")
        thumbnail = tk.PhotoImage(master=gui, file=filename+".png")
        thumbnail = thumbnail.subsample(1, 1)
        gui.thumbnail = thumbnail
        gui.button = tk.Button(gui, image=thumbnail).grid(rowspan=2, column=0, sticky="e")

        gui.title_label = tk.Label(gui, text=video_desc["snippet"]["title"]).grid(row=0, column=1, sticky="w")
        gui.desc_label = tk.Label(gui, text=video_desc["snippet"]["description"]).grid(row=1, column=1, sticky="w")

        self.videos.append((video_desc, gui))
        try:
            video_id = video_desc["id"]["videoId"]
            self.register(gui, lambda x : self.change_view(self.parent_controller.views["Youtube"], video_id))
        except KeyError:
            pass # lol
        self.window.update()


    def display(self):
        self.query = tk.StringVar()
        self.query.trace("w", lambda l, idx, mode: self.update_results())
        entry = tk.Entry(self.window, textvariable=self.query, font="arial 80 ", justify="center", fg="black")
        # entry.place(relx=0.25, rely=0.90, height=100, width=100)
        entry.focus_set()
        entry.grid(row=0, sticky="n")

        resources_path = path.join(path.dirname(__file__), "../images/")
        b = self.add_image(resources_path + "strzalka.png", 0.1, 1.0, 2, 2, "s")
        self.register(b, lambda x : self.change_view(self.parent_controller.views["Main"]))

        self.mainloop()

    def update_results(self):
        if time.time() - self.timer > 1.0: # to be safe xD
            query = self.query.get()
            self.reset_list()
            try:
                results = self.controller.search(query)["items"]
                for result in results:
                    self.show_video(result)
            except KeyError:
                pass

            self.timer = time.time()
            self.window.update()


if __name__ == "__main__":
    youtube_list_view = YoutubeListView(None)
    youtube_list_view.display()
