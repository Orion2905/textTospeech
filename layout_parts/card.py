import tkinter as tk
from tkinter import *
from tkinter import ttk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from functions import variables


class Card:
    def __init__(self, parent, icons):
        self.variables = variables.RootOptions()

        self.BACKGROUND_COLOR = self.variables.BACKGROUND_2
        self.BUTTON_BACKGROUND = self.variables.BUTTON_BACKGROUND

        self.FONT_1 = ("Arial", 14)
        self.FONT_5 = ("Arial", 12)

        self.card = ttk.Frame(parent, borderwidth=3, relief=RAISED)

        container = ttk.Frame(self.card)
        container.pack(side=TOP)

        self.image = ttk.Label(container, image=icons['home'], relief=FLAT)
        self.image.pack(pady=4)

        self.title = ttk.Label(container, text="Title")
        self.title.pack()

        self.description = ttk.Label(container, text="This is the description of this frame", font=self.variables.FONT_3)
        self.description.pack()

        self.button = ttk.Button(
            container,
            text="Choose this service".upper(),
            bootstyle='success'
        )
        self.button.pack(padx=10, pady=10)

        self.close = ttk.Button(
            container,
            text="Close".upper(),
            command=self.close,
            image=icons['rounded_x'],
            bootstyle='link'
        )
        self.close.pack( side=RIGHT)

    def close(self):
        self.card.place_forget()

    def place(self):
        self.card.place(
            anchor=CENTER, relx=.5, rely=.68
        )