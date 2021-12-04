# Michael Luther CIS345 - Tu/Thurs - 10:30AM - Project GUI

from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from dataclasses import dataclass
from country_loader import load_countries


widget_background = "#D2D7E0"
window_background = "#5A6881"


class AppWindow(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.geometry("850x480")
        self.title("SpeedTax")
        self.countries = load_countries("mdluther-country_data.json")

        try:
            self.iconbitmap("./images/icon.ico")
        except:
            print("Image not found")

        self.rowconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.add_menu_bar()
        self.add_sidebar()

        self.country_frames = {}

        workspace = Frame(self, bg=window_background)
        workspace.grid_propagate(False)
        workspace.rowconfigure(0, weight=1)
        workspace.columnconfigure(0, weight=1)

        for code, country_object in self.countries.items():
            frame = CountryFrame(workspace, country_object)
            self.country_frames[code] = frame
            frame.grid(row=0, column=0, sticky=NSEW)

        workspace.grid(row=0, column=1, sticky=NSEW)

        self.show_frame("CU")

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

    def show_frame(self, code):
        frame = self.country_frames[code]
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

        for country_code, country in self.countries.items():
            country_listbox.insert(END, f"{country_code} - {country.name}")
            for tax, properties in country.taxes.items():
                tax_listbox.insert(END, f"{tax} - {properties.description}")

        label_search_box.grid(row=0, columnspan=2)
        search_box.grid(row=1, column=0, padx=5, pady=10)
        search_button.grid(row=1, column=1, padx=5, pady=10, sticky=W)
        button1.grid(row=2, column=0, padx=5, pady=5, sticky=EW)
        button2.grid(row=2, column=1, padx=5, pady=1, sticky=EW)

        country_listbox.grid(row=3, column=0, columnspan=2, pady=10, padx=5, sticky=EW)
        tax_listbox.grid(row=3, column=0, columnspan=2, pady=10, padx=5, sticky=EW)

        sidebar.grid(row=0, column=0, rowspan=2, sticky=NS)

    def search_listbox(self, listbox, search_value):
        for i in range(listbox.size()):
            if search_value.get().lower() in listbox.get(i).lower():
                listbox.selection_set(i)
                listbox.activate(i)
                break


class CountryFrame(Frame):
    def __init__(self, parent, country):
        Frame.__init__(self, parent)
        self.country = country
        self.config(bg="black", relief=RAISED, borderwidth=1)

        country_code = Label(self, text=self.country.country_code)
        name = Label(self, text=self.country.name)

        country_code.pack()
        name.pack()

        # country_code.grid(row=0, column=0)
        #  name.grid(row=0, column=1)

        tax_code_labels = []
        tax_properties_headers = []
        tax_properties_labels = []

        for tax, properties in self.country.taxes.items():
            tax_code_labels.append(Label(self, text=f"{tax} Tax"))

            tax_properties_labels.append(Label(self, text=f"{tax} Description:"))
            tax_properties_headers.append(Label(self, text=f"{tax} Type:"))
            tax_properties_headers.append(Label(self, text=f"{tax} Exemption(s):"))

            tax_properties_labels.append(Label(self, text=f"{properties.description}"))
            tax_properties_labels.append(Label(self, text=f"{properties.tax_type}"))
            tax_properties_labels.append(Label(self, text=f"{properties.exemptions}"))

            for label in tax_code_labels:
                label.pack()
            for label in tax_properties_headers:
                label.pack()
            for label in tax_properties_labels:
                label.pack()

        ## Working on grid. For now just packed.
        # for i in range(len(tax_code_labels)):
        #     count = 0
        #    tax_code_labels[i].grid(row=count, column=0)
        #    for j in range(len(tax_properties_headers)):
        #        count += 1
        #        tax_properties_headers[j].grid(row=count, column=1)
        #        for k in range(len(tax_properties_labels)):
        #            count += 1
        #             tax_properties_headers[k].grid(row=count, column=2)
        #     count += 1

        raw_image = Image.open("./images/flags/ae.png")
        raw_image.resize(
            (width := 50, width * int(raw_image.size[0] / raw_image.size[1])),
            Image.ANTIALIAS,
        )
        flag_image = ImageTk.PhotoImage(raw_image)

        flag_widget = Label(self, image=flag_image)
        flag_widget.photo = flag_image

        flag_widget.pack()
        # flag_widget.grid(row=0, column=2)


def main():
    app = AppWindow()
    app.mainloop()


if __name__ == "__main__":
    main()
