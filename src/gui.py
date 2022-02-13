import tkinter as tk
from functools import partial

from model import ingredient_searcher

ing_searcher = ingredient_searcher()

ingredients = ing_searcher.get_ingredients("")
ing_frame = None
buttons = []
window = None
sv = None

# on ingredient click
def ing_select_click(ing):
    ing_searcher.select(ing)
    # ingredients.remove(ing)
    # print(ing)


# load all ingredient buttons
def load_ingredient_buttons():
    global ing_frame
    for b in buttons:
        b.destroy()
    if ing_frame:
        ing_frame.pack_forget()
    ing_frame = tk.Frame(window)
    ing_frame.pack(pady=20)
    for ing in ingredients:
        b = tk.Button(ing_frame, text=ing, command=partial(ing_select_click, ing))
        b.pack(side="left")
        buttons.append(b)
        pass


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


if __name__ == "__main__":
    window = tk.Tk()
    sv = tk.StringVar()
    window.title("Recipe Recommender 1.0")
    window.geometry("500x800")
    load_ingredient_screen()
    window.mainloop()
    ing_frame = None
