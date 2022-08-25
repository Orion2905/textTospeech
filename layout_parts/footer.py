import tkinter as tk
from tkinter import *
import datetime

import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class Footer:
    def __init__(self, parent, icons):
        self.BACKGROUND_COLOR = "#1E90FF"
        self.BUTTON_BACKGROUND = "#d1ccc0"

        footer = ttk.Frame(parent, height=16, bootstyle="primary")
        footer.pack(
            side=tk.BOTTOM, fill=tk.BOTH
        )

        ttk.Label(footer, text=f"Copyright © {datetime.datetime.now().year} Social Bear", bootstyle="inverse-primary").pack()
