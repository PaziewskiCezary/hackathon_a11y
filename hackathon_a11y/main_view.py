from os import path

from tkinter import *

from .view import View

class MainView(View):
    def add_image(self, window, filename, x, y, subsample_x, subsample_y, anchor):
        photo = PhotoImage(master=window, file=filename)
        photo = photo.subsample(subsample_x, subsample_y)
        button = Button(window, image=photo)
        button.place(relx=x, rely=y, anchor=anchor)
        window.smieci.append(photo)


    def display(self):
        window = Tk()
        window.title("Odtwarzacz")
        window.configure(background="#FAE3B4")
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        window.geometry(str(screen_width) + 'x' + str(screen_height))
        window.smieci = []

        resources_path = path.join(path.dirname(__file__), "../images/")

        self.add_image(window, resources_path + "strzalka.png", 0, 0, 2, 2, 'nw')
        self.add_image(window, resources_path + "spotify.png", 0.2, 0.5, 2, 2, CENTER)
        self.add_image(window, resources_path + "youtube.png", 0.5, 0.5, 2, 2, CENTER)
        self.add_image(window, resources_path + "rss.png", 0.8, 0.5, 2, 2, CENTER)

        window.mainloop()

if __name__ == "__main__":
    main_view = MainView()
    main_view.display()
