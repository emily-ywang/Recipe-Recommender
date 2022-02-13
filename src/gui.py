import tkinter as tk
from functools import partial

from model import ingredient_searcher

ing_searcher = ingredient_searcher()

ingredients = ing_searcher.get_ingredients("")
ing_frame = None
sel_frame = None
buttons = []
sel_buttons = []
window = None
sel = ing_searcher.selected_ingredients
sv = None

# on ingredient click
def ing_select_click(ing):
    global ingredients
    ing_searcher.select_ingredient(ing)
    ingredients = ing_searcher.remove_selected(ing_searcher.get_ingredients(sv.get()))
    load_ingredient_buttons()
    load_selected_buttons()
    # ingredients.remove(ing)
    # print(ing)

def selected_click(ing):
    global sel, ingredients
    ing_searcher.remove_ingredient(ing)
    sel = ing_searcher.selected_ingredients
    ingredients = ing_searcher.remove_selected(ing_searcher.get_ingredients(sv.get()))
    # ingredients = ing_searcher.get_ingredients("")
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
    sv.trace_add("write", text_box_changed)
    search_bar = tk.Entry(window, width=20, bg="white", fg="black", textvariable=sv)
    search_bar.pack(pady=20)
    load_ingredient_buttons()

# main method
if __name__ == "__main__":
    window = tk.Tk()
    sv = tk.StringVar()
    window.title("Recipe Recommender 1.0")
    window.geometry("500x800")
    load_ingredient_screen()
    window.mainloop()
    ing_frame = None
