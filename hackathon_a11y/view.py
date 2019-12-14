import os
import tkinter as tk
from abc import abstractmethod

from hackathon_a11y.user_settings import UserSettings

class View:
    """
    Abstract class to represent a window

    Static attribute:
        user_settings : UserSettings
            Containts info specific to user, e.g. time between elements
            to highlight

    Attributes:
        highlighted_element : GUI Element
        highlight_cycle : List[GUI Element]
            List of elements to highlight
        action_map : Dictionary GUI Element -> Function
            If key-event is detected, function action_map[highlighted_element]
            is called with highlighted_element as its argument
    """
    user_settings = UserSettings()

    def __init__(self, parent_controller):
        self.parent_controller = parent_controller
        self.highlightable = []
        self.highlighted_element = None
        self.actions = dict()

        self.window = tk.Tk()
        self.window.bind('<Return>', self.select)
        self.window.title("Odtwarzacz")
        self.window.configure(background="#FAE3B4")
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        self.window.geometry(str(screen_width) + 'x' + str(screen_height))
        self.window.smieci = []

    def change_view(self, new_view_class, *args, **kwargs):
        self.window.after_cancel(self.task)
        self.window.destroy()
        new_window = new_view_class(self.parent_controller, *args, **kwargs)
        new_window.display()

    def select(self, event):
        return self.actions[self.highlighted_element](self.highlighted_element)

    def add_image(self, filename, x, y, subsample_x, subsample_y, anchor):
        photo = tk.PhotoImage(master=self.window, file=filename)
        photo = photo.subsample(subsample_x, subsample_y)
        button = tk.Button(self.window, image=photo)
        button.place(relx=x, rely=y, anchor=anchor)
        self.window.smieci.append(photo) # To make it not garbage collected since tkinter will not show it otherwise
        return button

    def mainloop(self):
        #self.window.mainloop()
        butts = self.highlightable
        i = 0
        butt = butts[i]
        self.highlighted_element = butt
        butt.config(background="black")

        def highlight_next_item(self, i):
            butts = self.highlightable
            if i >= len(butts): # list could have shrunk in the meantime
                i = 0
            self.highlighted_element.config(background="#FAE3B4")
            i = (i + 1) % len(butts)
            butt = butts[i]
            self.highlighted_element = butt
            butt.config(background="black")
            self.window.update_idletasks()
            self.window.update()
            try:
                os.system("mplayer " + butt.sound)
            except Exception:
                pass
            self.task = self.window.after(self.user_settings.highlight_time, lambda : highlight_next_item(self, i))


        self.window.after(self.user_settings.highlight_time, lambda : highlight_next_item(self, i))
        self.window.mainloop()


    def register(self, button, action):
        self.highlightable.append(button)
        self.actions[button] = action

    def unregister(self, button):
        self.highlightable.remove(button)
        self.actions.pop(button)

    @abstractmethod
    def display(self):
        """
        Creates and displays the window; starts highlightning cycle

        :return: None
        """
        pass

