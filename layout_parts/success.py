# https://dribbble.com/shots/1237618--Gif-Spinner
from pathlib import Path
from itertools import cycle
from tkinter import ttk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk, ImageSequence
from functions import variables


class Success:
    def __init__(self, root):

        self.ROOT = root
        self.WINDOW_SIZE = "420x150"
        self.variables = variables.RootOptions()

        # ================== ROOT OPTIONS =================== #
        root.geometry(self.WINDOW_SIZE)
        root.resizable(False, False)
        # self.icon = ImageTk.PhotoImage(file="logo1.ico")
        root.iconbitmap(self.variables.ROOT_ICON)
        root.title(self.variables.ROOT_TITLE + " - SUCCESS!")
        # ================== ROOT OPTIONS =================== #

        # open the GIF and create a cycle iterator
        file_path = "images/test2.gif"
        with Image.open(file_path) as im:
            # create a sequence
            sequence = ImageSequence.Iterator(im)
            images = [ImageTk.PhotoImage(s) for s in sequence]
            self.image_cycle = cycle(images)

            # length of each frame
            self.framerate = im.info["duration"]

        self.img_container = ttk.Label(root, image=next(self.image_cycle))
        self.img_container.pack(fill="both", expand="yes", side=LEFT, padx=20, pady=(0, 0))

        ttk.Label(
            root, text="SUCCESS!!", font=("Impact", 30), bootstyle="success"
        ).place(relx=.4)

        self.message = ttk.Label(
            root, text="Lorem ipsum dolor sit amet, \nconsectetur adipiscing elit."
        ).place(relx=.4, rely=.5)

        root.after(self.framerate, self.next_frame)

    def next_frame(self):
        """Update the image for each frame"""
        self.img_container.configure(image=next(self.image_cycle))
        self.ROOT.after(self.framerate, self.next_frame)


def run():
    root = ttk.Toplevel()
    main = Success(root)
    root.mainloop()
