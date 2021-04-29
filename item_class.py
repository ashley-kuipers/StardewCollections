from tkinter import *

BACKGROUND = "#F7B970"
DARKER_BACKGROUND = "#D67702"
RIGHT_CLICKED_BG = "#99d973"
TWO_GIFTS_BG = "#dec0f1"
RAIN = "#92BBCD"
SUN = "#F8D541"

ITEM_NAME_FONT = ("Courier", 14, "bold underline")
ITEM_TEXT_FONT = ("Courier", 12, "normal")
HEART_BUTTON_FONT = ("Courier", 12, "bold")

GIFT = "\U0001F381"
CHECKBOX = "\u2611"
EMPTY_BOX = "\u2610"
HEART = "\u2665"
EMPTY_HEART = "\u2661"
RESET = "\u27F2"

checked = {}
total_hearts = {}
total_gifts = {}


class Item:
    def __init__(self, item, frame, info_frame):
        self.item_name = item['item_name']
        self.image = item['image']
        self.button_bg = BACKGROUND
        self.page = item['page']
        self.column = item['column']
        self.row = item['row']
        self.info_frame = info_frame

        if item["notes_1"]:
            self.notes_1 = item["notes_1"]
        else:
            self.notes_1 = ""

        if item["notes_2"]:
            self.notes_2 = item["notes_2"]
        else:
            self.notes_2 = ""

        if item["notes_3"]:
            self.notes_3 = item["notes_3"]
        else:
            self.notes_3 = ""

        if item["notes_4"]:
            self.notes_4 = item["notes_4"]
        else:
            self.notes_4 = ""

        # create buttons
        self.total_buttons = []
        self.new_button = Button(frame, image=self.image, bg=self.button_bg, highlightthickness=0,
                                 activebackground=DARKER_BACKGROUND, command=self.change_background, width=60,
                                 height=60)

        # checked if item is checked & adjust background
        self.checked = checked[self.item_name]
        if self.checked:
            self.change_background()        

        # add buttons to screen
        self.new_button.grid(column=self.column, row=self.row, sticky="W", padx=1, pady=1)
        self.total_buttons.append(self.new_button)

        # add bindings for hover and right click
        self.new_button.bind("<Enter>", self.on_hover)
        self.new_button.bind("<Leave>", self.on_leave)
        self.new_button.bind("<Button-2>", self.right_click)
        self.new_button.bind("<Button-3>", self.right_click)

        # add heart and gifts plus/reset buttons
        self.heart_frame = Frame(info_frame, bg=DARKER_BACKGROUND, pady=10)
        self.add_heart = Button(self.heart_frame, bg=self.button_bg, highlightthickness=0, text=f"+{HEART}",
                                 activebackground=DARKER_BACKGROUND, command=self.plus_heart, width=3,
                                 height=1, font=HEART_BUTTON_FONT)
        self.add_gift = Button(self.heart_frame, bg=self.button_bg, highlightthickness=0, text=f"+{GIFT}",
                               activebackground=DARKER_BACKGROUND, command=self.plus_gift, width=3,
                               height=1, font=HEART_BUTTON_FONT)
        self.reset_h = Button(self.heart_frame, bg=self.button_bg, highlightthickness=0, text=f"{RESET}{HEART}",
                              activebackground=DARKER_BACKGROUND, command=self.reset_hearts, width=3,
                              height=1, font=HEART_BUTTON_FONT)
        self.reset_g = Button(self.heart_frame, bg=self.button_bg, highlightthickness=0, text=f"{RESET}{GIFT}",
                              activebackground=DARKER_BACKGROUND, command=self.reset_gifts, width=3,
                              height=1, font=HEART_BUTTON_FONT)
        self.add_heart.grid(column=0, row=0, padx=5)
        self.reset_h.grid(column=1, row=0, padx=5)
        self.add_gift.grid(column=2, row=0, padx=5)
        self.reset_g.grid(column=3, row=0, padx=5)

        # add item name label
        self.item_name_label = Label(self.info_frame, text=f'{self.item_name}', bg=DARKER_BACKGROUND,
                                     font=ITEM_NAME_FONT, justify=CENTER, width=20)

        # add notes labels
        self.notes_1_label_text = item['notes_1_name']
        self.notes_2_label_text = item['notes_2_name']
        self.notes_3_label_text = item['notes_3_name']
        self.notes_4_label_text = item['notes_4_name']

        # change background to blue or yellow for weather in fish
        if self.button_bg == DARKER_BACKGROUND:
            pass
        else:
            self.fish_background()

        # add hearts and gifts to villagers
        if self.page == "Villagers":
            self.notes_3 = ""
            self.notes_4 = ""
            self.hearts = int(total_hearts[self.item_name])
            self.gifts = int(total_gifts[self.item_name])

            for full_heart in range(self.hearts):
                self.notes_3 += f"{HEART} "
            for full_gift in range(self.gifts):
                self.notes_3 += f"{CHECKBOX} "

            empty_hearts = 10 - self.hearts
            empty_gifts = 2 - self.gifts

            for empty_heart in range(empty_hearts):
                self.notes_3 += f"{EMPTY_HEART} "
            for gift in range(empty_gifts):
                self.notes_4 += f"{EMPTY_BOX} "

        # add notes texts - have to check if there is content in that column
        if self.notes_1:
            self.notes_1_text = Message(self.info_frame,
                                        text=f"{self.notes_1_label_text}\n{self.notes_1}",
                                        bg=DARKER_BACKGROUND, font=ITEM_TEXT_FONT,
                                        justify=CENTER, width=240)
        else:
            self.notes_1_text = Message(self.info_frame, text="", bg=DARKER_BACKGROUND,)

        if self.notes_2:
            self.notes_2_text = Message(self.info_frame,
                                        text=f"\n{self.notes_2_label_text}\n{self.notes_2}\n",
                                        bg=DARKER_BACKGROUND, font=ITEM_TEXT_FONT,
                                        justify=CENTER, width=240)
        else:
            self.notes_2_text = Message(self.info_frame, text="", bg=DARKER_BACKGROUND,)

        if self.notes_3:
            self.notes_3_text = Message(self.info_frame, text=f"{self.notes_3_label_text}\n{self.notes_3}",
                                        bg=DARKER_BACKGROUND, font=ITEM_TEXT_FONT,
                                        justify=CENTER, width=240)
        else:
            self.notes_3_text = Message(self.info_frame, text="", bg=DARKER_BACKGROUND,)

        if self.notes_4:
            self.notes_4_text = Message(self.info_frame, text=f"\n{self.notes_4_label_text}\n{self.notes_4}",
                                            bg=DARKER_BACKGROUND, font=ITEM_TEXT_FONT,
                                            justify=CENTER, width=240)   
        else:
            self.notes_4_text = Message(self.info_frame, text="", bg=DARKER_BACKGROUND)

    # show ingredients and source info on hover
    def on_hover(self, event):
        self.item_name_label.pack(padx=10, pady=5, fill=X)
        self.notes_1_text.pack(padx=10, fill=X)
        self.notes_2_text.pack(padx=10, fill=X)
        self.notes_3_text.pack(padx=10, fill=X)
        self.notes_4_text.pack(padx=10, fill=X)

    # what happens when you unhover
    def on_leave(self, enter):
        # if it is right clicked, keep the title and notes 1 on
        if self.button_bg == RIGHT_CLICKED_BG:
            if self.page == "Villagers":
                self.notes_2_text.pack_forget()
            else:
                self.notes_2_text.pack_forget()
                self.notes_3_text.pack_forget()
                self.notes_4_text.pack_forget()
        else:
            self.item_name_label.pack_forget()
            self.notes_1_text.pack_forget()
            self.notes_2_text.pack_forget()
            self.notes_3_text.pack_forget()
            self.notes_4_text.pack_forget()

        # if you have given 2 gifts, keep different background
        self.villager_background()

    def change_background(self):
        if self.button_bg != DARKER_BACKGROUND:
            self.new_button.config(bg=DARKER_BACKGROUND, relief="sunken")
            self.button_bg = DARKER_BACKGROUND
            self.checked = True
            checked[self.item_name] = True

        else:
            self.new_button.config(bg=BACKGROUND, relief="raised")
            self.button_bg = BACKGROUND
            self.checked = False
            checked[self.item_name] = False

            self.fish_background()

    def right_click(self, event):
        # if un right clicking, delete everything
        if self.button_bg == RIGHT_CLICKED_BG:

            self.new_button.config(bg=BACKGROUND)
            self.button_bg = BACKGROUND

            self.item_name_label.pack_forget()
            self.notes_1_text.pack_forget()
            self.notes_2_text.pack_forget()
            self.notes_3_text.pack_forget()
            self.notes_4_text.pack_forget()
            self.heart_frame.pack_forget()

        # if right clicking, keep label and notes 1 (and hearts/gifts for villagers)
        else:
            
            self.new_button.config(bg=RIGHT_CLICKED_BG)
            self.button_bg = RIGHT_CLICKED_BG

            self.item_name_label.pack(padx=5, pady=5, fill=X)
            self.notes_1_text.pack(padx=10, fill=X)
            
            if self.page == "Villagers":
                self.heart_frame.pack()
                self.notes_3_text.pack(padx=10, fill=X)
                self.notes_4_text.pack(padx=10, fill=X)

    def plus_heart(self):
        self.notes_3 = self.notes_3.replace(EMPTY_HEART, HEART, 1)
        self.notes_3_text.config(text=f"{self.notes_3_label_text}\n{self.notes_3}")
        self.hearts += 1
        total_hearts[self.item_name] = self.hearts

    def reset_hearts(self):
        self.notes_3 = self.notes_3.replace(HEART, EMPTY_HEART)
        self.notes_3_text.config(text=f"{self.notes_3_label_text}\n{self.notes_3}")
        self.hearts = 0
        total_hearts[self.item_name] = self.hearts

    def reset_gifts(self):
        self.notes_4 = self.notes_4.replace(CHECKBOX, EMPTY_BOX)
        self.notes_4_text.config(text=f"{self.notes_4_label_text}\n{self.notes_4}")
        self.gifts = 0
        total_gifts[self.item_name] = self.gifts

    def plus_gift(self):
        self.notes_4 = self.notes_4.replace(EMPTY_BOX, CHECKBOX, 1)
        self.notes_4_text.config(text=f"{self.notes_4_label_text}\n{self.notes_4}")
        self.gifts += 1
        total_gifts[self.item_name] = self.gifts

    def fish_background(self):
        if self.page == "Fishing" or self.page == "Fish":
            if self.notes_4 == "Rain":
                self.new_button.config(bg=RAIN)
            elif self.notes_4 == "Sun":
                self.new_button.config(bg=SUN)

    def villager_background(self):
        if self.page == "Villagers":
            if self.gifts > 1:
                if self.button_bg == BACKGROUND:
                    self.new_button.config(bg=TWO_GIFTS_BG, relief="raised")
                elif self.button_bg == DARKER_BACKGROUND:
                        pass