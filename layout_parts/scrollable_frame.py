import tkinter as tk
from tkinter import *
from tkinter import ttk
import customtkinter


class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = customtkinter.CTkCanvas(self, width=158, height=350, background="#1B1B1B")
        scrollbar = tk.Scrollbar(self, orient="vertical", command=canvas.yview, bg="#1B1B1B", troughcolor="#1B1B1B")
        self.scrollable_frame = customtkinter.CTkFrame(canvas, background="#1B1B1B")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill=BOTH, expand=True)
        scrollbar.pack(side="right", fill="y")


class ScrollableFrame_x(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = customtkinter.CTkCanvas(self, height=84, width=400, background="#D9D9D9")
        scrollbar = tk.Scrollbar(self, orient="horizontal", command=canvas.xview, background="#D9D9D9")
        self.scrollable_frame = customtkinter.CTkFrame(canvas, background="#D9D9D9")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(xscrollcommand=scrollbar.set)

        canvas.pack(side="bottom", fill=BOTH, expand=True)
        scrollbar.pack(side="bottom", fill="x")
