from os import path

from tkinter import *

from hackathon_a11y.view import View


class MainView(View):
    def display(self):
        self.window.title("Odtwarzacz")
        self.window.configure(background="#FAE3B4")
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        self.window.geometry(str(screen_width) + 'x' + str(screen_height))
        self.window.smieci = []

        resources_path = path.join(path.dirname(__file__), "../images/")
        resources_path_music = path.join(path.dirname(__file__), "../sounds/")

        b = self.add_image(resources_path + "strzalka.png", 0, 0, 2, 2, 'nw')
        b.sound = resources_path_music + 'wstecz.mp3'
        self.register(b, lambda x : sys.exit(0))
        # self.add_image(resources_path + "spotify.png", 0.2, 0.5, 2, 2, CENTER)
        b = self.add_image(resources_path + "youtube.png", 0.5, 0.5, 2, 2, CENTER)
        b.sound = resources_path_music + 'yt.mp3'
        self.register(b, lambda x : self.change_view(self.parent_controller.views["YoutubeList"]))
        self.add_image(resources_path + "rss.png", 0.8, 0.5, 2, 2, CENTER)

        self.mainloop()

if __name__ == "__main__":
    main_view = MainView(None)
    main_view.display()
