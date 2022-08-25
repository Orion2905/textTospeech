import time
import tkinter
import tkinter.messagebox
import tkinter.filedialog
import customtkinter
from layout_parts import scrollable_frame
from tkinter import PhotoImage
from tkinter import *
from tkinter import ttk
from tkinter import font
import PyPDF2
import pyttsx3
import threading
import datetime
import pygame
import soundfile as sf


# customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
# customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


class Footer:
    def __init__(self, parent):
        footer = customtkinter.CTkFrame(
            parent, height=30, fg_color="#5C7AFF", corner_radius=0
        )

        customtkinter.CTkLabel(footer, text=f"Copyright © {datetime.datetime.now().year} OrionDev").pack()

        footer.pack(side=BOTTOM, fill=X)


class Header:
    def __init__(self, parent):
        frame = customtkinter.CTkFrame(
            parent, height=200, fg_color="#5C7AFF", corner_radius=0
        )

        self.mic_icon = tkinter.PhotoImage(file="microphone.png")
        self.back_icon = tkinter.PhotoImage(file="undo.png")
        self.close_icon = tkinter.PhotoImage(file="cross-circle (4).png")

        customtkinter.CTkButton(
            frame, text=None, fg_color=None, width=32, command=lambda: self.back(parent), image=self.back_icon
        ).pack(side=LEFT, padx=15, pady=10)

        # menu_btn = ttk.Menubutton(
        #     frame, width=32, image=self.mic_icon
        # )
        # menu_btn.menu = Menu(menu_btn, tearoff=0)
        # menu_btn["menu"] = menu_btn.menu
        # menu_btn.menu.add_checkbutton(
        #     label="mayo", variable="Ciao"
        # )
        # menu_btn.menu.add_checkbutton(label="ketchup",
        #                         variable="ketchVar")
        # menu_btn.pack(side=LEFT, pady=10, padx=10)

        customtkinter.CTkButton(
            frame, text=None, fg_color=None, width=32, command=lambda: self.close(parent), image=self.close_icon
        ).pack(side=RIGHT, padx=15)

        frame.pack(side=TOP, fill=X)

    def close(self, parent):
        parent.on_closing()

    def back(self, parent):
        parent.main_app()

    def choose_voice(self):
        pass


class FirstWindow(customtkinter.CTk):
    WIDTH = 700
    HEIGHT = 600
    pygame.init()

    def __init__(self):
        super().__init__()

        self.audio_time = "00:00 / 00:00"
        self.elapsed_time = "55:00"
        self.audio_title = "No file created"

        self.play_icon = tkinter.PhotoImage(file="play.png")
        self.pause_icon = tkinter.PhotoImage(file="pause.png")
        self.stop_icon = tkinter.PhotoImage(file="stop (1).png")

        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        self.title("TEXT to speech".upper())
        self.geometry(f"{FirstWindow.WIDTH}x{FirstWindow.HEIGHT}")
        # self.minsize(App.WIDTH, App.HEIGHT)
        self.resizable(False, False)

        self.iconbitmap("mic2.ico")

        self.config(background="#FFFFFF")
        self.ROOT = self

        self.main_app()

    def main_app(self):
        for widget in self.winfo_children():
            widget.destroy()
        Header(self)

        my_font = font.Font(name="Arial Rounded MT")
        customtkinter.CTkLabel(
            self, text="text to speech".upper(), text_font=("Arial Rounded MT Bold", 32), text_color="black"
        ).place(relx=0.5, y=100, anchor=CENTER)

        frame_center = customtkinter.CTkFrame(self)
        self.image_1 = tkinter.PhotoImage(file="pdf.png")
        self.image_2 = tkinter.PhotoImage(file="txt.png")
        self.image_3 = tkinter.PhotoImage(file="contract.png")
        self.image_4 = tkinter.PhotoImage(file="logout.png")
        button_1 = customtkinter.CTkButton(
            frame_center,
            width=100, height=100,
            text=None, corner_radius=100, fg_color="#73FBD3", image=self.image_1,
            command=lambda : self.open_file_and_run(file_type="PDF")
        )
        button_1.grid(row=0, column=0, padx=10, pady=10)
        button_2 = customtkinter.CTkButton(
            frame_center, width=100, height=100, text=None, corner_radius=35, fg_color="#59D2FE", image=self.image_2,
            command=lambda: self.open_file_and_run(file_type="TXT")
        )
        button_2.grid(row=0, column=1, padx=10, pady=10)
        button_3 = customtkinter.CTkButton(
            frame_center, width=100, height=100, text=None, corner_radius=10, fg_color="#5C7AFF", image=self.image_3,
            command=lambda: self.open_file_and_run()
        )
        button_3.grid(row=1, column=0, padx=10, pady=10)
        button_4 = customtkinter.CTkButton(
            frame_center, width=100, height=100, text=None, corner_radius=20, fg_color="#44E5E7", image=self.image_4,
            command=self.on_closing
        )
        button_4.grid(row=1, column=1, padx=10, pady=10)

        frame_center.place(relx=0.5, rely=0.5, anchor=CENTER)

        Footer(self)

    def on_closing(self, event=0):
        if tkinter.messagebox.askquestion(title="Quit?", message="Do you want to quit?"):
            self.destroy()

    def open_file_and_run(self, file_type=None):
        if file_type == "PDF":
            file_to_read = tkinter.filedialog.askopenfilename(
                title="PDF file",
                filetypes=(
                    ('PDF files', '*.pdf'),
                    ('All files', '*.*')
                            )
            )
            pdf_file = open(file_to_read, 'rb')
            pdf_reader = PyPDF2.PdfFileReader(pdf_file)
            print(pdf_reader.numPages)
            text = ""
            for page in pdf_reader.pages:
                text = text + page.extractText()
                # page_obj = pdf_reader.getPage()
            # text = page_obj.extractText()
            pdf_file.close()

            self.second_window(text)
        elif file_type == "TXT":
            file_to_read = tkinter.filedialog.askopenfilename(
                title="TXT file",
                filetypes=(
                    ('TXT files', '*.txt'),
                    ('All files', '*.*')
                )
            )
            file_txt = open(file_to_read, "r")
            text = file_txt.readlines()
            self.second_window(" ".join(text))
        else:
            self.second_window(my_text="")

    def second_window(self, my_text):
        for widget in self.ROOT.winfo_children():
            widget.destroy()

        parent = self.ROOT
        Header(parent)

        self.pause = "Stop"

        self.image_1 = tkinter.PhotoImage(file="mp3-audio-file.png")

        frame_a = customtkinter.CTkFrame(parent, fg_color="#F4F4F4")
        button = customtkinter.CTkButton(
            parent,
            fg_color="#44E5E7",
            image=self.image_1, text=None, command=lambda: self.generate_thread(self.convert_audio).start()
        )
        button.place(x=570, y=380, width=80, height=80)

        self.text = tkinter.Text(frame_a, bg="#F4F4F4")
        self.text.config(highlightthickness=0, borderwidth=0)
        self.text.pack(fill=BOTH, expand=True, padx=10, pady=10)

        self.text.insert(INSERT, my_text)

        frame_b = customtkinter.CTkFrame(
            parent, fg_color="#4A8FE7"
        )

        self.word_count = customtkinter.CTkLabel(frame_b, text="0 words")
        self.word_count.place(anchor=CENTER, rely=.2, x=550)

        self.play_btn = customtkinter.CTkButton(
            frame_b, image=self.play_icon.subsample(2, 2), text=None, bg_color="#4A8FE7", fg_color="#4A8FE7",
            command=self.play_sound
        )
        self.play_btn.place(anchor=CENTER, y=59, x=15, height=24, width=24)

        self.audio_time_txt = customtkinter.CTkLabel(frame_b, text=str(self.audio_time))
        self.audio_time_txt.place(anchor=CENTER, y=59, x=577, )

        self.title = customtkinter.CTkLabel(frame_b, text=self.audio_title)
        self.title.place(anchor=CENTER, rely=.5, relx=.5)

        self.variable = IntVar(frame_b, 100)
        self.progress = customtkinter.CTkSlider(
            frame_b, fg_color="white", progress_color="#00FF0A", height=20, button_color="#73fbd3",
            button_hover_color="#59d2fe", from_=0, to=100, command=self.slider
        )
        self.progress.set(0)
        self.progress.pack(fill=X, padx=(30, 80), side=BOTTOM, pady=(0, 10))

        frame_b.place(relx=0.5, anchor=CENTER, y=520, width=620, height=80)

        frame_a.place(relx=0.5, anchor=CENTER, y=270, width=620, height=400)

        Footer(parent)

        self.updating_window()

    def play_time(self):
        current_time = pygame.mixer.music.get_pos() / 1000

        converted_current_time = time.strftime('%M:%S', time.gmtime(current_time))

        self.audio_time_txt["text"] = f"{converted_current_time} / {self.audio_time}"
        self.progress.set(int(current_time))

        self.audio_time_txt.after(1000, self.play_time)

    def play_sound(self):
        print("In esecuzione", self.audio_title)
        self.pause = "Pause"
        pygame.mixer.music.load(self.audio_title)

        pygame.mixer.music.play()

        self.play_time()

    def slider(self, x):
        pass

    def pause_sound(self):
        pass

    def stop_sound(self):
        pass

    def generate_thread(self, function):
        x = threading.Thread(target=function, args=(1,))
        return x

    def updating_window(self):
        # string = strftime('%H:%M:%S %p')
        text = self.text.get("1.0", END)
        # print(text.split(" "), str(len(text.split(" "))))
        self.word_count.config(text=str(len(text.split(" "))) + " words")
        self.word_count.after(1000, self.updating_window)

    def convert_audio(self, *args):
        self.title["text"] = "Working..."
        engine = pyttsx3.init()
        voice = engine.getProperty('voices')
        print(voice)
        engine.setProperty('voice', voice[0].id)
        # engine.say(self.text.get("1.0", END))
        file_path = tkinter.filedialog.askdirectory(
            title="Choose directory",
        )
        file_name = str(datetime.datetime.now()).replace(".", '').replace(" ", "").replace(":", "") + ".wav"

        print(file_path, file_name)
        engine.save_to_file(self.text.get("1.0", END), file_path+"/"+file_name)
        engine.runAndWait()
        if file_name and file_path:
            self.title["text"] = file_path+"/"+file_name
            self.audio_title = file_path+"/"+file_name
            audio = sf.SoundFile(self.audio_title)
            duration = audio.frames / audio.samplerate
            converted_current_time = time.strftime('%M:%S', time.gmtime(duration))
            self.audio_time_txt["text"] = f"00:00 / {converted_current_time}"

            self.audio_time = converted_current_time

            self.progress.config(to=int(duration))

        else:
            self.title["text"] = "No file selected"



if __name__ == "__main__":
    app = FirstWindow()
    app.mainloop()
