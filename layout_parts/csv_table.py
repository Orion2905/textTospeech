# ================ MODULES ================ #

# ================ tkinter ================ #
import tkinter as tk
from tkinter import *
from tkinter import ttk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import filedialog, simpledialog, messagebox
# from ttkwidgets import CheckboxTreeview
# ================ tkinter ================ #

# ================ program functions ================ #
from functions import read_presets, variables, errors
from services.facebook.facebook_login import FacebookBot
from layout_parts import topbar, clock, set_schedule, footer
from services.facebook.facebook_groups_name import FacebookBotGroupsInfo
# ================ program functions ================ #

# ================ others ================ #
import datetime
import time
import random
import threading
# ================ others ================ #

# ================ MODULES ================ #


class CsvTable:
    def __init__(self, frame, parent_2, icon, *args, **kwargs):

        self.groups_list_frame = frame
        self.PARENT = parent_2
        self.ICONS = icon
        # scroll_bar = tk.Scrollbar(self.groups_list_frame)
        self.delete = tk.PhotoImage(file="images/tresh.png")

        columns = ('Name', 'ID')
        self.groups_list = ttk.Treeview(
            self.groups_list_frame, column=columns, selectmode="extended", height=7
        )
        # define headings
        # self.groups_list.heading('Select', text='Select')
        self.groups_list.heading('#0', text='')
        self.groups_list.heading('#1', text='Name')
        self.groups_list.heading('#2', text='ID')
        # self.groups_list.insert(0, "GROUP NAME; GROUP ID")

        self.groups_list.column('#0', anchor='center', width=5)
        self.groups_list.column("Name", width=20)
        self.groups_list.column("ID", width=20)

        # add a scrollbar
        scrollbar = ttk.Scrollbar(self.groups_list, orient=tk.VERTICAL, command=self.groups_list.yview,
                                  bootstyle="dark-round")
        self.groups_list.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=RIGHT, fill=Y)

        self.groups_list.pack(fill=BOTH, expand=True)

        # Insert image to #0
        # for i in range(10):
        #     self.groups_list.insert(
        #         '', "end",
        #         text="☐",
        #         value=("A's value", "B's value")
        #     )
        # scroll_bar.pack(side=RIGHT, fill=BOTH)

        self.manual_upload_button = ttk.Button(
            self.groups_list_frame, text="MANUAL UPLOAD/DELETE", command=self.manual_upload
        )
        self.upload_button = ttk.Button(
            self.groups_list_frame, text="upload/delete from csv/txt".upper(),
            command=self.upload_csv
        )
        self.upload_button.pack(side=BOTTOM, fill=X)
        self.manual_upload_button.pack(side=BOTTOM, fill=X)

        self.select_all_checkbox = ttk.Checkbutton(self.groups_list_frame, text="Select All", command=self.select_all)
        self.select_all_checkbox.place(y=9, x=15)

        self.trash_button = ttk.Button(
            self.groups_list_frame, image=self.delete, bootstyle="outline-danger", command=self.delete_items
        )
        self.trash_button.place(rely=.83, relx=.77)

        self.groups_list.bind('<<TreeviewSelect>>', self.on_tree_click)
        self.groups_list.bind('<Button-2>', self.on_tree_right_click)
        self.groups_list.bind('<Button-3>', self.on_tree_right_click)

    def on_right_click(self, e):
        ''' right click context menu for all Tk Entry and Text widgets
        '''

        try:
            def rClick_Copy(e, apnd=0):
                e.widget.event_generate('<<Cut>>')

            def rClick_Cut(e):
                e.widget.event_generate('<<Copy>>')

            def rClick_Paste(e):
                e.widget.event_generate('<<Paste>>')

            e.widget.focus()

            nclst = [
                (' Cut', lambda e=e: rClick_Cut(e)),
                (' Copy', lambda e=e: rClick_Copy(e)),
                (' Paste', lambda e=e: rClick_Paste(e)),
            ]

            rmenu = tk.Menu(None, tearoff=0, takefocus=0)

            for (txt, cmd) in nclst:
                rmenu.add_command(label=txt, command=cmd)

            rmenu.tk_popup(e.x_root + 40, e.y_root + 10, entry="0")

        except tk.TclError:
            print(' - rClick menu, something wrong')
            pass

        return "break"

    def on_tree_right_click(self, event):
        question = messagebox.askyesno("Delete", message="Are you sure?")
        if question:
            row = self.groups_list.selection()
            # print('item:', row)
            # print('event:', event)
            row = self.groups_list.selection()[0]
            self.groups_list.delete(row)
            print(row)

            # print("you clicked on", self.groups_list.item(row).values())
        else:
            pass

    def on_tree_click(self, event):
        row = self.groups_list.selection()
        # print(row)
        if self.groups_list.item(row[0])["text"] != "☑":
            self.groups_list.item(row[0], text="☑")
        else:
            self.groups_list.item(row[0], text="☐")
        # self.tree.

    def delete_items(self):
        for row in self.groups_list.get_children():
            # print(row)
            if self.groups_list.item(row)["text"] == "☑":
                self.groups_list.delete(row)

    def select_all(self):
        for row in self.groups_list.get_children():
            # print(row)
            if self.groups_list.item(row)["text"] != "☑":
                self.groups_list.item(row, text="☑")
            else:
                self.groups_list.item(row, text="☐")

    # ============ UPLOAD IMAGE FUNCTION ============= #
    def upload_image(self):
        global image
        filetypes = (
            ('PNG', '*.png'),
            ('JPG', '*.jpg'),
            ('MP4', '*.mp4'),
            ("All file types", '*.*')
        )
        image = filedialog.askopenfilename(
            filetypes=filetypes,
            title='Open a file',
            initialdir='/',
        )
        self.set_image.label_image['text'] = str(image).split("/")[-1]
        print(image)
        self.ROOT.update()
        self.set_image.upload_image_frame.update()
        return image

    # ============ GET VALUES FUNCTION ============= #

    def upload_csv(self):

        def upload():
            global file_name

            filetypes = (
                ('CSV', '*.csv'),
                ('TXT', '*.txt'),
            )
            file_name = filedialog.askopenfilename(
                filetypes=filetypes,
                title='Open a file',
                initialdir='/',
            )
            file_path_label['text'] = file_name.split("/")[-1]
            file_path_label.pack(pady=5)

        def add_csv():
            with open(file_name, "r+", encoding="UTF-8") as f:
                for line in f:
                    self.groups_list.insert('', tk.END, text="☐", values=line.split(";"))

            groups_count = len(self.groups_list.get_children())
            self.PARENT.set_time.selected_groups["state"] = ACTIVE
            self.PARENT.set_time.selected_groups.delete(0, END)
            self.PARENT.set_time.selected_groups.insert(END, groups_count)
            self.PARENT.set_time.selected_groups["state"] = DISABLED

            print(groups_count, self.groups_list.get_children())

        def remove_csv():
            presets_list = read_presets.ReadPreference().read()
            file = ""
            for i in presets_list:
                if "groups_file=" in i:
                    file = i.replace("\n", "").split("=")[1]
                    break
                else:
                    file = ""
                    print("No file found")

            # add data to the treeview
            with open(file_name, "r+", encoding="UTF-8") as f:
                file_lines_count = f.readlines()
                for i in file_lines_count:
                    a = i.replace("\n", "").split(";")[1]
                    for row in self.groups_list.get_children():
                        b = str(list(self.groups_list.item(row).values())[2][1])
                        print(a, b)
                        if a == b or a in b:
                            print("SIII")
                            self.groups_list.delete(row)

        root_2 = ttk.Toplevel()

        root_2.geometry("350x200")
        root_2.configure()
        root_2.resizable(False, False)

        ttk.Label(root_2, text="Upload csv or txt file").pack(pady=3)
        button = tk.Button(root_2, image=self.ICONS['image'], command=upload).pack(pady=2)
        file_path_label = ttk.Label(root_2, text="")

        add = ttk.Button(root_2, text="add".upper(), command=add_csv).pack(fill=X, padx=10, pady=2)
        remove = ttk.Button(root_2, text="delete".upper(), command=remove_csv).pack(fill=X, padx=10)

        footer.Footer(root_2, self.ICONS)

        root_2.mainloop()

    # method to upload manually groups on the treeview
    def manual_upload(self):
        def add_csv():
            self.groups_list.insert('', tk.END, text="☐", values=[name_entry.get(), id_entry.get()])

        def remove_csv():
            for row in self.groups_list.get_children():
                if str(list(self.groups_list.item(row).values())[2][1]) == str(id_entry.get()):
                    print("SI")
                    self.groups_list.delete(row)

        root_2 = ttk.Toplevel()

        root_2.geometry("350x230")
        root_2.configure()
        root_2.resizable(False, False)

        ttk.Label(root_2, text="Add or delete new groups").pack(pady=3)

        frame = ttk.Frame(root_2)

        ttk.Label(frame, text="Name").grid(row=0, column=0, pady=5)
        name_entry = ttk.Entry(frame, )
        name_entry.grid(row=0, column=1)

        ttk.Label(frame, text="Id").grid(row=1, column=0)
        id_entry = ttk.Entry(frame)
        id_entry.grid(row=1, column=1)

        frame.pack()

        add = ttk.Button(root_2, text="add".upper(), command=add_csv).pack(fill=X, padx=10, pady=5)
        remove = ttk.Button(root_2, text="delete".upper(), command=remove_csv).pack(fill=X, padx=10)

        footer.Footer(root_2, self.ICONS)

        name_entry.bind('<Button-3>', self.on_right_click, add='')
        id_entry.bind('<Button-3>', self.on_right_click, add='')

        root_2.mainloop()
