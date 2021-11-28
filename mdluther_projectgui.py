# Michael Luther CIS345 - Tu/Thurs - 10:30AM - Project GUI

from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from dataclasses import dataclass
import json
from country import Country


# TODO
# Implement Tax class
# Implement Country Classes
# Populate Country Frame
# Add Country flags
# Clean up styling
# Add admin mode for editing tax info
# Improve search feature

widget_background = "#D2D7E0"
window_background = "#5A6881"

with open("country_data.json") as file:
    country_data = json.load(file)

tax_list = [
    Tax(tax_code, *tax)
    for values in country_data.values()
    for tax in values[1:]
    for tax_code, tax in tax.items()
]


class AppWindow(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.geometry("850x480")
        self.title("SpeedTax")

        try:
            self.iconbitmap("image.jpg")
        except:
            print("Image not found")

        self.rowconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.add_menu_bar()
        self.add_sidebar()

        self.frames = {}

        workspace = Frame(self, bg=window_background)
        workspace.grid_propagate(False)
        workspace.rowconfigure(0, weight=1)
        workspace.columnconfigure(0, weight=1)
        workspace.grid(row=0, column=1, sticky=NSEW)

        country_containers = []

        for container in country_containers:
            frame = container(workspace, self)
            self.frames[container] = frame
            frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

    def add_menu_bar(self):
        menu_bar = Menu(self)
        self.config(menu=menu_bar)
        file_menu = Menu(menu_bar, tearoff=False)
        help_menu = Menu(menu_bar, tearoff=False)

        menu_bar.add_cascade(label="File", menu=file_menu)
        menu_bar.add_cascade(label="Help", menu=help_menu)

        file_menu.add_command(label="Admin Mode", command=None)
        file_menu.add_command(label="Export", command=None)
        file_menu.add_command(label="Exit", command=self.quit)

        help_menu.add_command(label="About", command=None)

    def show_frame(self, controller):
        frame = self.frames[controller]
        frame.tkraise()

    def show_listbox(self, listbox):
        listbox.tkraise()

    def add_sidebar(self):
        global search_icon
        search_value = StringVar()

        sidebar = Frame(self, background="#D2D7E0", borderwidth=2, relief=GROOVE)

        button1 = ttk.Button(
            sidebar,
            text="By Country",
            command=lambda: self.show_listbox(country_listbox),
        )
        button2 = ttk.Button(
            sidebar,
            text="By Tax",
            command=lambda: self.show_listbox(tax_listbox),
        )

        label_search_box = Label(sidebar, text="Tax Selection", bg="#D2D7E0")
        search_box = ttk.Entry(sidebar, textvariable=search_value)

        search_button = ttk.Button(
            sidebar,
            text="Search",
            compound=LEFT,
            command=lambda: NONE,  ## self.highlight_option(search_value),
        )

        try:
            search_icon = ImageTk.PhotoImage(
                Image.open("./images/search.png").resize((15, 15), Image.ANTIALIAS)
            )
            search_button.config(image=search_icon)
        except (FileNotFoundError):
            print("Image not found")

        country_listbox = Listbox(sidebar)
        tax_listbox = Listbox(sidebar)

        country_list = sorted([values[0] for values in country_data.values()])
        tax_list = sorted(
            [
                f"{tax_code} - {tax[0]}"
                for values in country_data.values()
                for tax in values[1:]
                for tax_code, tax in tax.items()
            ]
        )

        country_listbox.insert(END, *country_list)
        tax_listbox.insert(END, *tax_list)

        label_search_box.grid(row=0, columnspan=2)
        search_box.grid(row=1, column=0, padx=5, pady=10)
        search_button.grid(row=1, column=1, padx=5, pady=10, sticky=W)
        button1.grid(row=2, column=0, padx=5, pady=5, sticky=EW)
        button2.grid(row=2, column=1, padx=5, pady=1, sticky=EW)

        country_listbox.grid(row=3, column=0, columnspan=2, pady=10, padx=5, sticky=EW)
        tax_listbox.grid(row=3, column=0, columnspan=2, pady=10, padx=5, sticky=EW)

        sidebar.grid(row=0, column=0, rowspan=2, sticky=NS)

    def highlight_option(self, listbox, search_value):
        for i in range(listbox.size()):
            if search_value.get().lower() in listbox.get(i).lower():
                listbox.selection_set(i)
                listbox.activate(i)
                break


class CountryWindow(Frame):
    def __init__(self, parent, country):
        Frame.__init__(self, parent)
        self.country = country
        self.config(bg="white", relief=RAISED, borderwidth=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        self.add_canvas_flag(self, "./images/vg.png")

    def add_canvas_flag(self, filepath, height=100, width=150):
        canvas = Canvas(
            self,
            background="black",
            width=height,
            height=width,
            relief="ridge",
            highlightthickness=1,
        )
        return canvas.create_image(
            0,
            0,
            anchor=NW,
            image=ImageTk.PhotoImage(
                Image.open(filepath).resize((height, width), Image.ANTIALIAS)
            ),
        )


def main():
    app = AppWindow()
    app.mainloop()


if __name__ == "__main__":
    main()