import tkinter as tk
from tkinter import *
import service_chooser
from user import profile, settings
from functions.variables import RootOptions
from tkinter import ttk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class TopBar:
    def __init__(self, parent, icons, parent_2):
        self.variables = RootOptions()


        self.style = ttk.Style()

        self.icons = icons
        self.home_image = tk.PhotoImage(file=r"images/topbar/home (2).png").subsample(1, 1)
        self.sun = tk.PhotoImage(file=r"images/topbar/sun.png"),
        self.moon = tk.PhotoImage(file=r"images/topbar/moon.png")
        self.expand_img = tk.PhotoImage(file=r"images/topbar/list.png")
        self.cross = tk.PhotoImage(file=r"images/topbar/cross.png")
        self.expand = tk.PhotoImage(file=r"images/topbar/list.png")
        self.firefox_img = tk.PhotoImage(file=r"images/topbar/firefox.png")
        self.chrome = tk.PhotoImage(file=r"images/topbar/chrome.png")
        self.firefox_img_2 = tk.PhotoImage(file=r"images/topbar/firefox2.png")
        self.chrome_2 = tk.PhotoImage(file=r"images/topbar/chrome2.png")

        self.BACKGROUND_COLOR = self.variables.BLUE_1
        self.BUTTON_BACKGROUND = self.variables.BLUE_2

        self.PARENT = parent
        self.PARENT_2 = parent_2
        self.height, self.width = self.PARENT.winfo_height(), self.PARENT.winfo_width()

        topbar = ttk.Frame(parent, bootstyle="primary", width=100)
        topbar.pack(
            side=tk.LEFT, fill=tk.BOTH
        )

        self.mode_bar = "close"
        self.expand = ttk.Button(
            topbar, image=self.expand_img, bootstyle="primary",
            command=self.expand_bar
        )
        self.expand.pack(side=TOP)

        self.mode_browser = "firefox"
        self.firefox = ttk.Button(
            topbar, image=self.firefox_img, bootstyle="primary",
            command=self.set_browser, text="Firefox"
        )
        self.firefox.pack()

        container = ttk.Frame(topbar, bootstyle="primary")
        container.pack(side=LEFT)

        self.home = ttk.Button(
            container, image=self.home_image, bootstyle="primary", text="Home",
            command=self.go_home
        )
        self.home.grid(row=0, column=0, pady=5)

        self.profile = ttk.Button(
            container, image=self.icons["user"], bootstyle="primary",
            command=self.go_profile, text="Profile"
        )
        self.profile.grid(row=1, column=0, pady=5)

        self.mode = "sun"
        self.option_2 = ttk.Button(
            container, image=self.sun, bootstyle="primary", command=self.set_mode, text="Light"
        )
        self.option_2.grid(row=2, column=0, pady=5)

        self.settings = ttk.Button(
            container, image=self.icons["settings"], bootstyle="primary",
            command=self.settings, text="Settings"
        )
        self.settings.grid(row=3, column=0, pady=5)

        self.exit = ttk.Button(
            container, image=self.icons["rounded_x"], bootstyle="primary",
            command=parent.destroy, text="Exit"
        )
        self.exit.grid(row=4, column=0, pady=5)

        logo = ttk.Button(
            topbar, image=self.icons["logo"], bootstyle="primary",
        )
        logo.place(relx=.9, rely=.20)

    def go_home(self):
        self.PARENT.destroy()
        try:
            service_chooser.run()
        except Exception as e:
            self.PARENT.destroy()

    def go_profile(self):
        self.PARENT.destroy()
        try:
            service_chooser.run('profile')
        except Exception as e:
            self.PARENT.destroy()

    def settings(self):
        self.PARENT.destroy()
        try:
            service_chooser.run('settings')
        except Exception as e:
            self.PARENT.destroy()

    def set_mode(self):
        print(self.mode)
        if self.mode == "sun":
            self.option_2['image'] = self.moon
            self.option_2.config(text="Dark")
            self.mode = "moon"

            # instantiate the style with another theme
            self.style = ttk.Style(theme='superhero')
            # self.main_root.message_box_frame(bootstyle="light")
        else:
            self.option_2['image'] = self.sun
            self.option_2.config(text="Light")
            self.mode = "sun"

            # instantiate the style with another theme
            self.style = ttk.Style(theme='cosmo')

    def set_browser(self):
        print(self.mode)
        if self.mode_browser == "firefox":
            self.firefox['image'] = self.chrome
            self.firefox.config(text="Chrome")
            self.mode_browser = "chrome"
            try:
                self.PARENT_2.start_button.config(text="Run with CHROME".upper(), image=self.chrome_2)
            except:
                pass

        else:
            self.firefox['image'] = self.firefox_img
            self.firefox.config(text="Firefox")
            self.mode_browser = "firefox"
            try:
                self.PARENT_2.start_button.config(text="Run with FIREFOX".upper(), image=self.firefox_img_2)
            except:
                pass

    def expand_bar(self):
        print(self.mode)
        if self.mode_bar == "close":
            self.expand['image'] = self.cross
            self.mode_bar = "open"
            self.home.config(compound=LEFT)
            self.profile.config(compound=LEFT)
            self.option_2.config(compound=LEFT)
            self.settings.config(compound=LEFT)
            self.exit.config(compound=LEFT)
            self.firefox.config(compound=LEFT)
            self.PARENT.geometry(f"{self.width+45}x{self.height}")
        else:
            self.expand['image'] = self.expand_img
            self.mode_bar = "close"
            self.home.config(compound=NONE)
            self.profile.config(compound=NONE)
            self.option_2.config(compound=NONE)
            self.settings.config(compound=NONE)
            self.exit.config(compound=NONE)
            self.firefox.config(compound=NONE)
            self.PARENT.geometry(f"{self.width}x{self.height}")

