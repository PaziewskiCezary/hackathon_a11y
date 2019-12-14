import tkinter as tk
from tkinter import font
from os import path

from hackathon_a11y.view import View

resources_path_music = path.join(path.dirname(__file__), "../sounds/")


class YouTubeKeyboardView(View):
    def show_keyboard(self, keyboard):
        uppercased = ['\u2b8c', 'A', '1', 'W', 'E', 'Ę', 'R', 'T', 'Y', 'U', 'I', 'O', 'P',
                       '\u2b8c', 'Q', 'Ą', 'S', 'Ś', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Ł',
                       '\u2b8c', 'Z', 'Ź', 'Ż', 'X', 'C', 'Ć', 'V', 'B', 'N', 'Ń', 'M', 'Ó',
                       '\u2b8c', 'SPACJA', 'COFNIJ']
        keyboard_row = 0
        keyboard_col = 0

        helv30 = font.Font(family='Helvetica', size=30, weight='bold')

        for i, character in enumerate(uppercased):
            b = None

            if character not in ['SPACJA', 'COFNIJ']:
                b = tk.Button(keyboard, text=character, width=2, height=1, bg="#fae3b4", fg="#1e4147", font=helv30)
                b.grid(row=keyboard_row, column=keyboard_col)
                keyboard_col += 1

            elif character == 'SPACJA':
                b = tk.Button(keyboard, text=character, width=13, height=1, bg="#fae3b4", fg="#1e4147", font=helv30)
                b.grid(
                    row=keyboard_row, column=keyboard_col, columnspan=6)
                keyboard_col += 6
            elif character == 'COFNIJ':
                b = tk.Button(keyboard, text=character, width=13, height=1, bg="#fae3b4", fg="#1e4147", font=helv30)
                b.grid(
                    row=keyboard_row, column=keyboard_col, columnspan=3)
                keyboard_col += 1

            if keyboard_col == 13:
                keyboard_col = 0
                keyboard_row += 1

            try:
                b.sound = path.join(resources_path_music, "{}.mp3".format(character.lower()))
            except AttributeError:
                print(character)

            if character == "SPACJA":
                character = " "

            b.character = character
            entry = self.entry

            if character == "COFNIJ":
                self.register(b, lambda x : entry.delete(len(entry.get()) - 1, len(entry.get())))
            elif character == "\u2b8c":
                self.register(b, lambda x : self.go_out())
            else:
                self.register(b, lambda x : entry.insert(len(entry.get()), x.character))

            self.window.smieci.append(b)
            self.window.update()

    def display(self):
        # powinna być w jakiejś nadklasie
        self.query = tk.StringVar()
        self.entry = tk.Entry(self.window, textvariable=self.query, font="arial 80 ", justify="center", fg="black")
        # entry.place(relx=0.25, rely=0.90, height=100, width=100)
        self.entry.focus_set()
        self.entry.grid(row=0, sticky="n")

        resources_path = path.join(path.dirname(__file__), "../images/")
        b = self.add_image(resources_path + "strzalka.png", 0.1, 1.0, 2, 2, "s")
        b.sound = path.join(resources_path_music, "wstecz.mp3")
        self.register(b, lambda x: self.go_out())

        keyboard = tk.Frame(self.window)
        keyboard.grid(row=1, sticky="s")
        self.show_keyboard(keyboard)

        self.mainloop()

    def go_out(self):
        self.change_view(self.parent_controller.views["YoutubeList"], query=self.entry.get())


if __name__ == "__main__":
    youtube_keyboard_view = YouTubeKeyboardView(None)
    youtube_keyboard_view.display()
