# ================ MODULES ================ #

# ================ tkinter ================ #
import tkinter as tk
from tkinter import *
from tkinter import ttk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import filedialog, simpledialog, messagebox
# ================ tkinter ================ #

# ================ program functions ================ #
from functions import read_presets, variables, errors
from services.facebook.facebook_login import FacebookBot
from layout_parts import topbar, clock, set_schedule, footer, csv_table
from services.facebook.facebook_groups_name import FacebookBotGroupsInfo
# ================ program functions ================ #

# ================ others ================ #
import datetime
import time
import random
import threading
# ================ others ================ #

# ================ MODULES ================ #


class SetTime:
    def __init__(self, root, parent):
        self.ROOT = root
        self.WINDOW_SIZE = "420x150"
        self.variables = variables.RootOptions()

        # ================== ROOT OPTIONS =================== #
        root.geometry(self.WINDOW_SIZE)
        root.resizable(False, False)
        # self.icon = ImageTk.PhotoImage(file="logo1.ico")
        root.iconbitmap(self.variables.ROOT_ICON)
        root.title(self.variables.ROOT_TITLE + " - Set time")
        # ================== ROOT OPTIONS =================== #

        self.time_box_frame = ttk.Frame(root)
        self.FONT_1 = ("Arial", 10, "bold")

        ttk.Label(self.time_box_frame, text="Choose time", font=self.FONT_1).pack()

        self.select_time_box = tk.Frame(self.time_box_frame)
        self.select_title = tk.Frame(self.select_time_box)
        self.select_time = tk.Frame(self.select_time_box)

        # ttk.Label(self.select_title, text="    N groups", justify=RIGHT).grid(row=0, column=2, sticky=W)
        hours = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
        minutes = [i for i in range(60)]
        for i in minutes:
            if i < 10:
                minutes[i] = "0"+str(i)

        self.hour_entry = ttk.Combobox(
            self.select_time, width=3, justify=CENTER, font=self.FONT_1, state="readonly", values=hours
        )
        self.hour_entry.set("Hours")

        self.minute_entry = ttk.Combobox(
            self.select_time, width=3, justify=CENTER, font=self.FONT_1, state="readonly", values=minutes
        )
        self.minute_entry.set("Minutes")

        self.seconds_entry = ttk.Combobox(
            self.select_time, width=3, justify=CENTER, font=self.FONT_1, state="readonly", values=minutes
        )
        self.seconds_entry.set("Seconds")

        self.hour_entry.grid(row=1, column=0)
        self.minute_entry.grid(row=1, column=1, padx=2)
        self.seconds_entry.grid(row=1, column=2)

        tk.Label(self.select_time, text="Hours").grid(row=2, column=0)
        tk.Label(self.select_time, text="Minute").grid(row=2, column=1)
        tk.Label(self.select_time, text="Seconds").grid(row=2, column=2)

        time_mode = ["AM", "PM"]

        self.date_filter_entry = ttk.Combobox(
            self.select_time, width=5, font=self.FONT_1, state="readonly", values=time_mode
        )
        self.date_filter_entry.grid(row=1, column=4)
        self.date_filter_entry.set("Choose mode")

        self.select_time.pack(fill=X)
        self.select_time_box.pack()

        self.time_box_frame.pack()

        # Add Button and Label
        ttk.Button(
            root, text="Set Date",
            width=20,
            command=self.set_time
        ).pack(pady=5)

        footer.Footer(root, icons=[])

        self.PARENT = parent

    def set_time(self):
        self.PARENT.pick_time.configure(state=ACTIVE)
        self.PARENT.pick_time.delete(
            0,
            END
        )
        self.PARENT.pick_time.insert(
            0, f"{self.hour_entry.get()}:{self.minute_entry.get()}:{self.seconds_entry.get()} {self.date_filter_entry.get()}"
        )
        self.PARENT.pick_time.configure(state=READONLY)



def run(parent):
    root = ttk.Toplevel()
    main = SetTime(root, parent)
    root.mainloop()