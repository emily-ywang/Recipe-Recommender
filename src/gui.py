import tkinter as tk
from functools import partial
from tkinter import LEFT
from PIL import Image, ImageTk
from model import ingredient_searcher
from bing_image_downloader import downloader
import string

ing_searcher = ingredient_searcher()
ingredients = ing_searcher.get_ingredients("")
recipes = ["eggs", "bacon", "pie", "hotdog"]
ing_frame = None
sel_frame = None
buttons = []
sel_buttons = []
window = None
sel = ing_searcher.selected_ingredients
sv = None
search_bar = None
get_button = None

# pull image from bing
def get_image(recipe: string):
    downloader.download(recipe, limit=1,  output_dir='resources', adult_filter_off=True,
                        force_replace=False, timeout=60, verbose=False)

# move on to recipes page
def to_recipes():
    clear_ingredients_window()
    draw_recipes()

# draw recipe buttons
def draw_recipes():
    r = 0
    c = 0
    ing_frame.pack_forget()
    sel_frame.pack_forget()
    for rec in recipes:
        #get_image(rec)
        image = Image.open("resources/" + rec + "/Image_1.jpg")
        image = image.resize((50, 50), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(image)
        button = tk.Button(ing_frame, text=rec, image=img, compound=LEFT, pady=20)
        button.grid(row=1, column=1)
        window.mainloop()
        c += 1
        if c > 2:
            c = 0
            r += 1

# clear ingredients window
def clear_ingredients_window():
    global ing_frame
    for b in buttons:
        b.destroy()
    for b in sel_buttons:
        b.destroy()
    search_bar.destroy()
    get_button.destroy()

# on ingredient click
def ing_select_click(ing):
    global ingredients
    ing_searcher.select_ingredient(ing)
    ingredients = ing_searcher.remove_selected(ing_searcher.get_ingredients(sv.get()))
    load_ingredient_buttons()
    load_selected_buttons()

def selected_click(ing):
    global sel, ingredients
    ing_searcher.remove_ingredient(ing)
    sel = ing_searcher.selected_ingredients
    ingredients = ing_searcher.remove_selected(ing_searcher.get_ingredients(sv.get()))
    load_ingredient_buttons()
    load_selected_buttons()

# load all ingredient buttons
def load_ingredient_buttons():
    global ing_frame
    for b in buttons:
        b.destroy()
    if ing_frame:
        ing_frame.pack_forget()
    ing_frame = tk.Frame(window)
    ing_frame.pack()
    r = 0
    c = 0
    for ing in ingredients[0:16]:
        if c == 2:
            c = 0
            r += 1
        c += 1
        b = tk.Button(ing_frame, text=ing, command=partial(ing_select_click, ing))
        b.grid(row=r, column=c)
        buttons.append(b)

# load all ingredient buttons
def load_selected_buttons():
    global sel_frame
    for b in sel_buttons:
        b.destroy()
    if sel_frame:
        sel_frame.pack_forget()
    sel_frame = tk.Frame(window, pady=100)
    sel_frame.pack()
    r = 15
    c = 0
    for ing in sel[0:30]:
        if c == 2:
            c = 0
            r += 1
        c += 1
        b = tk.Button(sel_frame, text=ing, command=partial(selected_click, ing))
        b.grid(row=r, column=c)
        sel_buttons.append(b)

# on text box change (a, b, c) do nothing!
def text_box_changed(a, b, c):
    # update ingredients list
    global ingredients
    ingredients = ing_searcher.remove_selected(ing_searcher.get_ingredients(sv.get()))
    load_ingredient_buttons()

# load ingredient screen
def load_ingredient_screen():
    global search_bar, get_button
    sv.trace_add("write", text_box_changed)
    search_bar = tk.Entry(window, width=20, bg="white", fg="black", textvariable=sv)
    search_bar.pack(pady=20)
    load_ingredient_buttons()
    get_button = tk.Button(window, text="Get recpes", command=partial(to_recipes), fg="black")
    get_button.place(x=350)
    get_button.place(y=700)

# main method
if __name__ == "__main__":
    window = tk.Tk()
    sv = tk.StringVar()
    window.title("Recipe Recommender 1.0")
    window.geometry("500x800")
    load_ingredient_screen()
    window.mainloop()
