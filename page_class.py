from tkinter import *
from item_class import Item

BACKGROUND = "#F7B970"
DARKER_BACKGROUND = "#D67702"

BUTTON_FONT = ("Courier", 8, "normal")


class Page:
    def __init__(self, master, page, dict, buttons_frame):

        # create page frame
        self.frame = Frame(master, bg=DARKER_BACKGROUND, width=160, height=100, pady=10)
        self.frame.grid(row=0, column=0, sticky="news")
        
        self.information_frame = Frame(master, bg=DARKER_BACKGROUND, width=250, height=100)
        self.information_frame.grid(row=0, column=1, sticky="news")

        self.buttons_frame = buttons_frame

        self.dict = dict
        self.page = page

        # create page buttons
        self.button = Button(self.buttons_frame, text=page, command=self.up, width=11, bg=DARKER_BACKGROUND, font=BUTTON_FONT, activebackground=DARKER_BACKGROUND)

        self.widgets=[]
        # filling with widgets
        for item in self.dict:
            if item['page'] == page:
                # create widgets using the item class
                new_item = Item(item, self.frame, self.information_frame)
                self.widgets.append(new_item)
                # unless page == villager, then make villager subclass?
                # unless page == Fish, make fish subclass?

        self.reset_button = Button(self.buttons_frame, text=f"Reset Ship 1", bg=DARKER_BACKGROUND, width=16,
                                   font=("Courier", 14, "bold"), activebackground=DARKER_BACKGROUND,
                                   command=self.reset)
        self.reset_button.grid(column=10, row=0, sticky="NEWS", rowspan=2)

    def up(self):
        self.frame.tkraise()
        self.information_frame.tkraise()
        self.reset_button = Button(self.buttons_frame, text=f"Reset {self.page}", bg=DARKER_BACKGROUND, width=16,
                                   font=("Courier", 14, "bold"), activebackground=DARKER_BACKGROUND,
                                   command=self.reset)
        self.reset_button.grid(column=10, row=0, sticky="NEWS", rowspan=2)

    def reset(self):
        for item in self.widgets:
            item.reset_background()

