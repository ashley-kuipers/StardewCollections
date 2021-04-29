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

        self.dict = dict
        self.page = page

        # create page buttons
        self.button = Button(buttons_frame, text=page, command=self.up, width=11, bg=DARKER_BACKGROUND, font=BUTTON_FONT, activebackground=DARKER_BACKGROUND)

        # filling with widgets
        for item in self.dict:
            if item['page'] == page:
                # create widgets using the item class
                new_item = Item(item, self.frame, self.information_frame)

                # unless page == villager, then make villager subclass?
                # unless page == Fish, make fish subclass?

    def up(self):
        self.frame.tkraise()
        self.information_frame.tkraise()

