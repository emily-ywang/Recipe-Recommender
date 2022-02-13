import tkinter as tk
from functools import partial

ingredients = ["milk", "rabbit", "juice", "calamari", "hot dog", "orange", "penis", "frog", "ginger", "arsenic"]
window = None
sv = None

# on ingredient click
def ing_click(ing):
    print(ing)

# load all ingredient buttons
def load_ingredient_buttons():
    frame1 = tk.Frame(window)
    frame1.pack(pady=20)
    for ing in ingredients:
        b = tk.Button(frame1, text=ing, command=partial(ing_click, ing))
        b.pack(side="left")
        pass

# on text box change
def text_box_changed(a, b, c):
    # update ingredients list
    load_ingredient_buttons()

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





