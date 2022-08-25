import time
import tkinter as tk

import database.database
from layout_parts import topbar
from layout_parts import footer
from layout_parts import scrollable_frame
from layout_parts import card
from tkinter import *
from services.facebook import facebook_groups, facebook_gui
from tkinter import ttk
from functions import read_presets, save_actions, variables

from PIL import ImageTk, Image


class Table_1:
    def __init__(self, root, columns):
        self.WINDOW_COLOR = "#dfe4ea"
        self.groups_list_frame = tk.Frame(root, bg=self.WINDOW_COLOR, borderwidth=1)
        self.groups_list_frame.grid_propagate(0)

        # scroll_bar = tk.Scrollbar(self.groups_list_frame)
        columns = columns
        self.groups_list = ttk.Treeview(
            self.groups_list_frame, columns=columns, show="headings", selectmode="extended"
        )
        # define headings
        for i in columns:
            self.groups_list.heading(i, text=i)
            self.groups_list.column(i, minwidth=0, width=50, stretch=YES)

        # add a scrollbar
        scrollbar = ttk.Scrollbar(self.groups_list, orient=tk.VERTICAL, command=self.groups_list.yview, bootstyle="dark-round")
        self.groups_list.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=RIGHT, fill=Y)

        self.groups_list.pack(fill=BOTH, expand=True, side=BOTTOM)

        self.groups_list_frame.pack(fill=BOTH, expand=True, side=BOTTOM)

    def insert(self, items):
        self.groups_list.insert('', tk.END, values=items)
