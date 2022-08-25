import tkinter as tk
from tkinter import *
from tkinter import ttk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

import datetime
import time


class Clock:
    def __init__(self, frame):
        self.FONT_1 = ("Arial", 10, "bold")
        self.FONT_5 = ("Arial", 12)
        self.FONT_2 = ("Arial", 24, "bold")
        self.FONT_3 = ("Arial", 18)
        self.FONT_4 = ("Impact", 30)

        self.ROOT = frame

        self.clock_box_shadow = ttk.Frame(
            frame, width=140, height=100, bootstyle="primary"
        )
        self.clock_box = ttk.Frame(
            frame,
            width=200, height=100, bootstyle="primary", borderwidth=3,
        )
        print(self.clock_box.winfo_width(), self.clock_box.winfo_height())
        self.date = ttk.Label(
            self.clock_box, text=str(datetime.datetime.now().strftime("%x")),
            font=self.FONT_3, bootstyle="inverse-primary"
        )
        self.date.pack(anchor=CENTER)

        self.clock = ttk.Label(self.clock_box, font=self.FONT_4, bootstyle="inverse-primary")
        self.clock.pack(padx=2, anchor=CENTER)

        # self.clock_box_shadow.place(anchor=W, x=12, y=82, width=157, height=100)
        self.clock_box.place(anchor=W, x=10, rely=.5, width=200, height=110)

        self.digital_clock()

    def digital_clock(self):
        text_input = time.strftime("%H:%M:%S")
        self.clock.config(text=text_input)
        self.clock.after(100, self.digital_clock)
        self.ROOT.update()
