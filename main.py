import tkinter
import tkinter.messagebox
import customtkinter
from layout_parts import scrollable_frame
from tkinter import PhotoImage



customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):

    WIDTH = 780
    HEIGHT = 520

    def __init__(self):
        super().__init__()

        self.title("Talent Show - Scheda voto")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        # self.minsize(App.WIDTH, App.HEIGHT)
        self.resizable(False, False)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(
            master=self,
            width=180,
            corner_radius=30, background="#1B1B1B"
        )
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(
            master=self,
            width=580,
            height=480
        )
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============

        # configure grid layout (1x11)
        # self.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
        # self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Pertecipanti".upper(),
                                              text_font=("Inter", -20, "bold"))  # font name and size in px
        self.label_1.grid(row=1, column=0, pady=30, padx=10)

        scrollable_frame_1 = scrollable_frame.ScrollableFrame(self.frame_left)

        for i in range(20):
            self.button_1 = customtkinter.CTkButton(master=scrollable_frame_1.scrollable_frame,
                                                    text="Mario Rossi",
                                                    fg_color="#632E2E",
                                                    width=150,
                                                    height=45,
                                                    text_font=("Inter", 12, "bold"),
                                                    # fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                    command=self.button_event,
                                                    corner_radius=11
                                                    )
            self.button_1.pack(pady=5, padx=5)

        scrollable_frame_1.grid()

        self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Aggiungi Partecipante",
                                                fg_color="#676767",
                                                width=180,
                                                height=45,
                                                text_font=("Inter", -14),
                                                # fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                command=self.button_event,
                                                corner_radius=0
                                                )
        self.button_1.place(y=475)

        # self.switch_1 = customtkinter.CTkSwitch(master=self.frame_left)
        # self.switch_1.grid(column=0, pady=10, padx=20, sticky="w")
        #
        # self.switch_2 = customtkinter.CTkSwitch(master=self.frame_left,
        #                                         text="Dark Mode",
        #                                         command=self.change_mode)
        # self.switch_2.grid(column=0, pady=10, padx=20, sticky="w")

        # ============ frame_right ============

        # configure grid layout (3x7)
        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)

        self.frame_info = customtkinter.CTkFrame(
            master=self.frame_right,
            width=540,
            height=230,
            corner_radius=30,
            fg_color="#7A7A7A"
        )
        self.frame_info.grid(row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew")

        # ============ frame_info ============

        # configure grid layout (1x1)
        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)

        self.label_info_1 = customtkinter.CTkFrame(
            master=self.frame_info,
            height=200,
            width=240,
            fg_color="#D9D9D9",  # <- custom tuple-color
            corner_radius=30

        )
        self.label_info_1.grid(column=0, row=0, sticky="w", padx=15)

        self.name = customtkinter.CTkLabel(
            master=self.label_info_1,
            text="Nome:",
            text_color="black",
            width=30,
            justify="left",
            text_font=("Inter", -14, "bold")
        )
        self.name.place(x=12, y=20)

        self.surname = customtkinter.CTkLabel(
            master=self.label_info_1,
            text="Cognome:",
            text_color="black",
            justify="left",
            text_font=("Inter", -14, "bold")
        )
        self.surname.place(x=12, y=50, width=10,)

        self.nickname = customtkinter.CTkLabel(
            master=self.label_info_1,
            text="Nickname:",
            width=30,
            text_color="black",
            text_font=("Inter", -14, "bold")
        )
        self.nickname.place(x=12, y=80)

        self.description = customtkinter.CTkLabel(
            master=self.label_info_1,
            text="Descrizione:",
            text_color="black",
            width=30,
            text_font=("Inter", -14, "bold")
        )
        self.description.place(x=20, y=110)

        self.surname = customtkinter.CTkLabel(
            master=self.label_info_1,
            text="Cognome:",
            text_color="black",
            justify="left",
            width=30,
            text_font=("Inter", -14, "bold")
        )
        self.surname.place(x=12, y=50)

        self.nickname = customtkinter.CTkLabel(
            master=self.label_info_1,
            text="Nickname:",
            text_color="black",
            width=30,
            text_font=("Inter", -14, "bold")
        )
        self.nickname.place(x=12, y=80)

        self.description = customtkinter.CTkLabel(
            master=self.label_info_1,
            text="Descrizione:",
            text_color="black",
            width=30,
            text_font=("Inter", -14, "bold")
        )
        self.description.place(x=12, y=110)

        #
        self.name_output = customtkinter.CTkLabel(
            master=self.label_info_1,
            text=f"Mario",
            text_color="black",
            justify="left",
            text_font=("Inter", -14)
        )
        self.name_output.place(x=80, y=20)

        self.surname_output = customtkinter.CTkLabel(
            master=self.label_info_1,
            text="Rossi",
            text_color="black",
            justify="left",
            text_font=("Inter", -14)
        )
        self.surname_output.place(x=80, y=50)

        self.nickname_output = customtkinter.CTkLabel(
            master=self.label_info_1,
            text="MarioRossi",
            text_color="black",
            text_font=("Inter", -14)
        )
        self.nickname_output.place(x=98, y=80)

        self.description_output = customtkinter.CTkLabel(
            master=self.label_info_1,
            text="Descrizione del cantante",
            text_color="black",
            text_font=("Inter", -14)
        )
        self.description_output.place(x=10, y=130)

        customtkinter.CTkLabel(
            self.frame_info, text="Voto giuria", text_font=("Inter", -12, "bold"), text_color="black"
        ).place(relx=.5, y=40)
        marks_frame_1 = customtkinter.CTkFrame(
            master=self.frame_info,
            width=160,
            height=60,
            fg_color="#D9D9D9",
            corner_radius=20
        )
        marks_frame_1.place(relx=.51, y=60)

        self.star_image = PhotoImage(file="star.png")
        self.sta_button = customtkinter.CTkButton(
            master=self.frame_info,
            corner_radius=20,
            image=self.star_image,
            text=None,
            width=60,
            height=60,
            fg_color="#2870C5"
        )
        self.sta_button.place(relx=.84, y=60)

        customtkinter.CTkLabel(
            self.frame_info, text="Voto pubblico", text_font=("Inter", -12, "bold"), text_color="black"
        ).place(relx=.5, y=130)
        marks_frame_2 = customtkinter.CTkFrame(
            master=self.frame_info,
            width=160,
            height=60,
            fg_color="#D9D9D9",
            corner_radius=20
        )
        marks_frame_2.place(relx=.51, y=150)

        self.sta_button_2 = customtkinter.CTkButton(
            master=self.frame_info,
            corner_radius=20,
            image=self.star_image,
            text=None,
            width=60,
            height=60,
            fg_color="#22C087"
        )
        self.sta_button_2.place(relx=.84, y=150)

        judge_frame = customtkinter.CTkFrame(
            master=self.frame_right,
            width=540,
            height=84,
            fg_color="#D9D9D9",
            background="#D9D9D9",
            bg_color="#D9D9D9",
            corner_radius=30
        )
        judge_frame.place(x=10, rely=.81)

        scrollable_frame_2 = scrollable_frame.ScrollableFrame_x(judge_frame)

        for i in range(6):
            self.judge = customtkinter.CTkButton(
                master=scrollable_frame_2.scrollable_frame, text="Valerio Bianchi",
                width=165, height=45, fg_color="#703C78", bg="#D9D9D9"
            )
            self.judge.grid(row=0, column=i, padx=5, pady=5)

        scrollable_frame_2.place(y=0, x=40)

        self.add_image = PhotoImage(file="plus.png")
        self.add_button = customtkinter.CTkButton(
            master=judge_frame,
            image=self.add_image,
            text="",
            corner_radius=30,
            width=65,
            height=65,
            fg_color="#6D6D6D"
        )
        self.add_button.place(relx=.85, y=10)
        # ============ frame_right ============

        # self.radio_var = tkinter.IntVar(value=0)
        #
        # self.label_radio_group = customtkinter.CTkLabel(master=self.frame_right,
        #                                                 text="CTkRadioButton Group:")
        # self.label_radio_group.grid(row=0, column=2, columnspan=1, pady=20, padx=10, sticky="")
        #
        # self.radio_button_1 = customtkinter.CTkRadioButton(master=self.frame_right,
        #                                                    variable=self.radio_var,
        #                                                    value=0)
        # self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")
        #
        # self.radio_button_2 = customtkinter.CTkRadioButton(master=self.frame_right,
        #                                                    variable=self.radio_var,
        #                                                    value=1)
        # self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")
        #
        # self.radio_button_3 = customtkinter.CTkRadioButton(master=self.frame_right,
        #                                                    variable=self.radio_var,
        #                                                    value=2)
        # self.radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")
        #
        # self.slider_1 = customtkinter.CTkSlider(master=self.frame_right,
        #                                         from_=0,
        #                                         to=1,
        #                                         number_of_steps=3,
        #                                         command=self.progressbar.set)
        # self.slider_1.grid(row=4, column=0, columnspan=2, pady=10, padx=20, sticky="we")
        #
        # self.slider_2 = customtkinter.CTkSlider(master=self.frame_right,
        #                                         command=self.progressbar.set)
        # self.slider_2.grid(row=5, column=0, columnspan=2, pady=10, padx=20, sticky="we")
        #
        # self.slider_button_1 = customtkinter.CTkButton(master=self.frame_right,
        #                                                height=25,
        #                                                text="CTkButton",
        #                                                command=self.button_event)
        # self.slider_button_1.grid(row=4, column=2, columnspan=1, pady=10, padx=20, sticky="we")
        #
        # self.slider_button_2 = customtkinter.CTkButton(master=self.frame_right,
        #                                                height=25,
        #                                                text="CTkButton",
        #                                                command=self.button_event)
        # self.slider_button_2.grid(row=5, column=2, columnspan=1, pady=10, padx=20, sticky="we")
        #
        # self.checkbox_button_1 = customtkinter.CTkButton(master=self.frame_right,
        #                                                  height=25,
        #                                                  text="CTkButton",
        #                                                  border_width=3,   # <- custom border_width
        #                                                  fg_color=None,   # <- no fg_color
        #                                                  command=self.button_event)
        # self.checkbox_button_1.grid(row=6, column=2, columnspan=1, pady=10, padx=20, sticky="we")
        #
        # self.check_box_1 = customtkinter.CTkCheckBox(master=self.frame_right,
        #                                              text="CTkCheckBox")
        # self.check_box_1.grid(row=6, column=0, pady=10, padx=20, sticky="w")
        #
        # self.check_box_2 = customtkinter.CTkCheckBox(master=self.frame_right,
        #                                              text="CTkCheckBox")
        # self.check_box_2.grid(row=6, column=1, pady=10, padx=20, sticky="w")
        #
        # self.entry = customtkinter.CTkEntry(master=self.frame_right,
        #                                     width=120,
        #                                     placeholder_text="CTkEntry")
        # self.entry.grid(row=8, column=0, columnspan=2, pady=20, padx=20, sticky="we")
        #
        # self.button_5 = customtkinter.CTkButton(master=self.frame_right,
        #                                         text="CTkButton",
        #                                         command=self.button_event)
        # self.button_5.grid(row=8, column=2, columnspan=1, pady=20, padx=20, sticky="we")
        #
        # # set default values
        # self.radio_button_1.select()
        # # self.switch_2.select()
        # self.slider_1.set(0.2)
        # self.slider_2.set(0.7)
        # self.progressbar.set(0.5)
        # self.slider_button_1.configure(state=tkinter.DISABLED, text="Disabled Button")
        # self.radio_button_3.configure(state=tkinter.DISABLED)
        # self.check_box_1.configure(state=tkinter.DISABLED, text="CheckBox disabled")
        # self.check_box_2.select()

    def button_event(self):
        print("Button pressed")

    def change_mode(self):
        if self.switch_2.get() == 1:
            customtkinter.set_appearance_mode("dark")
        else:
            customtkinter.set_appearance_mode("light")

    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()


if __name__ == "__main__":
    app = App()
    app.start()