from tkinter import *
import pandas
from tkinter import messagebox

from item_class import checked, total_hearts, total_gifts
from page_class import Page, DARKER_BACKGROUND

SAVE_FONT = ("Courier", 15, "bold")

window = Tk()
window.title("Stardew Collections")
window.config(padx=3, pady=3, bg=DARKER_BACKGROUND)

# excluded missing bundle for now
PAGES = ["Other", "Mining", "Animal", "Fish", "Winter", "Fall", "Summer", "Spring", "Achieves", "Villagers", "Gems", "Artifacts", "Cooking", "Fishing", "Ship 2", "Ship 1"]

# read csv information, put in dict
complete_df = pandas.read_csv("complete.csv", engine='python', keep_default_na=False)
complete_dict = complete_df.to_dict(orient="records")

# create images, check saved checked, hearts, gifts, setup dicts for each
for listing in complete_dict:
    listing["image"] = PhotoImage(file=listing["image_path"])
    
    checked[listing["item_name"]] = listing["checked"]

    if listing['page'] == "Villagers":
        total_hearts[listing["item_name"]] = listing["notes_3"]
        total_gifts[listing["item_name"]] = listing["notes_4"]

# create button frame
buttons_frame = Frame(window, bg=DARKER_BACKGROUND, width=100, height=100)
buttons_frame.grid(row=1, column=0, columnspan=2, sticky="news")

col = 7
row = 1
for page in PAGES:
    current_page = Page(window, page, complete_dict, buttons_frame)
    current_page.button.grid(row=row, column=col, sticky="news")
    col -= 1
    if col < 0:
        col = 7
        row = 0


def save():
    for thing in complete_dict:
        thing["checked"] = checked[thing["item_name"]]
        if thing['page'] == "Villagers":
            thing["notes_3"] = total_hearts[thing["item_name"]]
            thing["notes_4"] = total_gifts[thing["item_name"]]
    final_df = pandas.DataFrame(complete_dict)
    final_df.to_csv("complete.csv", index=False)
    messagebox.showinfo(title="Saved", message="You have saved successfully!")


save_button = Button(buttons_frame, text="Save Progress", bg=DARKER_BACKGROUND, command=save, width=20, font=SAVE_FONT, activebackground=DARKER_BACKGROUND)
save_button.grid(column=9, row=0, sticky="NEWS", rowspan=2)

window.mainloop()


