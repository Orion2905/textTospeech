import datetime
import tkinter as tk
from tkinter import *
import tkcalendar
from tkinter import ttk
import ttkbootstrap as ttk

from ttkbootstrap.constants import *
from dateutil import parser
from layout_parts import topbar
import layout_parts
import layout_parts.footer
from database import database
from functions import convert_time, variables
import random
from tkinter import filedialog
from tkinter import simpledialog, messagebox


class SetTime:
    def __init__(self, parent, mode_chooser_a=False):
        self.FONT_1 = ("Arial", 9, "bold")
        print(str(datetime.datetime.now().strftime('%p')))

        self.info_image = tk.PhotoImage(file="images/info.png")

        self.time_box_frame = parent

        self.select_time_box = ttk.Frame(self.time_box_frame)
        self.select_title = ttk.Frame(self.select_time_box)
        self.select_time = ttk.Frame(self.select_time_box)

        ttk.Label(
            self.select_title, text="Delay between each post", justify=LEFT
        ).grid(row=0, column=0, sticky=W, padx=0)
        ttk.Label(
            self.select_title, text="           N posts"
        ).grid(row=0, column=1)
        ttk.Label(
            self.select_title, text="          N groups", justify=RIGHT
        ).grid(row=0, column=2, sticky=W)

        self.hour_entry = ttk.Entry(self.select_time, width=6, justify=CENTER, font=self.FONT_1)
        self.minute_entry = ttk.Entry(self.select_time, width=6, justify=CENTER, font=self.FONT_1)
        self.seconds_entry = ttk.Entry(self.select_time, width=6, justify=CENTER, font=self.FONT_1)

        self.hour_entry.grid(row=1, column=0)
        self.minute_entry.grid(row=1, column=1, padx=2)
        self.seconds_entry.grid(row=1, column=2)

        ttk.Label(self.select_time, text="Hours").grid(row=2, column=0)
        ttk.Label(self.select_time, text="Minute").grid(row=2, column=1)
        ttk.Label(self.select_time, text="Seconds").grid(row=2, column=2)

        self.number_of_post = ttk.Spinbox(
            self.select_time, width=5, from_=0, to=30, justify=CENTER, font=self.FONT_1
        )
        self.number_of_post.grid(row=1, column=3, padx=8)

        ttk.Label(self.select_time, text="Repeat").grid(row=2, column=3)

        self.selected_groups = ttk.Entry(
            self.select_time,
            background="#3742FA", justify=CENTER, width=5, text="0", font=self.FONT_1, state=DISABLED
        )
        self.selected_groups.grid(row=1, column=4, padx=4)

        mode_list = ["Loop Mode", "Schedule Mode"]

        if not mode_chooser_a:
            self.mode_chooser = ttk.Combobox(
                self.select_time_box, values=mode_list, font=self.FONT_1, state="readonly"
            )
            self.mode_chooser.set("Choose mode")

            # self.mode_chooser.place(y=85, width=265)
        else:
            mode_list = ["All", "Male", "Female"]
            age_range = [x for x in range(15, 81)]
            age_range.insert(0, "All")
            mode_list_birthday = ["All", "Next Week", "Next Month", "Define date birthday"]

            ttk.Label(self.select_time, text="Choose sex").place(y=50)
            self.mode_chooser = ttk.Combobox(
                self.select_time_box, values=mode_list, font=self.FONT_1, state="readonly"
            )
            self.mode_chooser.set("Male/Female")

            self.mode_chooser.place(y=90, width=105)

            ttk.Label(self.select_time, text="Age range").place(y=50, x=108)
            self.mode_chooser_2 = ttk.Combobox(
                self.select_time_box, values=age_range, font=self.FONT_1, state="readonly"
            )
            self.mode_chooser_2.set("From")

            self.mode_chooser_2.place(y=90, x=108, width=45)

            self.mode_chooser_2_1 = ttk.Combobox(
                self.select_time_box, values=age_range, font=self.FONT_1, state="readonly"
            )
            self.mode_chooser_2_1.set("To")

            self.mode_chooser_2_1.place(y=90, x=157, width=45)

            # ttk.Label(self.select_time, text="Birthday soon").place(y=50, x=205)
            self.mode_chooser_3 = ttk.Combobox(
                self.select_time_box, values=mode_list_birthday, font=self.FONT_1, state="readonly"
            )
            self.mode_chooser_3.set("Birthday soon")

            # self.mode_chooser_3.place(y=90, x=205, width=110)

        self.info = ttk.Button(
            self.select_time_box,
            image=self.info_image,
            bootstyle="info-outline",
            command=lambda : tk.messagebox.showinfo(
                title="Info box", message="All bots have a default delay ranging from 35 to 50 seconds"
            )
        ).place(y=80, x=265)

        self.select_title.pack(fill=X)
        self.select_time.pack(fill=BOTH, expand=True)
        self.select_time_box.place(x=250, y=1, height=120)

        self.mode_chooser.bind('<<ComboboxSelected>>', self.check_for_scheduled_posts)



    def get_user_data(self):
        f = open("user/user_data.txt", "r")
        a = f.readlines()[2].replace("\n", "")
        print(a)
        name = database.Database().select_where(
            "subscribed_clientinfo", f"subscriptionID = '{a}'"
        )
        return name[0]

    def check_for_scheduled_posts(self, event):
        mode = self.mode_chooser.get()

        print(mode, "SELECT")

        self.user_data = self.get_user_data()
        scheduled_post_data = database.Database().select_where(
            table="scheduled_post", clausole=f"id_user = {self.user_data[0]} ORDER BY start_time DESC"
        )
        datetime_obj = parser.parse(str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        for i in scheduled_post_data:
            # print(i[3], datetime_obj, (i[3] == datetime_obj))
            if i[3] <= datetime_obj and i[4] == "ACTIVE":
                # print("SIII")
                pass
        self.ROOT.after(100, self.check_for_scheduled_posts)
        self.ROOT.update()


class SetSchedule:
    def __init__(self, parent, icons, parent_2, parent_3, mode=""):
        self.PARENT = parent
        self.PARENT_2 = parent_2
        self.PARENT_3 = parent_3

        self.MODE = mode
        self.info_image = tk.PhotoImage(file="images/info.png")
        self.FONT_1 = ("Arial", 10, "bold")
        self.FONT_5 = ("Arial", 12)
        self.FONT_2 = ("Arial", 24, "bold")
        self.FONT_3 = ("Arial", 18)
        self.FONT_4 = ("Impact", 30)
        self.FONT_6 = ("Impact", 18)
        self.FONT_7 = ("Arial", 12, "bold")

        self.ICONS = {
            "home": PhotoImage(file=r"images/topbar/home (2).png").subsample(1, 1),
            "rounded_x": PhotoImage(file=r"images/topbar/cross-circle (1).png").subsample(1, 1),
            "user": PhotoImage(file=r"images/topbar/user.png").subsample(1, 1),
            "sign-out": PhotoImage(file=r"images/topbar/sign-out (1).png").subsample(1, 1),
            "next": PhotoImage(file=r"images/angle-circle-left.png").subsample(1, 1),
            "back": PhotoImage(file=r"images/angle-circle-right.png").subsample(1, 1),
            "instagram": PhotoImage(file=r"images/Instagram_icon-icons.com_66804.png").subsample(2, 2),
            "facebook": PhotoImage(file=r"images/facebook_icon-icons.com_53612.png").subsample(2, 2),
            "whatsapp": PhotoImage(file=r"images/whatsapp_icon-icons.com_53606.png").subsample(2, 2),
            "fb_bot_1": PhotoImage(file=r"images/fb_bot_1.png").subsample(9, 9),
            "chrome": PhotoImage(file=r"images/chrome.png").subsample(1, 1),
            "firefox": PhotoImage(file=r"images/topbar/firefox2.png").subsample(1, 1),
            "settings": PhotoImage(file=r"images/topbar/settings.png").subsample(1, 1),
            "image": PhotoImage(file=r"images/upload.png").subsample(13, 13),
            "logo": PhotoImage(file=r"images/topbar/logo.png"),
            "save": PhotoImage(file=r"images/disk.png")

        }

        self.WINDOW_COLOR = "#dfe4ea"

        self.schedule_mode_frame = ttk.LabelFrame(
            self.PARENT, bootstyle='dark', text="Campaign planning"
        )

        self.set_date_frame = ttk.Frame(self.schedule_mode_frame) #borderwidth=2, relief=SOLID, cursor="hand2"

        self.pick_date = ttk.DateEntry(self.set_date_frame, dateformat="%Y-%m-%d")

        # self.pick_date.configure(state="readonly")
        self.pick_date.pack()

        self.clock_image = tk.PhotoImage(file=r"images/clock.png")

        self.time_pick_frame = ttk.Frame(self.set_date_frame)
        self.pick_time = ttk.Entry(self.time_pick_frame)
        self.pick_time_image = ttk.Button(
            self.time_pick_frame, image=self.clock_image, bootstyle="default-date",
            command=lambda: layout_parts.time_entry.run(self)
        )
        self.pick_time.pack(side=tk.LEFT, fill=tk.X, expand=tk.YES)
        self.pick_time_image.pack(side=tk.LEFT)
        self.time_pick_frame.pack(pady=2)
        self.pick_time.insert(
            END,
            f""
            f"{datetime.datetime.now().strftime('%I')}:"
            f"{datetime.datetime.now().strftime('%M')}:{datetime.datetime.now().strftime('%S')}"
            f" {str(datetime.datetime.now().strftime('%p'))}"
        )
        self.pick_time.configure(state="readonly")

        # print(self.pick_time.get(), self.pick_date.entry.get())

        # self.set_date = ttk.Label(self.set_date_frame, text="year-month-day", font=self.FONT_7)
        # self.set_date.pack()

        # self.set_time = ttk.Label(self.set_date_frame, text="hh:mm:ss", font=self.FONT_6)
        # self.set_time.pack()
        self.info = ttk.Button(
            self.schedule_mode_frame,
            image=self.info_image,
            bootstyle="light-date",
            command=lambda: tk.messagebox.showinfo(title="Info box",
                                                   message="After saving the post, leave the SERVICE CHOOSER"
                                                           " window open and the"
                                                           " scheduled campaigns will be activated automatically")
        ).place(y=-7, x=254)

        self.set_date_frame.place(relx=.35, rely=.5, relwidth=.63, anchor=CENTER)

        self.save_scheduled_frame = ttk.Frame(
            self.schedule_mode_frame
        )

        # self.set_date_frame.bind("<Button-1>", lambda e, a="si": self.save_date())
        # self.set_date.bind("<Button-1>", lambda e, a="si": self.save_date())
        # self.set_time.bind("<Button-1>", lambda e, a="si": self.save_date())

        self.save_image_btn = ttk.Button(
            self.save_scheduled_frame, image=icons["save"], text="Save post", compound=TOP, bootstyle="primary",
            command=self.save_scheduled_post
        )
        self.save_image_btn.place(relx=.5, rely=.5, anchor=CENTER)

        self.save_scheduled_frame.place(relx=.61, rely=.5, relwidth=.23, relheight=.9, anchor=CENTER)

        self.schedule_mode_frame.place(anchor=W, x=290, y=50, height=110, width=103)

    def save_scheduled_post(self):
        f = open("user/user_data.txt", "r")
        a = f.readlines()[0].replace("\n", "")
        # print(a)

        db = database.Database()
        date_string = f"{self.pick_date.entry.get().replace('/', '-').replace(' ',  '')} {str(self.pick_time.get())}"

        # print(date_string)

        datetime_obj = parser.parse(date_string)
        try:
            all_filters = [
                self.PARENT_3.set_time.mode_chooser.get(),
                [self.PARENT_3.set_time.mode_chooser_2.get(), self.PARENT_3.set_time.mode_chooser_2_1.get()],
                self.PARENT_3.set_time.mode_chooser_3.get()
            ]
        except:
            try:
                all_filters = [self.PARENT_3.keywords_entry.get(), self.PARENT_3.date_filter_entry.get()]
            except:
                all_filters = ""

        # print("QUI", datetime_obj)
        hours_to_seconds = int(self.PARENT_3.get_all_values()[0]) * 3600
        minute_to_seconds = int(self.PARENT_3.get_all_values()[1]) * 60
        seconds_sum = hours_to_seconds + minute_to_seconds + int(self.PARENT_3.get_all_values()[2])
        base_time = 1

        repeats = self.PARENT_3.set_time.number_of_post.get()
        caption = self.PARENT_3.post_caption.get("1.0", END)
        delay = base_time + seconds_sum + random.randint(5, 70)

        try:
            image = self.PARENT_3.get_all_values()[5]
        except:
            image = ""

        if self.MODE == "HOTLEAD":
            file_name = ""
        else:
            filetypes = (
                ('CSV', '*.csv'),
                ('TXT', '*.txt'),
            )
            file_name = filedialog.askopenfilename(
                filetypes=filetypes,
                title='Choose CSV FILE',
                initialdir='/',
            )

        db.insert_into(
            "scheduled_post",
            (
                "id_schedule", "id_user", "post_type", "start_time",
                "status", "delay", "repeats", "caption", "image_path", "csv_path", "other_filters", "browser"
            ),
            (
                0, a, self.MODE, datetime_obj, "ACTIVE",
                delay, repeats, caption, image, file_name, str(all_filters),
                self.PARENT_3.top_bar.mode_browser
            )
        )

    def save_date(self):
        # Create Object
        root = ttk.Toplevel()

        # Set geometry
        root.geometry("400x400")
        root.resizable(False, False)

        tk.Label(root, text="Choose date", font=self.FONT_1).pack()

        # Add Calendar
        cal = tkcalendar.Calendar(
            root, selectmode='day',
            year=datetime.datetime.now().year, month=datetime.datetime.now().month,
            day=datetime.datetime.now().day
        )
        cal.pack(pady=20)

        def grad_date():
            date = cal.selection_get()
            self.set_date.configure(text=date)
            self.set_time.configure(
                text=f"{hour_entry.get()}:{minute_entry.get()}:{seconds_entry.get()} {date_filter_entry.get()}"
            )

        self.time_box_frame = ttk.Frame(root)

        ttk.Label(self.time_box_frame, text="Choose time", font=self.FONT_1).pack()

        self.select_time_box = tk.Frame(self.time_box_frame)
        self.select_title = tk.Frame(self.select_time_box)
        self.select_time = tk.Frame(self.select_time_box)

        # ttk.Label(self.select_title, text="    N groups", justify=RIGHT).grid(row=0, column=2, sticky=W)
        hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        minutes = [i for i in range(60)]

        hour_entry = ttk.Combobox(
            self.select_time, width=3, justify=CENTER, font=self.FONT_1, state="readonly", values=hours
        )
        hour_entry.set("Hours")

        minute_entry = ttk.Combobox(
            self.select_time, width=3, justify=CENTER, font=self.FONT_1, state="readonly", values=minutes
        )
        minute_entry.set("Minutes")

        seconds_entry = ttk.Combobox(
            self.select_time, width=3, justify=CENTER, font=self.FONT_1, state="readonly", values=minutes
        )
        seconds_entry.set("Seconds")

        hour_entry.grid(row=1, column=0)
        minute_entry.grid(row=1, column=1, padx=2)
        seconds_entry.grid(row=1, column=2)

        tk.Label(self.select_time, text="Hours").grid(row=2, column=0)
        tk.Label(self.select_time, text="Minute").grid(row=2, column=1)
        tk.Label(self.select_time, text="Seconds").grid(row=2, column=2)

        time_mode = ["AM", "PM"]

        date_filter_entry = ttk.Combobox(
            self.select_time, width=5, font=self.FONT_1, state="readonly", values=time_mode
        )
        date_filter_entry.grid(row=1, column=4)
        date_filter_entry.set("Choose mode")

        self.select_time.pack(fill=X)
        self.select_time_box.pack()

        self.time_box_frame.pack()

        # Add Button and Label
        ttk.Button(
            root, text="Set Date",
            command=grad_date,
            width=20, height=2, bd=1
        ).pack(pady=5)

        footer = layout_parts.footer.Footer(icons=[], parent=root)

        # Execute Tkinter
        root.mainloop()


class SetImage:
    def __init__(self, parent_root, icons, parent):
        self.PARENT = parent
        self.PARENT_ROOT = parent_root

        self.FONT_1 = ("Arial", 10, "bold")
        self.FONT_5 = ("Arial", 12)
        self.FONT_2 = ("Arial", 24, "bold")
        self.FONT_3 = ("Arial", 18)
        self.FONT_4 = ("Impact", 30)
        self.FONT_6 = ("Impact", 18)
        self.FONT_7 = ("Arial", 12, "bold")

        self.WINDOW_SIZE = "655x500"
        self.WINDOW_COLOR = "#dfe4ea"
        self.BACKGROUND_2 = "#aaa69d"

        self.upload_image_frame = ttk.LabelFrame(self.PARENT_ROOT, text="Set Image/video", bootstyle='dark')

        self.set_image_frame = ttk.Frame(self.upload_image_frame)
        self.save_image_btn = ttk.Button(
            self.set_image_frame, image=icons["image"], text="image/video", compound=TOP,
            command=self.PARENT.upload_image
        )
        self.save_image_btn.place(relx=.5, rely=.5, anchor=CENTER)
        self.set_image_frame.place(x=5, rely=.05, relwidth=.34, relheight=.91)

        self.label_image = ttk.Label(
            self.upload_image_frame, text="image/video",
            justify=CENTER
        )
        self.label_image.place(anchor=W, relx=.5, rely=.5)

        # tk.Label(self.upload_image_frame, text="Upload image", bg="#1E90FF").place(anchor=W, relx=.35, rely=.5)

        self.image_name = ttk.Label(self.upload_image_frame, font=self.FONT_1)

        self.upload_image_frame.place(anchor=W, x=290, y=160, height=110, width=289)
